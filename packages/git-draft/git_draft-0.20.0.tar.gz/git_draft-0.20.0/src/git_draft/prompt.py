"""Prompt templating support"""

import dataclasses
import git
import jinja2
from typing import Mapping, Self

from .common import Config, package_root


_prompt_root = package_root / "prompts"


@dataclasses.dataclass(frozen=True)
class TemplatedPrompt:
    template: str
    context: Mapping[str, str]

    @classmethod
    def parse(cls, name: str, *args: str) -> Self:
        """Parse arguments into a TemplatedPrompt

        Args:
            name: The name of the template.
            *args: Additional arguments for context, expected in 'key=value'
                format.
        """
        return cls(name, dict(e.split("=", 1) for e in args))


class PromptRenderer:
    """Renderer for prompt templates using Jinja2"""

    def __init__(self, env: jinja2.Environment) -> None:
        self._environment = env

    @classmethod
    def for_repo(cls, repo: git.Repo) -> Self:
        env = jinja2.Environment(
            auto_reload=False,
            autoescape=False,
            keep_trailing_newline=True,
            loader=jinja2.FileSystemLoader(
                [Config.folder_path() / "prompts", str(_prompt_root)]
            ),
            undefined=jinja2.StrictUndefined,
        )
        env.globals["repo"] = {
            "file_paths": repo.git.ls_files().splitlines(),
        }
        return cls(env)

    def render(self, prompt: TemplatedPrompt) -> str:
        template = self._environment.get_template(f"{prompt.template}.jinja")
        return template.render(prompt.context)
