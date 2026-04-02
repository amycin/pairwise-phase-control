# Pairwise local phase summaries under continuous phase-kick noise

This repository packages a simulation-analysis manuscript and the preserved artifacts used to write it.

## What is included

- `paper/`:
  - `paper.md`: editable manuscript source
  - `paper.tex`: LaTeX export
  - `paper.docx`: editable Word version
  - `paper.pdf`: compiled PDF
  - `references.bib`: bibliography file
  - `figures/`: figure assets used in the manuscript
- `data/`:
  - `pairwise_runs.csv`: preserved run-level results
  - `pairwise_summary.csv`: descriptive summaries by workload, noise, and mode
  - `pairwise_comparisons.csv`: paired deltas and bootstrap confidence intervals
  - `entropy_sensitivity.csv`: fresh-seed sensitivity summaries
- `scripts/`:
  - `reproduce_analysis.py`: reproduces summary tables from the saved CSVs
- `docs/`:
  - `reproducibility.md`: explanation of what is and is not reproducible from this archive

## Scope

The manuscript explains a narrow repeated-seed statevector simulation result. It does not claim hardware validation, a compiler/runtime advantage, or a universal control improvement. The result is limited to:

- the preserved 6-qubit and 12-qubit nearest-neighbor chain workloads,
- the archived continuous phase-kick noise models,
- the archived controller modes `OFF`, `SINGLE_BLOCK`, and `PAIR_BLOCK`,
- the cycles-to-threshold endpoint at fidelity `< 0.90`.

## Reproducibility status

This package supports **analysis reproducibility** from the preserved CSV outputs.

It does **not** support end-to-end rerunning of the original simulator, because the simulator source that generated the archived run tables was not preserved in the artifact bundle. The included script regenerates the descriptive and paired-comparison statistics from the archived CSV files.

## Recommended citation

See `CITATION.cff`.

## License

- Code and scripts: MIT
- Manuscript text and figures authored for this package: CC BY 4.0 is recommended if you choose to publish publicly.
- Third-party reference metadata remain attributed to their original sources.
