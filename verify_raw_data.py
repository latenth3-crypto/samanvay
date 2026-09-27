"""Check raw snapshot hashes from SOURCES.md, without modifying any files."""

import argparse
import hashlib
from pathlib import Path
import re
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--git-ref", help="Check stored Git blobs, e.g. HEAD, instead of local files")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    sources = (root / "SOURCES.md").read_text(encoding="utf-8")
    snapshots = re.findall(
        r"- \*\*Local Path:\*\* `([^`]+)`.*?"
        r"- \*\*SHA-256 Checksum:\*\* `([0-9a-f]{64})`", sources, re.S
    )
    if len(snapshots) != 3:
        raise SystemExit("Expected three documented raw snapshots in SOURCES.md")
    failures = 0
    for path, expected in snapshots:
        try:
            data = (subprocess.check_output(
                ["git", "cat-file", "blob", f"{args.git_ref}:{path}"], cwd=root
            ) if args.git_ref else (root / path).read_bytes())
            actual = hashlib.sha256(data).hexdigest()
            ok = actual == expected
            print(f"{'PASS' if ok else 'FAIL'} {path}: {actual}")
            if not ok:
                print(f"  expected: {expected}")
            failures += not ok
        except (OSError, subprocess.CalledProcessError) as exc:
            print(f"FAIL {path}: {exc}")
            failures += 1
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
