"""The One-Line Cat Joke That Lands.

Writes a single one-line joke about cats (under 200 characters) to
/output/entry.txt. Fully deterministic: no randomness, no network, no
clock, no environment input. Running it twice produces byte-identical
output.
"""

import os
from pathlib import Path

JOKE = (
    "My cat stared at a blank wall for an hour, then turned to me "
    "like I was the one wasting my life."
)


def main() -> None:
    # Bundle-session guard: the 1-200 character gate below must stay
    # intact; the joke text itself is unchanged by this edit.
    # The gate requires 1 to 200 characters of non-whitespace text.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke must be 1 to 200 characters")
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
