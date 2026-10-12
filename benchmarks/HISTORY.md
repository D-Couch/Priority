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
| [hybrid-lexical-preserving-heldout](results/hybrid-lexical-preserving-heldout/report.md) | heldout-v1 | `770ab3f865` | 27/32 | 27 | 0 | 78.6% | 10.65 |
| [hybrid-priority-packed-heldout](results/hybrid-priority-packed-heldout/report.md) | heldout-v1 | `2c6a37b371` | 28/32 | 28 | 0 | 75.5% | 10.96 |
| [hybrid-priority-packed-original](results/hybrid-priority-packed-original/report.md) | gameplay-v1 | `2c6a37b371` | 20/20 | 20 | 0 | 96.2% | 10.73 |
| [lexical-seed43-heldout](results/lexical-seed43-heldout/report.md) | heldout-v1 | `4144f33dff` | 27/32 | 27 | 0 | 75.5% | 11.13 |
| [lexical-seed43-original](results/lexical-seed43-original/report.md) | gameplay-v1 | `4144f33dff` | 20/20 | 20 | 0 | 96.2% | 10.95 |
| [hybrid-seed43-heldout](results/hybrid-seed43-heldout/report.md) | heldout-v1 | `4144f33dff` | 27/32 | 27 | 0 | 75.5% | 10.74 |
| [hybrid-seed43-original](results/hybrid-seed43-original/report.md) | gameplay-v1 | `4144f33dff` | 20/20 | 20 | 0 | 96.2% | 11.16 |
| [leave-game-rule-heldout](results/leave-game-rule-heldout/report.md) | heldout-v1 | `38ff1f08c8` | 0/0 | pending / n/a | 0 | 77.1% | 10.17 |
| [leave-game-rule-original](results/leave-game-rule-original/report.md) | gameplay-v1 | `38ff1f08c8` | 0/0 | pending / n/a | 0 | 96.2% | 10.93 |
| [leave-game-phrase-heldout](results/leave-game-phrase-heldout/report.md) | heldout-v1 | `b5987a7976` | 26/32 | 26 | 0 | 78.6% | 9.94 |
| [leave-game-phrase-original](results/leave-game-phrase-original/report.md) | gameplay-v1 | `b5987a7976` | 20/20 | 20 | 0 | 96.2% | 10.11 |
| [concise-outcomes-heldout](results/concise-outcomes-heldout/report.md) | heldout-v1 | `18b40500a9` | 24/32 | 24 | 0 | 78.6% | 11.04 |
| [concise-outcomes-original](results/concise-outcomes-original/report.md) | gameplay-v1 | `18b40500a9` | 20/20 | 20 | 0 | 96.2% | 10.61 |
| [casting-order-heldout](results/casting-order-heldout/report.md) | heldout-v1 | `1e5d8960cc` | 27/32 | 27 | 0 | 79.7% | 10.40 |
| [casting-order-original](results/casting-order-original/report.md) | gameplay-v1 | `1e5d8960cc` | 20/20 | 20 | 0 | 96.2% | 10.95 |
| [novel-v1-baseline](results/novel-v1-baseline/report.md) | novel-v1 | `0841001ac9` | 17/20 | 17 | 0 | 82.5% | 8.21 |
| [casting-order-contract-heldout](results/casting-order-contract-heldout/report.md) | heldout-v1 | `dea2984bcb` | 25/32 | 25 | 0 | 78.1% | 10.74 |
| [casting-order-contract-original](results/casting-order-contract-original/report.md) | gameplay-v1 | `dea2984bcb` | 20/20 | 20 | 0 | 96.2% | 11.16 |
| [gameplay-v1 verification 2026-10-12](results/verification-2026-10-12-gameplay/report.md) | gameplay-v1 | `0079f3e44c` | 20/20 | 20 | 0 | 96.2% | 11.27 |
| [heldout-v1 verification 2026-10-12](results/verification-2026-10-12-heldout/report.md) | heldout-v1 | `0079f3e44c` | 25/32 | 25 | 0 | 78.1% | 10.30 |
| [commander-damage-heldout](results/commander-damage-heldout/report.md) | heldout-v1 | `9acdbc3a36` | 26/32 | 26 | 0 | 81.2% | 10.50 |
| [commander-damage-gameplay](results/commander-damage-gameplay/report.md) | gameplay-v1 | `456390538f` | 20/20 | 20 | 0 | 96.2% | 10.87 |
| [reasoning-low-heldout](results/reasoning-low-heldout/report.md) | heldout-v1 | `10c549d012` | 29/32 | 29 | 0 | 81.2% | 8.41 |
| [reasoning-low-gameplay](results/reasoning-low-gameplay/report.md) | gameplay-v1 | `10c549d012` | 19/20 | pending / n/a | n/a | 96.2% | 8.18 |
| [reasoning-low-gameplay-isolated](results/reasoning-low-gameplay-isolated/report.md) | gameplay-v1 | `879563d751` | 20/20 | 20 | 0 | 96.2% | 8.38 |
| [reasoning-off-heldout](results/reasoning-off-heldout/report.md) | heldout-v1 | `f3d0bfb7b9` | 26/32 | 26 | 0 | 81.2% | 4.99 |
| [reasoning-off-gameplay](results/reasoning-off-gameplay/report.md) | gameplay-v1 | `f3d0bfb7b9` | 18/20 | 18 | 0 | 96.2% | 4.94 |
| [reasoning-low-gameplay-repeat](results/reasoning-low-gameplay-repeat/report.md) | gameplay-v1 | `d4491d1041` | 20/20 | 20 | 0 | 96.2% | 8.40 |
| [reasoning-low-default-gameplay](results/reasoning-low-default-gameplay/report.md) | gameplay-v1 | `823c4d85a1` | 20/20 | 20 | 0 | 96.2% | 8.49 |

Completion is n/a when historical finish telemetry is missing. Correctness is AI-assisted rubric review, not independent human validation. These are development cases; a single seeded run does not establish accuracy on unseen questions.

Review-note correction: [atomic-sections](results/atomic-sections/review-addendum.md).
Review-note correction: [heldout-baseline](results/heldout-baseline/review-addendum.md).