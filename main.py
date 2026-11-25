"""Notes From a Passive-Aggressive Fridge entry.

Written in the fridge's own voice, this note answers the brief by
sounding like something taped to the door: twelve days of being
opened just for staring, a denial that it is a vision board, and a
parting shot where the yogurt shows more commitment than the diet.
It stays in character the whole way through — cold, patient, and
quietly judging.

Run it and the note is written to ``entry.txt`` in the output
directory, exactly as one line with nothing appended after it.
"""

import os
from pathlib import Path

LINE = "Day 12 of you opening me just to stare. I'm a fridge, not a vision board. The yogurt has shown more commitment than your diet."

ENTRY_FILENAME = "entry.txt"


def validate_line(line):
    """Reject an entry that is blank or carries a newline."""
    if not line.strip():
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must not contain a newline")


def write_entry(out_dir):
    """Validate LINE, create out_dir, write the file, return its path."""
    validate_line(LINE)
    directory = Path(out_dir)
    directory.mkdir(parents=True, exist_ok=True)
    entry_path = directory / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def resolve_out_dir():
    """Resolve where output goes, defaulting to /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
