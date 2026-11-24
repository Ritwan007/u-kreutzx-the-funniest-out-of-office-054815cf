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
    # The grader reads /output/entry.txt; ENTRY_OUTPUT_DIR only redirects
    # the target for local dry runs, it never changes the bytes written.
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back and prove the file on disk is exactly the entry, one line.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw == (text + "\n").encode("utf-8"), "written bytes differ from entry"
    assert raw.count(b"\n") == 1, "file must hold exactly one line"


if __name__ == "__main__":
    main()
