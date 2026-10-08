# Raw Data Source

Raw GEO expression downloads are **not redistributed in this Git repository**.

The analysis is based on the public GEO series:

- **Series:** GSE69683
- **Study context:** U-BIOPRED severe-asthma whole-blood transcriptomics
- **Assay platform:** GPL13158 — Affymetrix HT HG-U133+ PM Array Plate

The public repository stores processed, analysis-ready derivatives and provenance records rather than duplicating the original raw GEO downloads.

## Reproduction route

To reconstruct the source-data stage:

1. Retrieve GSE69683 from NCBI GEO.
2. Confirm the sample identifiers against `data/manifests/sample_manifest.tsv`.
3. Confirm cohort-selection and ancestry-label decisions against:
   - `data/manifests/MS1_cohort_selection_audit.tsv`
   - `data/manifests/MS1_ancestry_label_provenance.tsv`
4. Run the documented processing workflow represented in the authoritative executed notebook.

The 24-sample analysis cohort contains 12 `black_african` and 12 `white_caucasian` GEO metadata records. Genetic ancestry was not independently re-estimated.

No private or participant-identifiable source data should be placed in this directory.
