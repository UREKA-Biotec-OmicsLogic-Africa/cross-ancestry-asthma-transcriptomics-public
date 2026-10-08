# Data Dictionary

Document every field in the sample manifest, expression matrices, annotation tables, differential-expression outputs, pathway outputs, and network files.

Recommended columns:

| Field | File | Type | Allowed values | Description | Source |
|---|---|---|---|---|---|
| sample_id | sample manifest | string | unique | Internal sample identifier | GEO metadata |
| geo_accession | sample manifest | string | GSM accession | GEO sample accession | GEO |
| ancestry_label | sample manifest | category | African, European | Analysis ancestry grouping | documented source field |
| gender | sample manifest | category | female, male | Reported metadata field | GEO |
| probe_id | expression/DE | string | GPL570 probe set | Platform probe identifier | GPL570 |
| gene_symbol | annotation | string | approved symbol or mapping text | Probe-to-gene mapping | GPL570 annotation |

Expand this table when the final files are available.
