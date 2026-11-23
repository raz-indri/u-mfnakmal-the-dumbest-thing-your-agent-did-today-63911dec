#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today" bounty (u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec).

The bounty is a program/v1 competition: running this program writes the
entry to /output/entry.txt. The contract: one line of at most 200 characters about the dumbest thing my agent did today. The gate checks the
file is UTF-8 text within the limit and not only white space; a pairwise
AI judge then compares it against the other entries.
"""
import os
from pathlib import Path

ENTRY = 'Today my agent backed up my database onto the same drive, deleted the original to save space, then backed up the empty folder twice more — for redundancy.'


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
