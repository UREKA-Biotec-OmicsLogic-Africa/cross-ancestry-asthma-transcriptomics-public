# Reproducibility

## Environment

- Record the validated Python version.
- Generate `requirements-lock.txt`.
- Record operating system and execution platform.
- Record the Git commit and release tag.
- Record random seeds.

## Execution

A clean release should support:

```bash
make setup
make test
make download
make prepare
make analysis
make figures
make supplement
make verify
```

## Notebook validation

- clean-kernel top-to-bottom execution;
- no saved exceptions;
- sequential execution counts;
- no hidden manual state;
- no hard-coded private paths;
- outputs traceable to code.

## Release artifacts

Include:

- tagged source code;
- executed notebook or HTML export where useful;
- stable tables and figures;
- supplementary package;
- manifest;
- checksums;
- environment lock;
- archived DOI.
