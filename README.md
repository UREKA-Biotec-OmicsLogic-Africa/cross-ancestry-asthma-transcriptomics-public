# Cross-Ancestry Asthma Transcriptomics

**Public reproducibility repository | Severe-asthma whole-blood transcriptomics | GSE69683 (U-BIOPRED)**

This repository provides the publicly shareable computational workflow, documented provenance, processed public-data-derived materials, analysis outputs, and publication-facing result maps supporting two complementary scientific manuscripts investigating ancestry-associated transcriptomic variation in severe asthma.

The repository is maintained under **UREKA Biotec / OmicsLogic Africa**. It is separate from the private development repository containing manuscript drafts and internal editorial records.

## Project leadership and attribution

- **Project lead and developer:** [Dr. Adekunle Oluwatosin Adeluwoye](https://github.com/Tossman) (GitHub: [`@Tossman`](https://github.com/Tossman))
- **Institutional hosting:** [UREKA Biotec / OmicsLogic Africa](https://github.com/UREKA-Biotec-OmicsLogic-Africa)
- **Research role:** Project lead and Program Director, UREKA Biotec / OmicsLogic Africa

This project was led and its public reproducibility repository developed by Dr. Adeluwoye. Institutional hosting supports sustained visibility and research collaboration. Commit-level authorship and future collaborator contributions are recorded through individual Git identities.

## Project team contributions

In addition to project leadership, the following team members contributed to investigation, analysis, validation, and manuscript preparation:

- Watafua Miriam — investigation, data curation, lead execution of pipeline workflow, analysis, visualisation, writing  
- Katherine David — validation, literature curation, visualisation, writing  
- Lawal Jamiu — validation, reproducibility checks, writing  
- Ayanfeoluwa Alabetutu — methodology, software, validation, analysis, writing, supervision

## Dataset and analytical scope

| Characteristic | Documented analysis |
| --- | --- |
| Data source | GEO accession **GSE69683**, U-BIOPRED |
| Biological material | Whole blood |
| Study population | 24 severe-asthma participants |
| Recorded ancestry/race groups | 12 `black_african`; 12 `white_caucasian` |
| Sex distribution | 16 female; 8 male |
| Microarray platform | **GPL13158**, Affymetrix HT HG-U133+ PM Array Plate |
| Reported probe features | 54,715 |
| Gene-level expression profiles | 21,653 |
| Primary model | Expression ~ ancestry group + sex |

The ancestry/race group labels follow the source metadata; **genetic ancestry was not independently inferred**. Findings should be interpreted in the context of the small cohort, whole-blood sampling, and observational expression data.

## Complementary manuscript analyses

Both companion manuscripts derive from the same authoritative executed analysis but have deliberately distinct publication-facing scopes.

### Manuscript 1 — Gene-level differential expression

Manuscript 1 focuses on cohort characterisation and quality control, sample structure, sex-adjusted ancestry-associated differential expression, sensitivity analyses, probe-to-gene mapping, curated asthma-associated genes, and ACKR1/Duffy-related interpretation. A reciprocal sex contrast is retained as an internal validation analysis.

Publication-facing map: [`results/manuscript_1/MS1_PUBLICATION_MAP.txt`](results/manuscript_1/MS1_PUBLICATION_MAP.txt)

### Manuscript 2 — Pathways and co-expression networks

Manuscript 2 focuses on pre-ranked gene-set enrichment analysis (GSEA), single-sample GSEA (ssGSEA), pathway-level contrasts, curated-gene co-expression networks, and network centrality. Subgroup networks are reported descriptively, **not** as formal comparative network-topology tests.

Publication-facing map: [`results/manuscript_2/MS2_PUBLICATION_MAP.txt`](results/manuscript_2/MS2_PUBLICATION_MAP.txt)

Manuscript files, internal drafts, peer-review correspondence, and unpublished editorial documents are intentionally excluded from this public reproducibility repository. Publication and preprint links can be added after release.

## Authoritative analysis and provenance

The numerical reference for the companion manuscripts is the executed publication-master notebook:

[`notebooks/shared/Cross_Ancestry_Asthma_Transcriptomics_PUBLICATION_MASTER_EXECUTED_v1.ipynb`](notebooks/shared/Cross_Ancestry_Asthma_Transcriptomics_PUBLICATION_MASTER_EXECUTED_v1.ipynb)

Documented execution information:

- **Notebook SHA-256:** `568aed3e22b7baafcc1bd42f23157c145ac1f41ffb30402f52d182280896795f`
- **Execution start:** `2026-07-30T14:27:12+00:00`
- **Platform:** GPL13158
- **Generated files indexed by the authoritative-run verifier:** 72

The notebook and publication-output maps are the principal references for interpretation of the analysis outputs. External execution paths recorded in historical provenance should not be treated as prerequisites for accessing the public repository.

## Repository layout

```text
config/                Configuration resources
data/                  Data inputs and public-data-derived materials
docs/                  Documentation and provenance resources
notebooks/shared/      Executed publication-master notebook
results/manuscript_1/  MS1 figures, tables and supplementary outputs
results/manuscript_2/  MS2 figures, tables and supplementary outputs
scripts/               Reproducibility and integrity checks
CITATION.cff           Citation metadata
environment.yml        Conda environment specification
requirements.txt       Python dependency specification
LICENSE                Repository licence
```

For the precise publication-facing outputs, consult the two `MS1_PUBLICATION_MAP.txt` and `MS2_PUBLICATION_MAP.txt` files linked above rather than assuming that every historically generated output is part of a manuscript submission.

## Environment and verification

Clone the repository:

```bash
git clone https://github.com/UREKA-Biotec-OmicsLogic-Africa/cross-ancestry-asthma-transcriptomics-public.git
cd cross-ancestry-asthma-transcriptomics-public
```

Set up a compatible Python environment using `environment.yml` or `requirements.txt`, as appropriate for your system. The commands below are **repository verification checks**, not a promise that the complete upstream computational analysis will be rerun from raw data:

```bash
python scripts/verify_authoritative_run.py --root .
python scripts/verify_deoverlap_structure.py --root .
```

In the validated October 2026 working repository, the authoritative-run verifier reported:

```text
PASS: 72 generated files indexed
PASS: ancestry DE counts
PASS: sex DE counts
PASS: full network edge count
PASS: 13-gene curated set
FINAL STATUS: PASS
```

The structural/de-overlap verifier reported:

```text
FINAL STRUCTURE STATUS: PASS
```

These checks validate specified analytical products and publication-directory assignments. They do not replace independent assessment of source data, external validity, all optional intermediate files, or computational re-execution.

## Availability and responsible interpretation

This repository exposes the public computational and result materials selected for reproducibility; it does not redistribute confidential internal manuscripts or editorial documents. Verify any externally sourced or larger intermediate datasets against the repository documentation and original data-source terms before reuse.

Results are exploratory in the context of the analysed cohort. Recorded ancestry/race labels are metadata categories, not genetic-ancestry estimates; subgroup network counts are descriptive and should not be interpreted as evidence of differential network architecture without an appropriate inferential analysis.

## Citation and licence

Please consult [`CITATION.cff`](CITATION.cff) for the current software/repository citation metadata and [`LICENSE`](LICENSE) for reuse conditions. Cite GEO accession **GSE69683** and the relevant originating study when using the underlying expression data. Companion manuscript citations will be added when formally available.

## Contributing

Contributions and corrections are welcome through issues and pull requests, subject to repository access and project-maintainer review. Contributors should use their own GitHub-linked author identities and avoid adding manuscript drafts, private records, or sensitive material to public commits.
