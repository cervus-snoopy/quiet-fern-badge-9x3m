#!/usr/bin/env python3
"""Entry for make.fun "Make the AI Judge Laugh: The Office Joke Open".

Writes a single line of office comedy to entry.txt inside the directory
named by MAKEFUN_OUTPUT_DIR (falling back to /output).
"""

import os

JOKE = (
    "The office plant survived five layoffs and three CEOs, "
    "so HR gave it a badge, a parking space, and a performance review."
)


def main():
    if not (1 <= len(JOKE) <= 200):
        raise ValueError("joke must be 1-200 characters, got %d" % len(JOKE))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
