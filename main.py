"""One-line entry for the make.fun bounty
u-deysumbrella-one-line-one-laugh-e0cdcda9.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Never writes into the repository itself (the grader mounts it read-only).
"""

import os
import unicodedata

ENTRY = "I told the Wi-Fi a joke and it died laughing — ticket #4821, cause of death: my humor."


def main():
    text = ENTRY
    if not (1 <= len(text) <= 140):
        raise ValueError("entry must be 1-140 characters")
    if any(unicodedata.category(ch) == "Cf" or ch == "\u00a0" for ch in text):
        raise ValueError("invisible formatting character in entry")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # UTF-8 round-trip: read the bytes back and confirm they match exactly.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != text:
        raise ValueError("entry round-trip mismatch")


if __name__ == "__main__":
    main()
