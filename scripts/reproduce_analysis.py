#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd


def percentile_bootstrap_ci(values: np.ndarray, n_boot: int = 5000, seed: int = 12345):
    rng = np.random.default_rng(seed)
    vals = np.asarray(values, dtype=float)
    meds = np.empty(n_boot, dtype=float)
    n = len(vals)
    for i in range(n_boot):
        sample = vals[rng.integers(0, n, size=n)]
        meds[i] = np.median(sample)
    lo, hi = np.percentile(meds, [2.5, 97.5])
    return float(lo), float(hi)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', required=True, help='Path to pairwise_runs.csv')
    ap.add_argument('--outdir', required=True)
    ap.add_argument('--bootstrap', type=int, default=5000)
    ap.add_argument('--seed', type=int, default=12345)
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    runs = pd.read_csv(args.data)
    summary = runs.groupby(['workload','n','noise','mode']).agg(
        seeds=('cycle_to_threshold','size'),
        median_cycles=('cycle_to_threshold','median'),
        mean_cycles=('cycle_to_threshold','mean'),
        sd_cycles=('cycle_to_threshold','std'),
        q25=('cycle_to_threshold', lambda x: np.quantile(x, 0.25)),
        q75=('cycle_to_threshold', lambda x: np.quantile(x, 0.75)),
    ).reset_index()
    summary.to_csv(outdir / 'pairwise_summary_recomputed.csv', index=False)

    rows = []
    for (workload, n, noise), sub in runs.groupby(['workload', 'n', 'noise']):
        piv = sub.pivot(index='seed', columns='mode', values='cycle_to_threshold').sort_index()
        for a, b in [('SINGLE_BLOCK', 'OFF'), ('PAIR_BLOCK', 'OFF'), ('PAIR_BLOCK', 'SINGLE_BLOCK')]:
            delta = (piv[a] - piv[b]).dropna().to_numpy()
            ci_lo, ci_hi = percentile_bootstrap_ci(delta, n_boot=args.bootstrap, seed=args.seed)
            rows.append({
                'comparison': f'{a}_minus_{b}',
                'median_delta': float(np.median(delta)),
                'mean_delta': float(np.mean(delta)),
                'ci_lo': ci_lo,
                'ci_hi': ci_hi,
                'positive_frac': float(np.mean(delta > 0)),
                'negative_frac': float(np.mean(delta < 0)),
                'zero_frac': float(np.mean(delta == 0)),
                'seeds': int(delta.size),
                'workload': workload,
                'n': int(n),
                'noise': noise,
            })
    pd.DataFrame(rows).to_csv(outdir / 'pairwise_comparisons_recomputed.csv', index=False)


if __name__ == '__main__':
    main()
