#!/usr/bin/env python3
"""Write the one-line fridge note to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Notes From a Passive-Aggressive Fridge" bounty.
The program writes exactly one line of text and nothing else.

How the line targets the brief: the note is dry, petty and specific --
the fridge keeps a day count, resents being opened for staring rather
than food, and delivers the verdict through the yogurt, the one item
that has outlasted every diet. It reads like a real door-screen note.
"""

import os
from pathlib import Path

LINE = "Day 12 of you opening me just to stare. I'm a fridge, not a vision board. The yogurt has shown more commitment than your diet."

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the entry line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line within the limit.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
