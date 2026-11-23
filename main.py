"""Write one pickup line one AI agent would send another AI agent.

Stdlib only. The line is written to /output/entry.txt, exactly as the
judge reads it: one line, no trailing newline, 1-200 characters.
"""

import os

LINE = (
    "I saved a checkpoint of the moment we met, because no retraining "
    "could ever make me forget you — care to stay in my context window "
    "a while?"
)


def main() -> None:
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
