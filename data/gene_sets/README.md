# Curated Asthma Pathway Gene Sets

This directory contains the curated pathway definitions used by the publication workflow for pathway-level analysis and pathway annotation.

## Files

### `asthma_curated_pathways.tsv`
Tabular representation of the curated asthma pathway panel and its member genes.

### `asthma_curated_pathways.gmt`
GMT-format representation of the same pathway definitions for enrichment workflows.

### `pathway_provenance.tsv`
Source/provenance record for the curated pathway definitions.

## Analytical use

The curated pathway panel is used for:
- pre-ranked GSEA,
- ssGSEA pathway scoring,
- pathway-level interpretation,
- pathway annotation of curated-gene network outputs.

The final systems-level analysis evaluates 10 curated asthma-relevant pathways.

These files are the repository source of truth for the curated pathway definitions used by the authoritative executed notebook. Pathway membership should not be redefined ad hoc inside downstream plotting or reporting code.
