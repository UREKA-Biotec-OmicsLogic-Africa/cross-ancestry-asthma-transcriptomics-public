# Statistical Analysis Plan

Finalize this document before freezing the publication release.

## Genome-wide ancestry analysis

- unit: GPL570 probe set;
- test or model: to be finalized;
- fold-change definition: difference in mean log2 expression;
- multiple testing: Benjamini-Hochberg;
- FDR threshold: 0.05;
- absolute log2 fold-change threshold: 0.5.

## Genome-wide gender analysis

Specify the same details and whether ancestry is included as a covariate.

## Curated-gene analysis

Planned model:

```text
expression ~ ancestry + gender
```

State the coding, reference groups, model assumptions, correction scope, and effect reported.

## Pathway analysis

Document GSEA ranking statistic, permutation type, permutation count, gene-set-size limits, ssGSEA normalization, and FDR correction.

## Co-expression analysis

Treat subgroup networks as exploratory. Pre-specify the correlation method and threshold.

## Reconciliation requirement

All methods in this document, the code, tables, figures, supplementary files, abstract, Methods, Results, and legends must agree.
