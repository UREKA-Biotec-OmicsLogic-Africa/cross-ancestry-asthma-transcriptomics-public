#!/usr/bin/env python3
"""Windows-safe allocator for MS1 -> MS2 publication outputs.

This version avoids both:
- shutil.copy2 / Windows CopyFile2
- temporary-file + atomic-replace logic

It uses direct streamed binary copying with SHA-256 verification.

Place this file in:
    <repo>/scripts/allocate_publication_outputs_v3_windows_safe.py

Run from anywhere:
    python scripts\allocate_publication_outputs_v3_windows_safe.py --overwrite
"""

from __future__ import annotations

from pathlib import Path
import argparse
import csv
import hashlib
import os
import sys

MS2_MAP = {
    "results/manuscript_1/supplementary/S2_pathway_and_enrichment/MS1_S2A_GSEA_ancestry_adjusted.tsv":
        "results/manuscript_2/main_tables/MS2_Table_1_GSEA.tsv",
    "results/manuscript_1/supplementary/S2_pathway_and_enrichment/MS1_S2B_ssGSEA_scores.tsv":
        "results/manuscript_2/supplementary/MS2_Table_S2_ssGSEA_scores.tsv",
    "results/manuscript_1/supplementary/S2_pathway_and_enrichment/MS1_S2C_ssGSEA_ancestry_adjusted_OLS.tsv":
        "results/manuscript_2/main_tables/MS2_Table_2_ssGSEA_adjusted.tsv",
    "results/manuscript_1/supplementary/S2_pathway_and_enrichment/MS1_S2D_ssGSEA_ancestry_wilcoxon.tsv":
        "results/manuscript_2/supplementary/MS2_Table_S2b_ssGSEA_Wilcoxon.tsv",
    "results/manuscript_1/main_figures/11_gsea_lollipop_ancestry.png":
        "results/manuscript_2/main_figures/MS2_Figure_1A_GSEA_lollipop.png",
    "results/manuscript_1/main_figures/12_gsea_significance_ancestry.png":
        "results/manuscript_2/main_figures/MS2_Figure_1B_GSEA_significance.png",
    "results/manuscript_1/main_figures/13_ssgsea_pathway_scores.png":
        "results/manuscript_2/main_figures/MS2_Figure_2A_ssGSEA_scores.png",
    "results/manuscript_1/main_figures/14_volcano_ssgsea_pathways.png":
        "results/manuscript_2/main_figures/MS2_Figure_2B_ssGSEA_volcano.png",
    "results/manuscript_1/main_figures/08_volcano_plot_sex_annotated.png":
        "results/manuscript_2/main_figures/MS2_Figure_3A_sex_volcano.png",
    "results/manuscript_1/main_figures/09_heatmap_top_de_sex.png":
        "results/manuscript_2/main_figures/MS2_Figure_3B_sex_heatmap.png",
    "results/manuscript_1/supplementary/S4_coexpression_networks/MS1_S4_all_samples_network.png":
        "results/manuscript_2/main_figures/MS2_Figure_4_full_network.png",
    "results/manuscript_1/supplementary/S4_coexpression_networks/MS1_S4_network_summary.tsv":
        "results/manuscript_2/main_tables/MS2_Table_4_network_summary.tsv",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(1024 * 1024)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def copy_direct_verified(src: Path, dst: Path) -> None:
    """Copy bytes directly to destination and verify SHA-256."""
    dst.parent.mkdir(parents=True, exist_ok=True)

    # Preflight: confirm parent exists and is writable.
    if not dst.parent.exists():
        raise FileNotFoundError(f"Destination parent could not be created: {dst.parent}")

    probe = dst.parent / ".__write_test__.tmp"
    try:
        with probe.open("wb") as handle:
            handle.write(b"ok")
    finally:
        if probe.exists():
            probe.unlink()

    # Direct binary copy. No CopyFile2 and no temporary destination.
    with src.open("rb") as source, dst.open("wb") as target:
        while True:
            block = source.read(1024 * 1024)
            if not block:
                break
            target.write(block)
        target.flush()
        os.fsync(target.fileno())

    if not dst.exists():
        raise FileNotFoundError(f"Destination was not created: {dst}")

    src_hash = sha256(src)
    dst_hash = sha256(dst)
    if src_hash != dst_hash:
        raise IOError(
            f"SHA-256 mismatch after copy:\n"
            f"  source:      {src_hash}\n"
            f"  destination: {dst_hash}"
        )


def detect_repo_root() -> Path:
    script = Path(__file__).resolve()
    candidate = script.parent.parent
    if (candidate / "results").is_dir() and (candidate / "scripts").is_dir():
        return candidate
    current = Path.cwd().resolve()
    if (current / "results").is_dir() and (current / "scripts").is_dir():
        return current
    raise FileNotFoundError(
        "Repository root could not be detected. "
        "Place this script inside <repo>/scripts/ or run it from the repo root."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default=None,
        help="Optional repository root. Normally unnecessary.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite mapped MS2 derivative files if they already exist and differ.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else detect_repo_root()
    print(f"Repository root: {root}")
    print()

    if not (root / "results" / "manuscript_1").is_dir():
        print("ERROR: results/manuscript_1 is missing.")
        return 2

    # Preflight all destination directories before any copying.
    destination_dirs = sorted({
        (root / dst_rel).parent for dst_rel in MS2_MAP.values()
    })
    print("Preflight destination directories:")
    for directory in destination_dirs:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"  OK: {directory}")
    print()

    rows = []
    copied = 0
    verified_existing = 0
    missing = []
    conflicts = []
    failures = []

    for i, (src_rel, dst_rel) in enumerate(MS2_MAP.items(), 1):
        src = root / src_rel
        dst = root / dst_rel

        print(f"[{i:02d}/{len(MS2_MAP):02d}]")
        print(f"  SOURCE:      {src}")
        print(f"  DESTINATION: {dst}")

        if not src.is_file():
            print("  STATUS: MISSING SOURCE")
            missing.append(src_rel)
            print()
            continue

        try:
            # Confirm source is actually readable.
            with src.open("rb") as handle:
                handle.read(1)
        except Exception as exc:
            print(f"  STATUS: SOURCE NOT READABLE - {type(exc).__name__}: {exc}")
            failures.append((src_rel, str(exc)))
            print()
            continue

        src_hash = sha256(src)

        if dst.exists():
            if not dst.is_file():
                print("  STATUS: CONFLICT - destination exists but is not a file")
                conflicts.append(dst_rel)
                print()
                continue

            dst_hash = sha256(dst)
            if src_hash == dst_hash:
                print("  STATUS: EXISTS AND VERIFIED (identical)")
                verified_existing += 1
                rows.append({
                    "source": src_rel,
                    "destination": dst_rel,
                    "sha256": dst_hash,
                    "size_bytes": dst.stat().st_size,
                    "status": "verified_existing",
                })
                print()
                continue

            if not args.overwrite:
                print("  STATUS: EXISTS BUT DIFFERS - skipped")
                conflicts.append(dst_rel)
                print()
                continue

        try:
            copy_direct_verified(src, dst)
        except Exception as exc:
            print(f"  STATUS: COPY FAILED - {type(exc).__name__}: {exc}")
            failures.append((src_rel, str(exc)))
            print()
            continue

        copied += 1
        dst_hash = sha256(dst)
        print("  STATUS: COPIED AND SHA-256 VERIFIED")
        rows.append({
            "source": src_rel,
            "destination": dst_rel,
            "sha256": dst_hash,
            "size_bytes": dst.stat().st_size,
            "status": "copied",
        })
        print()

    manifest = root / "results" / "manuscript_2" / "MANIFEST.tsv"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["source", "destination", "sha256", "size_bytes", "status"],
            delimiter="\t",
        )
        writer.writeheader()
        writer.writerows(rows)

    print("=" * 78)
    print("ALLOCATION SUMMARY")
    print(f"Copied and verified:       {copied}")
    print(f"Already present/verified:  {verified_existing}")
    print(f"Missing sources:           {len(missing)}")
    print(f"Conflicting destinations:  {len(conflicts)}")
    print(f"Copy/read failures:        {len(failures)}")
    print(f"Manifest:                  {manifest}")

    if missing:
        print("\nMissing source files:")
        for item in missing:
            print(f"  - {item}")

    if conflicts:
        print("\nConflicting destination files:")
        for item in conflicts:
            print(f"  - {item}")

    if failures:
        print("\nCopy/read failures:")
        for item, error in failures:
            print(f"  - {item}")
            print(f"    {error}")

    if missing or conflicts or failures:
        print("\nSTATUS: REVIEW REQUIRED - do not make the Phase D commit yet.")
        return 1

    print("\nSTATUS: SUCCESS - all 12 mapped files are present and checksum-verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
