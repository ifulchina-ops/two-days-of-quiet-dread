#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one single-line code review comment to /output/entry.txt: an
approval of a pull request carrying quiet existential dread. The comment
is fixed, so every run writes the exact same bytes (deterministic).
"""

import os

COMMENT = "Approved. The diff is clean, the tests are green, and this code will outlive everyone who reviewed it."

OUTPUT_PATH = "/output/entry.txt"

# The sealed gate: /output/entry.txt must hold 1 to 140 characters.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 140


def main() -> None:
    if not GATE_MIN_CHARS <= len(COMMENT) <= GATE_MAX_CHARS:
        raise SystemExit("comment outside the 1-140 character gate")
    if COMMENT != COMMENT.strip() or "\n" in COMMENT:
        raise SystemExit("comment must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(COMMENT)


if __name__ == "__main__":
    main()
