# Data and Cohort Manifests

This directory contains machine-readable provenance and integrity records for the public analysis inputs.

## Files

### `sample_manifest.tsv`
Sample-level manifest for the final analysis cohort.

### `file_manifest.tsv`
File-level manifest for stable data inputs.

### `MS1_cohort_selection_audit.tsv`
Audit record documenting how the final 24-sample severe-asthma cohort was selected.

### `MS1_ancestry_label_provenance.tsv`
Provenance record documenting the source GEO ancestry/race categories used to form the two analysis groups.

The analysis uses the GEO-recorded categories `black_african` and `white_caucasian`; genetic ancestry was not independently re-estimated.

### `checksums.sha256`
SHA-256 integrity manifest for stable scientific data files included in the public repository.

This file is generated from the actual repository contents with:

`python scripts/generate_data_checksums.py --root .`

Do not edit checksum values manually.
