"""Unsent: a micro-confession -- entry program.

Writes a To: line and one unsent message to OUTPUT_DIR/entry.txt.
Standard library only, no network, same bytes every run.
"""

import os

ENTRY = (
    "To: Dad\n"
    "fixed the gate latch you kept asking about. took eleven minutes. sorry it took me until after the funeral"
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    # Gate: 1 to 260 characters of UTF-8, not only white space.
    assert ENTRY.strip() and 1 <= len(ENTRY) <= 260
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
