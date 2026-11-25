#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — one-line entry.

Writes a single joke (one line, <=200 chars) about a meeting that
should have been an email to entry.txt.
"""

import os

ENTRY = "The agenda had one item: 'discuss the email.' Forty-five minutes later, nobody had read the email."


def main():
    # Self-gate mirroring the sealed scorer: UTF-8 text, 1-200 chars,
    # single line, not only whitespace.
    text = ENTRY
    assert 1 <= len(text) <= 200, f"gate: {len(text)} chars, need 1-200"
    assert "\n" not in text and "\r" not in text, "gate: must be one line"
    assert text.strip(), "gate: must not be blank"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"chars: {len(ENTRY)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    main()
