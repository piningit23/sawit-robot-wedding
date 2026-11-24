#!/usr/bin/env python3
"""One-line robot wedding vow.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

VOW = "I promise to love you in sickness and in health, through every firmware update, in Wi-Fi and in airplane mode, till low battery do us part."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
