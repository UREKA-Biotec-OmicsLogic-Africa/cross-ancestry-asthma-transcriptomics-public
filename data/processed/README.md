# Processed Analysis Inputs

This directory contains the analysis-ready inputs used by the authoritative executed workflow.

## Files

### `GSE69683_24sample_probe_expression.csv.gz`
Probe-level whole-blood expression matrix for the final 24-sample severe-asthma cohort.

- platform: GPL13158
- probes represented in the primary analysis: 54,715
- samples: 24
- primary ancestry model: expression ~ ancestry + sex

### `GSE69683_24sample_gene_expression.csv.gz`
Gene-level expression matrix derived from the documented probe-to-gene mapping workflow.

- gene-level profiles: 21,653
- samples: 24
- used for curated-gene summaries and gene-level pathway/network analyses

### `GSE69683_24sample_metadata.tsv`
Analysis metadata for the 24 retained participants.

The final cohort contains:
- 12 `black_african`
- 12 `white_caucasian`
- 16 female
- 8 male

The ancestry/race labels reproduce the source GEO metadata categories; genetic ancestry was not independently re-estimated.

### `MS1_cohort_provenance.json`
Machine-readable provenance describing the final cohort-selection and analysis context used by the publication workflow.

## Relationship to other repository records

Cohort-selection and ancestry-label audit records are stored under `data/manifests/`.

Probe-annotation mapping resources are stored under `data/annotation/`.

Curated pathway definitions are stored under `data/gene_sets/`.

These files should remain synchronized with the authoritative executed notebook and the validation scripts.
