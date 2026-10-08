#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, csv, hashlib, shutil, sys

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def find_repo_root(explicit_root):
    root = Path(explicit_root).expanduser().resolve() if explicit_root else Path(__file__).resolve().parents[1]
    required = [root / "results" / "manuscript_1", root / "results" / "manuscript_2"]
    missing = [p for p in required if not p.exists()]
    if missing:
        print("ERROR: repository root could not be validated.")
        print("Resolved root:", root)
        for p in missing:
            print("MISSING:", p)
        sys.exit(2)
    return root

def copy_verified(src: Path, dst: Path, overwrite: bool):
    if not src.exists():
        return ("MISSING SOURCE", "")
    dst.parent.mkdir(parents=True, exist_ok=True)
    src_hash = sha256(src)
    if dst.exists():
        dst_hash = sha256(dst)
        if dst_hash == src_hash:
            return ("ALREADY PRESENT / VERIFIED", src_hash)
        if not overwrite:
            return ("CONFLICT - USE --overwrite AFTER REVIEW", src_hash)
    shutil.copyfile(src, dst)
    if not dst.exists():
        return ("COPY FAILED", src_hash)
    if sha256(dst) != src_hash:
        return ("COPY FAILED - HASH MISMATCH", src_hash)
    return ("COPIED AND SHA-256 VERIFIED", src_hash)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()
    root = find_repo_root(args.root)

    ms1 = root / "results" / "manuscript_1"
    ms2 = root / "results" / "manuscript_2"
    s2 = ms1 / "supplementary" / "S2_pathway_and_enrichment"
    s4 = ms1 / "supplementary" / "S4_coexpression_networks"
    figs = ms1 / "main_figures"

    mappings = [
        (s2/"MS1_S2A_GSEA_ancestry_adjusted.tsv",
         ms2/"main_tables"/"MS2_Table_1_GSEA.tsv",
         "Main Table 1: GSEA"),
        (s2/"MS1_S2C_ssGSEA_ancestry_adjusted_OLS.tsv",
         ms2/"main_tables"/"MS2_Table_2_ssGSEA_adjusted.tsv",
         "Main Table 2: adjusted ssGSEA"),
        (s4/"MS1_S4_network_summary.tsv",
         ms2/"main_tables"/"MS2_Table_3_network_summary.tsv",
         "Main Table 3: network summary"),
        (figs/"11_gsea_lollipop_ancestry.png",
         ms2/"main_figures"/"MS2_Figure_1A_GSEA_lollipop.png",
         "Figure 1A: GSEA lollipop"),
        (figs/"12_gsea_significance_ancestry.png",
         ms2/"main_figures"/"MS2_Figure_1B_GSEA_significance.png",
         "Figure 1B: GSEA significance"),
        (figs/"13_ssgsea_pathway_scores.png",
         ms2/"main_figures"/"MS2_Figure_2A_ssGSEA_scores.png",
         "Figure 2A: ssGSEA scores"),
        (figs/"14_volcano_ssgsea_pathways.png",
         ms2/"main_figures"/"MS2_Figure_2B_ssGSEA_volcano.png",
         "Figure 2B: adjusted ssGSEA volcano"),
        (s4/"MS1_S4_all_samples_network.png",
         ms2/"main_figures"/"MS2_Figure_3_full_coexpression_network.png",
         "Figure 3: full-cohort network"),
        (s2/"MS1_S2B_ssGSEA_scores.tsv",
         ms2/"submission_supplementary"/"Table_S2_ssGSEA"/"MS2_Table_S2_ssGSEA_scores.tsv",
         "Supplementary Table S2: ssGSEA score matrix"),
        (s2/"MS1_S2D_ssGSEA_ancestry_wilcoxon.tsv",
         ms2/"submission_supplementary"/"Table_S2_ssGSEA"/"MS2_Table_S2b_ssGSEA_Wilcoxon.tsv",
         "Supplementary Table S2: Wilcoxon sensitivity"),
        (s4/"MS1_S4_all_samples_edges.tsv",
         ms2/"submission_supplementary"/"Table_S3_network"/"MS2_Table_S3_all_samples_edges.tsv",
         "Supplementary Table S3: all-samples edges"),
        (s4/"MS1_S4_all_samples_nodes.tsv",
         ms2/"submission_supplementary"/"Table_S3_network"/"MS2_Table_S3_all_samples_nodes.tsv",
         "Supplementary Table S3: all-samples node centrality"),
    ]

    print("Repository root:", root)
    print()
    rows = []
    counts = {"copied":0,"verified":0,"missing":0,"conflict":0,"failed":0}

    for i,(src,dst,role) in enumerate(mappings,1):
        status,digest = copy_verified(src,dst,args.overwrite)
        print(f"[{i:02d}/{len(mappings):02d}] {role}")
        print("  SOURCE:      ", src)
        print("  DESTINATION: ", dst)
        print("  STATUS:      ", status)
        print()
        if status.startswith("COPIED"):
            counts["copied"] += 1
        elif status.startswith("ALREADY"):
            counts["verified"] += 1
        elif status.startswith("MISSING"):
            counts["missing"] += 1
        elif status.startswith("CONFLICT"):
            counts["conflict"] += 1
        else:
            counts["failed"] += 1
        rows.append({
            "role":role,
            "source": src.relative_to(root).as_posix() if src.exists() else str(src),
            "destination": dst.relative_to(root).as_posix(),
            "status":status,
            "sha256":digest
        })

    manifest = ms2/"MANIFEST.tsv"
    manifest.parent.mkdir(parents=True,exist_ok=True)
    with manifest.open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=["role","source","destination","status","sha256"],delimiter="\t")
        w.writeheader(); w.writerows(rows)

    print("="*78)
    print("FINAL DE-OVERLAPPED ALLOCATION SUMMARY")
    print("Copied and verified:      ", counts["copied"])
    print("Already present/verified: ", counts["verified"])
    print("Missing sources:          ", counts["missing"])
    print("Conflicting destinations: ", counts["conflict"])
    print("Copy/read failures:       ", counts["failed"])
    print("Manifest:                 ", manifest)
    bad=counts["missing"]+counts["conflict"]+counts["failed"]
    if bad==0:
        print()
        print("STATUS: SUCCESS - final MS2 pathway/network allocation is checksum-verified.")
        print("NOTE: reciprocal sex-contrast outputs were intentionally NOT allocated to MS2.")
        return 0
    print()
    print("STATUS: ATTENTION REQUIRED - review the items above.")
    return 1

if __name__=="__main__":
    raise SystemExit(main())
