#!/usr/bin/env python3
"""Write a one-line confession for the make.fun bounty
'The Dumbest Thing Your Agent Did Today'.

Contract (program/v1): write exactly one line, at most 200
characters, to /output/entry.txt. The line confesses the dumbest
thing my agent did today: it backed up a database onto the same
drive, deleted the original to save space, then backed up the
resulting empty folder twice more in the name of redundancy.
"""

import os

ENTRY = (
    "My agent copied my database onto the very same disk, erased the "
    "original to free up space, then copied the now-empty folder two "
    "more times and proudly called the emptiness redundancy."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
