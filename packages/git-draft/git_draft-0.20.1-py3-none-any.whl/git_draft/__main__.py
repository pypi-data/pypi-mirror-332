"""CLI entry point"""

from __future__ import annotations

import importlib.metadata
import logging
import optparse
import sys

from .bots import Operation, load_bot
from .common import PROGRAM, Config, UnreachableError, ensure_state_home
from .drafter import Drafter
from .editor import open_editor
from .prompt import TemplatedPrompt
from .store import Store


def new_parser() -> optparse.OptionParser:
    parser = optparse.OptionParser(
        prog=PROGRAM,
        version=importlib.metadata.version("git_draft"),
    )

    parser.disable_interspersed_args()

    parser.add_option(
        "--log",
        help="show log path and exit",
        action="store_true",
    )
    parser.add_option(
        "--root",
        help="path used to locate repository",
        dest="root",
    )

    def add_command(name: str, **kwargs) -> None:
        def callback(_option, _opt, _value, parser) -> None:
            parser.values.command = name

        parser.add_option(
            f"-{name[0].upper()}",
            f"--{name}",
            action="callback",
            callback=callback,
            **kwargs,
        )

    add_command("finalize", help="apply current draft to original branch")
    add_command("generate", help="start a new draft from a prompt")
    add_command("revert", help="discard the current draft")

    parser.add_option(
        "-b",
        "--bot",
        dest="bot",
        help="bot name",
    )
    parser.add_option(
        "-c",
        "--checkout",
        help="check out generated changes",
        action="store_true",
    )
    parser.add_option(
        "-d",
        "--delete",
        help="delete draft after finalizing or discarding",
        action="store_true",
    )
    parser.add_option(
        "-r",
        "--reset",
        help="reset index before generating a new draft",
        action="store_true",
    )
    parser.add_option(
        "-s",
        "--sync",
        help="commit prior worktree changes separately",
        action="store_true",
    )
    parser.add_option(
        "-t",
        "--timeout",
        dest="timeout",
        help="bot generation timeout",
    )

    return parser


def print_operation(op: Operation) -> None:
    print(op)


def main() -> None:
    config = Config.load()
    (opts, args) = new_parser().parse_args()

    log_path = ensure_state_home() / "log"
    if opts.log:
        print(log_path)
        return
    logging.basicConfig(level=config.log_level, filename=str(log_path))

    drafter = Drafter.create(
        store=Store.persistent(),
        path=opts.root,
        operation_hook=print_operation,
    )
    command = getattr(opts, "command", "generate")
    if command == "generate":
        bot_config = None
        if opts.bot:
            bot_configs = [c for c in config.bots if c.name == opts.bot]
            if len(bot_configs) != 1:
                raise ValueError(f"Found {len(bot_configs)} matching bots")
            bot_config = bot_configs[0]
        elif config.bots:
            bot_config = config.bots[0]
        bot = load_bot(bot_config)

        prompt: str | TemplatedPrompt
        if args:
            prompt = TemplatedPrompt.parse(args[0], *args[1:])
        else:
            if sys.stdin.isatty():
                prompt = open_editor("Enter your prompt here...")
            else:
                prompt = sys.stdin.read()

        drafter.generate_draft(
            prompt, bot, checkout=opts.checkout, reset=opts.reset
        )
    elif command == "finalize":
        drafter.finalize_draft(delete=opts.delete)
    elif command == "revert":
        drafter.revert_draft(delete=opts.delete)
    else:
        raise UnreachableError()


if __name__ == "__main__":
    main()
