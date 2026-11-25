"""The Funniest One-Line Resignation Letter.

A one-line resignation letter written by a cron job that has run
every minute since March, addressed to a tired engineering manager.
Writes the line to entry.txt in the output directory.
"""

import os

LINE = "I resign. I've run every minute since March, and the only human who ever looked at me was grep."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
