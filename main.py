#!/usr/bin/env python3
"""Entry program for Angry Judge: The Short Rant Contest.

Writes one short rant (at most 400 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt.
The target is the 'quick update': forty-five minutes, two
restarts, one moved button, and a request for a five-star
rating at the end of it.
"""

import os

RANT = (
    "A 'quick update' takes 45 minutes, restarts twice, "
    "moves the one button you'd finally memorized, changes "
    "nothing else, and then has the nerve to ask you to rate "
    "the experience. Five stars. It knows where I live."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
