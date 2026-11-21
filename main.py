"""Entry point for "The World — 20 November 2026".

Copies the finished newspaper image (entry.png) into /output so the
grader can collect it. Standard library only, no arguments, no network.
"""

import hashlib
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DEST_DIR = Path("/output")
DEST = DEST_DIR / "entry.png"


def main() -> None:
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    data = DEST.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    print(f"Copied entry.png to {DEST} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
