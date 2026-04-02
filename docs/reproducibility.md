# Reproducibility note

## What this archive can reproduce

From the preserved CSV files, the included script can reproduce:

- descriptive summaries by workload, noise condition, and controller mode;
- paired deltas between controller modes;
- percentile bootstrap confidence intervals, assuming the archived script settings;
- manuscript tables derived from those CSV files.

## What this archive cannot reproduce

This archive does not contain the original simulator source that generated the run-level files. As a result, it cannot:

- regenerate `pairwise_runs.csv` from first principles;
- verify simulator implementation details beyond what was recorded in the preserved reports;
- re-run alternative controller gains or noise parameters without new simulator code.

## Why this still matters

The analysis is transparent at the level of the archived outputs. That is enough for:

- checking arithmetic and table generation,
- verifying the paired-seed statistical summaries,
- auditing the manuscript against the preserved outputs.

It is not enough for a full end-to-end methods reproduction.
