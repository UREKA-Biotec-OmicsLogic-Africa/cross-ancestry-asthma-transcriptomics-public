# Probe Annotation and Mapping Audit

This directory contains the documented annotation resources used to translate microarray probe identifiers into gene-level labels for downstream reporting and analysis.

## Important platform distinction

The expression dataset was generated on **GPL13158 (Affymetrix HT HG-U133+ PM Array Plate)**.

The file named `GPL570_annotation_subset.tsv.gz` is retained as an **annotation cross-mapping resource only**, where compatible probe identifiers could be mapped. It should not be interpreted as the assay platform for GSE69683.

The primary analytical unit remains the GPL13158 probe-level expression matrix.

## Files

### `GPL570_annotation_subset.tsv.gz`
Documented GPL570-derived annotation subset used for compatible probe-to-gene cross-mapping.

### `ambiguous_probe_mappings.tsv`
Audit table of probe identifiers for which mapping was not unambiguous, including multi-gene or otherwise non-unique mappings where applicable.

### `unmapped_probes.tsv`
Audit table of probe identifiers for which no accepted gene mapping was retained.

## Mapping policy used in the analysis

Probe identifiers were normalized for mapping by removing the `_PM_` component where required by the documented workflow.

Mappings were classified as:
- unambiguous,
- ambiguous, or
- unmapped.

Probe-level differential expression is the primary analysis. For gene-labelled displays, the representative probe is the probe with the smallest ancestry FDR among accepted mappings. For curated-gene and gene-level analyses, unambiguous probes mapping to the same gene are summarized according to the executed workflow.

The resulting gene-level matrix contains 21,653 profiles.
