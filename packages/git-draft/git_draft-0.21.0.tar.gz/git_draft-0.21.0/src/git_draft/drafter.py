from __future__ import annotations

import dataclasses
from datetime import datetime
import json
import logging
from pathlib import PurePosixPath
import re
import textwrap
import time
from typing import Match, Sequence

import git

from .bots import Bot, Goal
from .common import JSONObject, random_id
from .prompt import PromptRenderer, TemplatedPrompt
from .store import Store, sql
from .toolbox import StagingToolbox, ToolVisitor


_logger = logging.getLogger(__name__)


@dataclasses.dataclass(frozen=True)
class _Branch:
    """Draft branch"""

    _name_pattern = re.compile(r"draft/(.+)")

    suffix: str

    @property
    def name(self) -> str:
        return f"draft/{self.suffix}"

    def __str__(self) -> str:
        return self.name

    @classmethod
    def active(cls, repo: git.Repo) -> _Branch | None:
        match: Match | None = None
        if not repo.head.is_detached:
            match = cls._name_pattern.fullmatch(repo.active_branch.name)
        if not match:
            return None
        return _Branch(match[1])

    @staticmethod
    def new_suffix():
        return random_id(9)


class Drafter:
    """Draft state orchestrator"""

    def __init__(self, store: Store, repo: git.Repo) -> None:
        with store.cursor() as cursor:
            cursor.executescript(sql("create-tables"))
        self._store = store
        self._repo = repo

    @classmethod
    def create(cls, store: Store, path: str | None = None) -> Drafter:
        return cls(store, git.Repo(path, search_parent_directories=True))

    def generate_draft(
        self,
        prompt: str | TemplatedPrompt,
        bot: Bot,
        tool_visitors: Sequence[ToolVisitor] | None = None,
        checkout: bool = False,
        reset: bool = False,
        sync: bool = False,
        timeout: float | None = None,
    ) -> str:
        if isinstance(prompt, str) and not prompt.strip():
            raise ValueError("Empty prompt")
        if self._repo.is_dirty(working_tree=False):
            if not reset:
                raise ValueError("Please commit or reset any staged changes")
            self._repo.index.reset()

        branch = _Branch.active(self._repo)
        if branch:
            self._stage_changes(sync)
            _logger.debug("Reusing active branch %s.", branch)
        else:
            branch = self._create_branch(sync)
            _logger.debug("Created branch %s.", branch)

        operation_recorder = _OperationRecorder()
        tool_visitors = [operation_recorder] + list(tool_visitors or [])
        toolbox = StagingToolbox(self._repo, tool_visitors)
        if isinstance(prompt, TemplatedPrompt):
            renderer = PromptRenderer.for_toolbox(toolbox)
            prompt_contents = renderer.render(prompt)
        else:
            prompt_contents = prompt

        with self._store.cursor() as cursor:
            [(prompt_id,)] = cursor.execute(
                sql("add-prompt"),
                {
                    "branch_suffix": branch.suffix,
                    "contents": prompt_contents,
                },
            )

        start_time = time.perf_counter()
        goal = Goal(prompt_contents, timeout)
        action = bot.act(goal, toolbox)
        end_time = time.perf_counter()
        walltime = end_time - start_time

        toolbox.trim_index()
        title = action.title
        if not title:
            title = _default_title(prompt_contents)
        commit = self._repo.index.commit(
            f"draft! {title}\n\n{prompt_contents}",
            skip_hooks=True,
        )

        with self._store.cursor() as cursor:
            cursor.execute(
                sql("add-action"),
                {
                    "commit_sha": commit.hexsha,
                    "prompt_id": prompt_id,
                    "walltime": walltime,
                },
            )
            cursor.executemany(
                sql("add-operation"),
                [
                    {
                        "commit_sha": commit.hexsha,
                        "tool": o.tool,
                        "reason": o.reason,
                        "details": json.dumps(o.details),
                        "started_at": o.start,
                    }
                    for o in operation_recorder.operations
                ],
            )

        _logger.info("Generated draft.")
        if checkout:
            self._repo.git.checkout("--", ".")
        return str(branch)

    def finalize_draft(self, delete=False) -> str:
        return self._exit_draft(revert=False, delete=delete)

    def revert_draft(self, delete=False) -> str:
        return self._exit_draft(revert=True, delete=delete)

    def _create_branch(self, sync: bool) -> _Branch:
        if self._repo.head.is_detached:
            raise RuntimeError("No currently active branch")
        origin_branch = self._repo.active_branch.name
        origin_sha = self._repo.commit().hexsha

        self._repo.git.checkout(detach=True)
        sync_sha = self._stage_changes(sync)
        suffix = _Branch.new_suffix()

        with self._store.cursor() as cursor:
            cursor.execute(
                sql("add-branch"),
                {
                    "suffix": suffix,
                    "repo_path": self._repo.working_dir,
                    "origin_branch": origin_branch,
                    "origin_sha": origin_sha,
                    "sync_sha": sync_sha,
                },
            )

        branch = _Branch(suffix)
        branch_ref = self._repo.create_head(branch.name)
        self._repo.git.checkout(branch_ref)
        return branch

    def _stage_changes(self, sync: bool) -> str | None:
        self._repo.git.add(all=True)
        if not sync or not self._repo.is_dirty(untracked_files=True):
            return None
        ref = self._repo.index.commit("draft! sync")
        return ref.hexsha

    def _exit_draft(self, *, revert: bool, delete: bool) -> str:
        branch = _Branch.active(self._repo)
        if not branch:
            raise RuntimeError("Not currently on a draft branch")

        with self._store.cursor() as cursor:
            rows = cursor.execute(
                sql("get-branch-by-suffix"), {"suffix": branch.suffix}
            )
            if not rows:
                raise RuntimeError("Unrecognized branch")
            [(origin_branch, origin_sha, sync_sha)] = rows

        if (
            revert
            and sync_sha
            and self._repo.commit(origin_branch).hexsha != origin_sha
        ):
            raise RuntimeError("Parent branch has moved, please rebase")

        # We do a small dance to move back to the original branch, keeping the
        # draft branch untouched. See https://stackoverflow.com/a/15993574 for
        # the inspiration.
        self._repo.git.checkout(detach=True)
        self._repo.git.reset("-N", origin_branch)
        self._repo.git.checkout(origin_branch)

        # Next, we revert the relevant files if needed. If a sync commit had
        # been created, we simply revert to it. Otherwise we compute which
        # files have changed due to draft commits and revert only those.
        if revert:
            if sync_sha:
                self._repo.git.checkout(sync_sha, "--", ".")
            else:
                diffed = set(self._changed_files(f"{origin_branch}..{branch}"))
                dirty = [p for p in self._changed_files("HEAD") if p in diffed]
                if dirty:
                    self._repo.git.checkout("--", *dirty)

        if delete:
            self._repo.git.branch("-D", branch.name)

        return branch.name

    def _changed_files(self, spec) -> Sequence[str]:
        return self._repo.git.diff(spec, name_only=True).splitlines()


class _OperationRecorder(ToolVisitor):
    def __init__(self) -> None:
        self.operations = list[_Operation]()

    def on_list_files(
        self, paths: Sequence[PurePosixPath], reason: str | None
    ) -> None:
        self._record(reason, "list_files", count=len(paths))

    def on_read_file(
        self, path: PurePosixPath, contents: str | None, reason: str | None
    ) -> None:
        self._record(
            reason,
            "read_file",
            path=str(path),
            size=-1 if contents is None else len(contents),
        )

    def on_write_file(
        self, path: PurePosixPath, contents: str, reason: str | None
    ) -> None:
        self._record(reason, "write_file", path=str(path), size=len(contents))

    def on_delete_file(self, path: PurePosixPath, reason: str | None) -> None:
        self._record(reason, "delete_file", path=str(path))

    def _record(self, reason: str | None, tool: str, **kwargs) -> None:
        self.operations.append(
            _Operation(
                tool=tool, details=kwargs, reason=reason, start=datetime.now()
            )
        )


@dataclasses.dataclass(frozen=True)
class _Operation:
    tool: str
    details: JSONObject
    reason: str | None
    start: datetime


def _default_title(prompt: str) -> str:
    return textwrap.shorten(prompt, break_on_hyphens=False, width=72)
