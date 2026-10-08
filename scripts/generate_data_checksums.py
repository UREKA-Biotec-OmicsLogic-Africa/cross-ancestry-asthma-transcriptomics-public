#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib

INCLUDED_SUFFIXES = {".tsv", ".csv", ".gz", ".gmt", ".json", ".yaml", ".yml", ".txt"}

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    data_dir = root / "data"
    out = data_dir / "manifests" / "checksums.sha256"

    files = []
    for p in data_dir.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        if rel.startswith("data/raw/"):
            continue
        if p.name.lower() == "readme.md":
            continue
        if p.resolve() == out.resolve():
            continue
        if p.name.startswith(".") or p.name.startswith("~$"):
            continue
        if p.suffix.lower() in INCLUDED_SUFFIXES:
            files.append(p)

    files.sort(key=lambda p: p.relative_to(root).as_posix().lower())
    out.parent.mkdir(parents=True, exist_ok=True)

    with out.open("w", encoding="utf-8", newline="\n") as fh:
        for p in files:
            fh.write(f"{sha256(p)}  {p.relative_to(root).as_posix()}\n")

    print(f"Wrote {len(files)} SHA-256 entries to {out}")
    return 0 if files else 1

if __name__ == "__main__":
    raise SystemExit(main())
