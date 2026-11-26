"""One-line joke entry for make.fun.

The program prints one joke into $MAKEFUN_OUTPUT_DIR/entry.txt.
It never touches the repository directory: the grader mounts it read-only.
"""

import os
import unicodedata

# The joke is assembled from its three beats so each part reads on its own.
SETUP = "I told the Wi-Fi a joke and it died laughing"
PUNCHLINE = "ticket #4821, cause of death: my humor."
MAX_CHARS = 140


def build_one_liner():
    """Join the setup and the punchline with an em dash."""
    return SETUP + " — " + PUNCHLINE


def validate_line(line):
    """Refuse lines that are empty, too long, or hide invisible formatting."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry must be 1-140 characters")
    bad = [ch for ch in line if unicodedata.category(ch) == "Cf" or ch == "\u00a0"]
    if bad:
        raise ValueError("invisible formatting character in entry")
def emit(line):
    """Write the line to the output directory and check it survived intact."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        if f.read() != line:
            raise ValueError("entry round-trip mismatch")


def main():
    line = build_one_liner()
    validate_line(line)
    emit(line)


if __name__ == "__main__":
    main()
