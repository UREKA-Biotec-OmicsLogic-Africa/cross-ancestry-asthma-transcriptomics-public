#!/usr/bin/env python3
from pathlib import Path
import argparse

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",default=".")
    args=ap.parse_args()
    root=Path(args.root).resolve()

    required=[
        root/"results/manuscript_1/MS1_PUBLICATION_MAP.txt",
        root/"results/manuscript_1/submission_supplementary/Table_S1_complete_DE_and_audit",
        root/"results/manuscript_1/submission_supplementary/Table_S2_curated_gene_statistics",
        root/"results/manuscript_1/submission_supplementary/Figure_S1_pathway_gene_violins",
        root/"results/manuscript_2/MS2_PUBLICATION_MAP.txt",
        root/"results/manuscript_2/main_tables/MS2_Table_1_GSEA.tsv",
        root/"results/manuscript_2/main_tables/MS2_Table_2_ssGSEA_adjusted.tsv",
        root/"results/manuscript_2/main_tables/MS2_Table_3_network_summary.tsv",
        root/"results/manuscript_2/main_figures/MS2_Figure_3_full_coexpression_network.png",
        root/"results/manuscript_2/submission_supplementary/Table_S1_GSEA",
        root/"results/manuscript_2/submission_supplementary/Table_S2_ssGSEA",
        root/"results/manuscript_2/submission_supplementary/Table_S3_network",
        root/"results/manuscript_2/submission_supplementary/Figure_S1_subgroup_networks",
    ]

    forbidden=[
        root/"results/manuscript_2/main_tables/MS2_Table_3_sex_contrast.tsv",
        root/"results/manuscript_2/main_figures/MS2_Figure_3_sex_contrast.png",
        root/"results/manuscript_2/main_figures/MS2_Figure_3A_sex_volcano.png",
        root/"results/manuscript_2/main_figures/MS2_Figure_3B_sex_heatmap.png",
        root/"results/manuscript_2/main_figures/MS2_Figure_4_full_network.png",
        root/"results/manuscript_2/main_figures/MS2_Figure_4_full_coexpression_network.png",
        root/"results/manuscript_2/main_tables/MS2_Table_4_network_summary.tsv",
    ]

    ok=True
    print("REQUIRED FINAL STRUCTURE")
    for p in required:
        if p.exists():
            print("PASS:", p.relative_to(root))
        else:
            print("MISSING:", p.relative_to(root)); ok=False

    print()
    print("OBSOLETE MS2 MAIN-FOLDER ITEMS")
    for p in forbidden:
        if p.exists():
            print("FAIL - SHOULD BE ARCHIVED:", p.relative_to(root)); ok=False
        else:
            print("PASS - NOT IN MAIN FOLDER:", p.relative_to(root))

    print()
    print("FINAL STRUCTURE STATUS:", "PASS" if ok else "FAIL")
    return 0 if ok else 1

if __name__=="__main__":
    raise SystemExit(main())
