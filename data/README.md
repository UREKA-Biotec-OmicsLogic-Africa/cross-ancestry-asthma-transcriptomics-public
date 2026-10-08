# Data Directory

This directory separates source references, controlled manifests, processed analysis inputs, platform annotation, and curated gene sets.

## Rules

- Do not commit participant-identifiable data.
- Do not redistribute third-party files without confirming their terms.
- Prefer programmatic download of public GEO files.
- Record every stable file in `data/manifests/file_manifest.tsv`.
- Generate SHA-256 checksums for publication-release files.
- Keep raw downloads out of Git unless there is a clear reproducibility need.

## Subdirectories

- `manifests/`: sample, file, and checksum records.
- `raw/`: local GEO downloads; ignored by Git.
- `annotation/`: documented GPL570 annotation subset and mapping audits.
- `processed/`: analysis-ready expression and metadata files.
- `gene_sets/`: curated pathway definitions and provenance.
