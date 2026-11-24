#!/usr/bin/env python3
"""Vending-machine pickup line entry.

Writes exactly one pickup line, spoken by the machine itself, to
/output/entry.txt. No input, no network, no randomness: the same line
on every run.
"""

import os

LINE = "My screen says PLEASE MAKE A SELECTION - and I've already made mine. It's you."


def main() -> None:
    # Self-check the same gate the sealed scorer applies: UTF-8 text of
    # 1 to 200 characters, not only white space.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
