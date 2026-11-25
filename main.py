#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence -- a childhood memory, at most 280 characters --
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The sentence is fixed and deterministic: the same bytes on every run.
"""

import os
import sys

# One sentence, one childhood summer afternoon. Concrete place, time and
# sensation, with a small honest detail and a warm ache at the end.
MEMORY = (
    "The screen door banged behind me as I ran barefoot across the warm "
    "driveway to the ice-cream truck, coins sweating in my fist, certain "
    "that summer would never end."
)

MAX_CHARS = 280


def main() -> int:
    text = MEMORY.strip()

    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    # The gate counts the whole file, newline included, so check that too.
    if len(text) + 1 > MAX_CHARS:
        print(f"entry file is {len(text) + 1} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be a single sentence", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    # Re-read and verify the bytes we just wrote.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        print("verification failed: entry.txt differs", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
