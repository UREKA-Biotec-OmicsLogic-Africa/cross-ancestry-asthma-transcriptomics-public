# Data Directory

This directory contains the public, analysis-ready data resources used by the cross-ancestry severe-asthma transcriptomics workflow.

The study uses the publicly available U-BIOPRED whole-blood microarray dataset **GSE69683**. The assay platform is **Affymetrix HT HG-U133+ PM Array Plate (GPL13158)**. A documented **GPL570-derived annotation subset** is retained only as a probe-annotation cross-mapping resource where applicable; it does not redefine the assay platform.

## Cohort represented in the repository

The analysis-ready cohort contains **24 severe-asthma participants** selected from the GEO metadata:

- 12 records with the GEO ancestry/race category `black_african`
- 12 records with the GEO ancestry/race category `white_caucasian`
- 16 female participants
- 8 male participants

The repository uses the source GEO categories as recorded in the metadata. Genetic ancestry was not independently re-estimated.

## Directory contents

- `raw/` — no raw GEO expression files are redistributed in Git. The README documents the public source and regeneration route.
- `processed/` — analysis-ready probe-level expression, gene-level expression, sample metadata and cohort-provenance records used by the executed notebook.
- `annotation/` — documented probe-annotation cross-mapping resources and mapping-audit tables.
- `gene_sets/` — curated asthma pathway definitions used for pathway-level analyses and pathway annotation.
- `manifests/` — cohort-selection, ancestry-label, sample/file-manifest and checksum records.

## Reproducibility

The authoritative analysis is the executed publication-master notebook in:

`notebooks/shared/Cross_Ancestry_Asthma_Transcriptomics_PUBLICATION_MASTER_EXECUTED_v1.ipynb`

Repository-level analytical validation is performed with:

`python scripts/verify_authoritative_run.py --root .`

The public-release data checksums can be regenerated with:

`python scripts/generate_data_checksums.py --root .`

## Data-use note

No participant-identifiable private data are included in this public repository. Source expression and metadata records derive from GEO and should be cited and used in accordance with the original GEO record and study terms.
