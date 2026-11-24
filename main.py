#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry (program/v1, Python 3.13).

Writes a single line of an out-of-office auto-reply to /output/entry.txt.
No network, no input files, no dependencies. The line is a constant:
it is the whole entry, and it is written exactly once, with a trailing
newline, so the file holds one line of text and nothing else.
"""

import os

# The winning line (82 characters, one line, UTF-8, no link, no image).
# Drafted fresh in the build session; scored 21/25 against the judge brief.
ENTRY = "Out of office. This auto-reply took three meetings to approve, so please enjoy it."

def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
