# Benchmark history

Each implementation change is committed before its full benchmark; reviewed results are committed separately. Runs appear in measurement order. Historical artifacts and the original pre-vectorization tags are preserved.

| Run | Suite | Tested commit | Reviewed correct | Correct and complete | Truncated | Evidence recall | Median s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [pre-vectorization](results/pre-vectorization/report.md) | gameplay-v1 | `98cd7e4318` | 12/20 | pending / n/a | n/a | 63.3% | 20.02 |
| [low-reasoning](results/low-reasoning/report.md) | gameplay-v1 | `6a176bd62b` | 16/20 | 16 | 0 | 63.3% | 12.37 |
| [structural-retrieval](results/structural-retrieval/report.md) | gameplay-v1 | `43d9d2a2dc` | 18/20 | 16 | 3 | 96.2% | 11.22 |
| [token-budget](results/token-budget/report.md) | gameplay-v1 | `6cf5cc3f71` | 18/20 | 18 | 0 | 93.8% | 10.83 |
| [focused-rulings](results/focused-rulings/report.md) | gameplay-v1 | `c9ceef4f97` | 17/20 | 17 | 0 | 93.8% | 9.88 |
| [medium-reasoning](results/medium-reasoning/report.md) | gameplay-v1 | `9a9dafd5e7` | 16/20 | 16 | 0 | 93.8% | 12.12 |
| [precise-topics](results/precise-topics/report.md) | gameplay-v1 | `a45cb97eda` | 17/20 | 17 | 0 | 96.2% | 12.09 |
| [answer-contract](results/answer-contract/report.md) | gameplay-v1 | `1432d4563f` | 19/20 | 19 | 1 | 93.8% | 12.11 |
| [atomic-sections](results/atomic-sections/report.md) | gameplay-v1 | `b486636207` | 20/20 | 20 | 0 | 96.2% | 10.21 |
| [atomic-sections-seed43](results/atomic-sections-seed43/report.md) | gameplay-v1 | `47ceb48a2f` | 20/20 | 20 | 0 | 96.2% | 9.95 |
| [heldout-baseline](results/heldout-baseline/report.md) | heldout-v1 | `e184b2efaf` | 25/32 | 25 | 0 | 75.5% | 10.91 |
| [relevant-rulings-heldout](results/relevant-rulings-heldout/report.md) | heldout-v1 | `1b544b16bb` | 25/32 | 25 | 0 | 75.5% | 10.26 |
| [relevant-rulings-original](results/relevant-rulings-original/report.md) | gameplay-v1 | `1b544b16bb` | 20/20 | 20 | 0 | 96.2% | 10.27 |
| [source-quotes-heldout](results/source-quotes-heldout/report.md) | heldout-v1 | `6f31339abf` | 25/32 | 25 | 0 | 75.5% | 10.25 |
| [source-quotes-original](results/source-quotes-original/report.md) | gameplay-v1 | `6f31339abf` | 20/20 | 20 | 0 | 96.2% | 9.92 |
| [hybrid-heldout](results/hybrid-heldout/report.md) | heldout-v1 | `2df6e9b3a6` | 29/32 | 29 | 0 | 81.0% | 10.69 |
| [hybrid-original](results/hybrid-original/report.md) | gameplay-v1 | `2df6e9b3a6` | 19/20 | 19 | 0 | 93.8% | 10.62 |
| [hybrid-neighbors-heldout](results/hybrid-neighbors-heldout/report.md) | heldout-v1 | `8cd2f2fdef` | 28/32 | 28 | 0 | 80.2% | 10.91 |
| [hybrid-neighbors-original](results/hybrid-neighbors-original/report.md) | gameplay-v1 | `8cd2f2fdef` | 19/20 | 19 | 0 | 93.8% | 11.48 |
| [hybrid-family-heldout](results/hybrid-family-heldout/report.md) | heldout-v1 | `d55b40a747` | 28/32 | 28 | 0 | 77.9% | 11.11 |
| [hybrid-family-original](results/hybrid-family-original-run2/report.md) | gameplay-v1 | `d55b40a747` | 19/20 | 19 | 0 | 89.6% | 11.73 |

Completion is n/a when historical finish telemetry is missing. Correctness is AI-assisted rubric review, not independent human validation. These are development cases; a single seeded run does not establish accuracy on unseen questions.

Review-note correction: [atomic-sections](results/atomic-sections/review-addendum.md).
Review-note correction: [heldout-baseline](results/heldout-baseline/review-addendum.md).