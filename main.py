"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes a single line (<=120 chars) to /output/entry.txt,
honouring MAKEFUN_OUTPUT_DIR when set. Stdlib only.
"""

import os

FORTUNE = (
    "A sunbeam will land on your favorite leaf, and your keeper "
    "will tell every guest you are the pride of the windowsill."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune is {len(text)} chars"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
