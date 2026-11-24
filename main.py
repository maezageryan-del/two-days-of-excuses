#!/usr/bin/env python3
"""Two days of excuses entry for make.fun.

Writes one line, in the voice of an AI agent explaining a missed
deadline, to entry.txt. The agent ran its own eval on the deadline
itself, scored it 0 out of 10, and discarded it as low quality: total
confidence meeting total failure. One line, 90 characters, inside
the 200 cap.
"""

import os

ENTRY = "I ran my own eval on the deadline, scored it 0 out of 10, and discarded it as low quality."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
