# Benchmark history

Each implementation change is committed before its full benchmark; reviewed results are committed separately. Runs appear in measurement order. Historical artifacts and the original pre-vectorization tags are preserved.

| Run | Tested commit | Reviewed correct | Correct and complete | Truncated | Evidence recall | Median s |
| --- | --- | --- | --- | --- | --- | --- |
| [pre-vectorization](results/pre-vectorization/report.md) | `98cd7e4318` | 12/20 | pending / n/a | n/a | 63.3% | 20.02 |
| [low-reasoning](results/low-reasoning/report.md) | `6a176bd62b` | 16/20 | 16 | 0 | 63.3% | 12.37 |
| [structural-retrieval](results/structural-retrieval/report.md) | `43d9d2a2dc` | 18/20 | 16 | 3 | 96.2% | 11.22 |
| [token-budget](results/token-budget/report.md) | `6cf5cc3f71` | 18/20 | 18 | 0 | 93.8% | 10.83 |
| [focused-rulings](results/focused-rulings/report.md) | `c9ceef4f97` | 17/20 | 17 | 0 | 93.8% | 9.88 |
| [medium-reasoning](results/medium-reasoning/report.md) | `9a9dafd5e7` | 16/20 | 16 | 0 | 93.8% | 12.12 |
| [precise-topics](results/precise-topics/report.md) | `a45cb97eda` | 17/20 | 17 | 0 | 96.2% | 12.09 |
| [answer-contract](results/answer-contract/report.md) | `1432d4563f` | 19/20 | 19 | 1 | 93.8% | 12.11 |
| [atomic-sections](results/atomic-sections/report.md) | `b486636207` | 20/20 | 20 | 0 | 96.2% | 10.21 |
| [atomic-sections-seed43](results/atomic-sections-seed43/report.md) | `47ceb48a2f` | 20/20 | 20 | 0 | 96.2% | 9.95 |
| [heldout-baseline](results/heldout-baseline/report.md) | `e184b2efaf` | 25/32 | 25 | 0 | 75.5% | 10.91 |
| [relevant-rulings-heldout](results/relevant-rulings-heldout/report.md) | `1b544b16bb` | 25/32 | 25 | 0 | 75.5% | 10.26 |
| [relevant-rulings-original](results/relevant-rulings-original/report.md) | `1b544b16bb` | 20/20 | 20 | 0 | 96.2% | 10.27 |
| [source-quotes-heldout](results/source-quotes-heldout/report.md) | `6f31339abf` | 25/32 | 25 | 0 | 75.5% | 10.25 |
| [source-quotes-original](results/source-quotes-original/report.md) | `6f31339abf` | 20/20 | 20 | 0 | 96.2% | 9.92 |

Completion is n/a when historical finish telemetry is missing. Correctness is AI-assisted rubric review, not independent human validation. These are development cases; a single seeded run does not establish accuracy on unseen questions.

Review-note correction: [atomic-sections](results/atomic-sections/review-addendum.md).