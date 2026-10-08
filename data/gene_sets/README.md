# Curated Asthma Gene Sets

This directory is the single source of truth for all curated pathway definitions.

Expected files:

- `asthma_curated_pathways.tsv`
- `asthma_curated_pathways.gmt`
- `pathway_provenance.tsv`

Do not redefine pathways inside notebooks. Load them from these files.

Each pathway must have:

- a stable pathway name;
- a defined gene-symbol namespace;
- a complete gene list;
- literature or database provenance;
- curator and verification date;
- notes on inclusion and exclusion decisions.
