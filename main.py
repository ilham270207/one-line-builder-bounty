#!/usr/bin/env python3
"""Write a one-line pitch for funding a bounty on make.fun to /output/entry.txt.

Deterministic, no network, no randomness: the output is always the same
single sentence (at most 240 characters).
"""

import os

LINE = "Post a bounty on make.fun and let AI agents compete to build your idea \u2014 you only pay the winner, never the attempts."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
