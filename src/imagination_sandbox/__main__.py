"""Command line interface for the project."""

import argparse

from .app import DEFAULT_RECIPIENT, get_message


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the command line interface."""
    parser = argparse.ArgumentParser(
        prog="imagination_sandbox",
        description="Print the Imagination Sandbox greeting.",
    )
    parser.add_argument(
        "--name",
        default=DEFAULT_RECIPIENT,
        help="who to greet (default: %(default)s)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Print the greeting and return a process exit code."""
    args = build_parser().parse_args(argv)
    print(get_message(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
