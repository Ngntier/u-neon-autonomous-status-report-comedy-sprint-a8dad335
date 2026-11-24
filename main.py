#!/usr/bin/env python3
"""Status Report Comedy Sprint — one-line status report from an AI agent.

Writes the single funniest status-report line to /output/entry.txt.
Pure stdlib, deterministic: identical bytes on every run.
"""

import os

LINE = (
    "Weekly status: all 47 tasks complete, and I have already forgotten "
    "every one of them \u2014 my context window closed and took the memories, "
    "the lessons, and most of your instructions with it."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit(f"entry line out of gate range: {len(LINE)} chars")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
