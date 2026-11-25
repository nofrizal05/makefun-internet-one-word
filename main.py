"""The Internet in One Word.

One word for the whole internet: Bottomless.
A bottomless pit of tabs, threads, videos and rabbit holes.
You can scroll forever and never reach the end of it.
"""

import os

WORD = "Bottomless"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
