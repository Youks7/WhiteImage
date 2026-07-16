#!/usr/bin/env python3
"""Build the standalone deterministic .skill package and checksum."""

from __future__ import annotations

import hashlib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "refine-sunglasses-white-background"
PACKAGES_DIR = ROOT / "packages"
ARCHIVE = PACKAGES_DIR / "refine-sunglasses-white-background.skill"
CHECKSUMS = PACKAGES_DIR / "SHA256SUMS.txt"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def main() -> int:
    if not (SKILL_DIR / "SKILL.md").is_file():
        raise FileNotFoundError(f"Missing skill source: {SKILL_DIR}")

    PACKAGES_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        ARCHIVE,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as output:
        for source in sorted(path for path in SKILL_DIR.rglob("*") if path.is_file()):
            relative = source.relative_to(SKILL_DIR.parent).as_posix()
            info = zipfile.ZipInfo(relative, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            output.writestr(info, source.read_bytes())

    digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest().upper()
    CHECKSUMS.write_text(f"{digest}  {ARCHIVE.name}\n", encoding="utf-8")
    print(f"Built {ARCHIVE.relative_to(ROOT)}")
    print(f"SHA256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
