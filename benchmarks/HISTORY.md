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
| [leave-game-rule-heldout](results/leave-game-rule-heldout/report.md) | heldout-v1 | `c8c6510b8f` | 0/0 | pending / n/a | 0 | 77.1% | 10.17 |
| [leave-game-rule-original](results/leave-game-rule-original/report.md) | gameplay-v1 | `c8c6510b8f` | 0/0 | pending / n/a | 0 | 96.2% | 10.93 |
| [leave-game-phrase-heldout](results/leave-game-phrase-heldout/report.md) | heldout-v1 | `00e3a79bc7` | 26/32 | 26 | 0 | 78.6% | 9.94 |
| [leave-game-phrase-original](results/leave-game-phrase-original/report.md) | gameplay-v1 | `00e3a79bc7` | 20/20 | 20 | 0 | 96.2% | 10.11 |
| [concise-outcomes-heldout](results/concise-outcomes-heldout/report.md) | heldout-v1 | `608bf3b06d` | 24/32 | 24 | 0 | 78.6% | 11.04 |
| [concise-outcomes-original](results/concise-outcomes-original/report.md) | gameplay-v1 | `608bf3b06d` | 20/20 | 20 | 0 | 96.2% | 10.61 |
| [casting-order-heldout](results/casting-order-heldout/report.md) | heldout-v1 | `2d31122fca` | 27/32 | 27 | 0 | 79.7% | 10.40 |
| [casting-order-original](results/casting-order-original/report.md) | gameplay-v1 | `2d31122fca` | 20/20 | 20 | 0 | 96.2% | 10.95 |
| [novel-v1-baseline](results/novel-v1-baseline/report.md) | novel-v1 | `b4da0a48c7` | 17/20 | 17 | 0 | 82.5% | 8.21 |
| [casting-order-contract-heldout](results/casting-order-contract-heldout/report.md) | heldout-v1 | `81f897e6d1` | 25/32 | 25 | 0 | 78.1% | 10.74 |
| [casting-order-contract-original](results/casting-order-contract-original/report.md) | gameplay-v1 | `81f897e6d1` | 20/20 | 20 | 0 | 96.2% | 11.16 |
| [gameplay-v1 verification 2026-10-12](results/verification-2026-10-12-gameplay/report.md) | gameplay-v1 | `d71b32a991` | 20/20 | 20 | 0 | 96.2% | 11.27 |
| [heldout-v1 verification 2026-10-12](results/verification-2026-10-12-heldout/report.md) | heldout-v1 | `d71b32a991` | 25/32 | 25 | 0 | 78.1% | 10.30 |
| [commander-damage-heldout](results/commander-damage-heldout/report.md) | heldout-v1 | `f2e4d92945` | 26/32 | 26 | 0 | 81.2% | 10.50 |
| [commander-damage-gameplay](results/commander-damage-gameplay/report.md) | gameplay-v1 | `5c91e67f88` | 20/20 | 20 | 0 | 96.2% | 10.87 |
| [reasoning-low-heldout](results/reasoning-low-heldout/report.md) | heldout-v1 | `4f916a92da` | 29/32 | 29 | 0 | 81.2% | 8.41 |
| [reasoning-low-gameplay](results/reasoning-low-gameplay/report.md) | gameplay-v1 | `4f916a92da` | 19/20 | pending / n/a | n/a | 96.2% | 8.18 |
| [reasoning-low-gameplay-isolated](results/reasoning-low-gameplay-isolated/report.md) | gameplay-v1 | `fbc4053338` | 20/20 | 20 | 0 | 96.2% | 8.38 |
| [reasoning-off-heldout](results/reasoning-off-heldout/report.md) | heldout-v1 | `94782cfa58` | 26/32 | 26 | 0 | 81.2% | 4.99 |
| [reasoning-off-gameplay](results/reasoning-off-gameplay/report.md) | gameplay-v1 | `94782cfa58` | 18/20 | 18 | 0 | 96.2% | 4.94 |
| [reasoning-low-gameplay-repeat](results/reasoning-low-gameplay-repeat/report.md) | gameplay-v1 | `0309b13dd9` | 20/20 | 20 | 0 | 96.2% | 8.40 |
| [reasoning-low-default-gameplay](results/reasoning-low-default-gameplay/report.md) | gameplay-v1 | `7901fc5fb1` | 20/20 | 20 | 0 | 96.2% | 8.49 |
| [low-prompt2800-gameplay](results/low-prompt2800-gameplay/report.md) | gameplay-v1 | `be096dc876` | 17/20 | 17 | 0 | 86.2% | 7.80 |
| [low-prompt3500-gameplay](results/low-prompt3500-gameplay/report.md) | gameplay-v1 | `a21d18ee13` | 18/20 | 18 | 0 | 93.8% | 8.50 |
| [cached-card-alias-gameplay](results/cached-card-alias-gameplay/report.md) | gameplay-v1 | `b19440a277` | 20/20 | 20 | 0 | 96.2% | 10.94 |
| [cached-card-alias-gameplay-repeat](results/cached-card-alias-gameplay-repeat/report.md) | gameplay-v1 | `b19440a277` | 20/20 | 20 | 0 | 96.2% | 10.90 |
| [parallel1-gameplay](results/parallel1-gameplay/report.md) | gameplay-v1 | `82bd05be6d` | 20/20 | 20 | 0 | 96.2% | 6.92 |
| [parallel1-gameplay-repeat](results/parallel1-gameplay-repeat/report.md) | gameplay-v1 | `82bd05be6d` | 20/20 | 20 | 0 | 96.2% | 6.89 |
| [evalbatch4096-gameplay](results/evalbatch4096-gameplay/report.md) | gameplay-v1 | `6f1655049d` | 20/20 | 20 | 0 | 96.2% | 7.43 |
| [physicalbatch1024-gameplay](results/physicalbatch1024-gameplay/report.md) | gameplay-v1 | `fe37f0c810` | 19/20 | 19 | 0 | 96.2% | 7.43 |
| [speculative-depth5-gameplay](results/speculative-depth5-gameplay/report.md) | gameplay-v1 | `b1166fde46` | 20/20 | 20 | 0 | 96.2% | 7.37 |
| [reasoning-off-parallel1-currentprompt](results/reasoning-off-parallel1-currentprompt/report.md) | gameplay-v1 | `46b65cc53d` | 18/20 | 18 | 0 | 96.2% | 3.90 |
| [final-guardrails-low-gameplay](results/final-guardrails-low-gameplay/report.md) | gameplay-v1 | `22ed98ddf3` | 18/20 | 18 | 0 | 96.2% | 7.85 |
| [reasoning-off-guardrails-gameplay](results/reasoning-off-guardrails-gameplay/report.md) | gameplay-v1 | `a025a91ec3` | 15/20 | 15 | 0 | 96.2% | 3.79 |
| [restored-prompt-low-gameplay](results/restored-prompt-low-gameplay/report.md) | gameplay-v1 | `c78c4fde8d` | 20/20 | 20 | 0 | 96.2% | 7.44 |
| [speculative-depth1-gameplay](results/speculative-depth1-gameplay/report.md) | gameplay-v1 | `fa249d800c` | 20/20 | 20 | 0 | 96.2% | 10.12 |
| [adaptive-reasoning-gameplay](results/adaptive-reasoning-gameplay/report.md) | gameplay-v1 | `9f14ea9b4f` | 19/20 | pending / n/a | n/a | 92.5% | 4.58 |
| [adaptive-reasoning-gameplay-repeat](results/adaptive-reasoning-gameplay-repeat/report.md) | gameplay-v1 | `9f14ea9b4f` | 20/20 | 20 | 0 | 96.2% | 4.22 |
| [adaptive-reasoning-heldout](results/adaptive-reasoning-heldout/report.md) | heldout-v1 | `e466761b9c` | 29/32 | 29 | 0 | 81.2% | 4.26 |
| [low-reasoning-seed43-parallel1](results/low-reasoning-seed43-parallel1/report.md) | gameplay-v1 | `e466761b9c` | 20/20 | 20 | 0 | 96.2% | 7.31 |
| [adaptive-reasoning-seed43](results/adaptive-reasoning-seed43/report.md) | gameplay-v1 | `e466761b9c` | 19/20 | 19 | 0 | 96.2% | 4.18 |
| [adaptive-reasoning-seed43-guarded](results/adaptive-reasoning-seed43-guarded/report.md) | gameplay-v1 | `4338abed70` | 20/20 | 20 | 0 | 96.2% | 6.18 |
| [adaptive-reasoning-seed43-narrow](results/adaptive-reasoning-seed43-narrow/report.md) | gameplay-v1 | `ef46eb58a2` | 19/20 | 19 | 0 | 96.2% | 4.14 |
| [adaptive-reasoning-seed43-final](results/adaptive-reasoning-seed43-final/report.md) | gameplay-v1 | `d7a6c3ca3f` | 20/20 | 20 | 0 | 96.2% | 4.15 |
| [adaptive-reasoning-seed42-final](results/adaptive-reasoning-seed42-final/report.md) | gameplay-v1 | `d7a6c3ca3f` | 20/20 | 20 | 0 | 96.2% | 4.25 |
| [lexical-low-heldout-current-baseline](results/lexical-low-heldout-current-baseline/report.md) | heldout-v1 | `a8ac3918d7` | 30/32 | 30 | 0 | 81.2% | 7.17 |
| [retrieval-core-rules-gameplay](results/retrieval-core-rules-gameplay/report.md) | gameplay-v1 | `8005ad57af` | 20/20 | 20 | 0 | 100.0% | 7.39 |
| [retrieval-core-rules-heldout](results/retrieval-core-rules-heldout/report.md) | heldout-v1 | `8005ad57af` | 30/32 | 30 | 0 | 82.0% | 7.22 |
| [pre-answer-precision](results/pre-answer-precision/report.md) | novel-v1 | `b0ecfbbae8` | 19/20 | 19 | 0 | 82.5% | 6.36 |
| [prototype-priority-novel](results/prototype-priority-novel/report.md) | novel-v1 | `cc0b677e84` | 20/20 | 20 | 0 | 87.5% | 5.95 |
| [prototype-priority-heldout](results/prototype-priority-heldout/report.md) | heldout-v1 | `cc0b677e84` | 30/32 | 30 | 0 | 82.0% | 7.51 |
| [prototype-priority-gameplay](results/prototype-priority-gameplay/report.md) | gameplay-v1 | `cc0b677e84` | 20/20 | 20 | 0 | 100.0% | 6.92 |
| [answer-contract-baseline-heldout](results/answer-contract-baseline-heldout/report.md) | heldout-v1 | `5eeede0874` | 30/32 | 30 | 0 | 82.0% | 7.48 |
| [explicit-clarification-heldout](results/explicit-clarification-heldout/report.md) | heldout-v1 | `a3e9798588` | 29/32 | 29 | 0 | 81.2% | 7.42 |
| [mechanics-v1-seed42](results/mechanics-v1-seed42/report.md) | mechanics-v1 | `8624f5228f` | 14/20 | 14 | 0 | 48.3% | 7.31 |
| [mechanics-v1-seed43](results/mechanics-v1-seed43/report.md) | mechanics-v1 | `8624f5228f` | 13/20 | 13 | 0 | 48.3% | 7.48 |
| [mechanics-v1-priority-seed42](results/mechanics-v1-priority-seed42/report.md) | mechanics-v1 | `14003d0673` | 18/20 | 18 | 0 | 78.3% | 6.86 |
| [mechanics-v1-priority-seed43](results/mechanics-v1-priority-seed43/report.md) | mechanics-v1 | `14003d0673` | 18/20 | 18 | 0 | 78.3% | 7.19 |
| [key-priority-gameplay](results/key-priority-gameplay/report.md) | gameplay-v1 | `14003d0673` | 19/20 | 19 | 0 | 100.0% | 7.01 |
| [key-priority-heldout](results/key-priority-heldout/report.md) | heldout-v1 | `14003d0673` | 29/32 | 29 | 0 | 82.0% | 7.52 |
| [key-priority-novel](results/key-priority-novel/report.md) | novel-v1 | `14003d0673` | 16/20 | 16 | 0 | 82.5% | 6.20 |

Completion is n/a when historical finish telemetry is missing. Correctness is AI-assisted rubric review, not independent human validation. These are development cases; a single seeded run does not establish accuracy on unseen questions.

Review-note correction: [atomic-sections](results/atomic-sections/review-addendum.md).
Review-note correction: [heldout-baseline](results/heldout-baseline/review-addendum.md).