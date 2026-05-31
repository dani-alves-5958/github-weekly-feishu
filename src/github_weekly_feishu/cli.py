from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from .converter import build_doc


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="github-weekly-feishu",
        description="Convert GitHub weekly Markdown notes to Feishu/Word friendly DOCX.",
    )
    parser.add_argument("source", type=Path, help="Input Markdown file.")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output DOCX path. Defaults to SOURCE with a .docx suffix.",
    )
    parser.add_argument(
        "--assets-root",
        type=Path,
        help="Base directory for relative image paths. Defaults to SOURCE parent.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    source = args.source

    if not source.exists():
        print(f"error: input file does not exist: {source}", file=sys.stderr)
        return 2
    if not source.is_file():
        print(f"error: input path is not a file: {source}", file=sys.stderr)
        return 2

    output = args.output or source.with_suffix(".docx")
    generated = build_doc(source=source, output=output, assets_root=args.assets_root)
    print(generated)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
