#!/usr/bin/env python3
"""Write the warning-label entry to /output/entry.txt."""

import os

ENTRY = "WARNING: This human will say \"I'm fine\" while visibly on fire. Do not take their word for it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
