# Targeted rule retrieval results

Implementation under test: `855024db872f940013d5d90071b234da601e493f` (`fix: preserve specific rules when prioritizing copies`). This follow-up narrows CR 707.10 priority to spell-copy questions and prioritizes CR 702.153a when casualty is discussed. A regression test verifies that both rules survive context packing for their respective queries.

| Suite | Reviewed result | Expected-evidence recall | Median latency | Errors / truncations |
|---|---:|---:|---:|---:|
| Mechanics-v1, seed 42 | 18/20 | 78.3% | 6.81 s | 0 / 0 |
| Mechanics-v1, seed 43 | 18/20 | 78.3% | 7.14 s | 0 / 0 |
| Gameplay-v1, seed 42 | 20/20 | 100% | 7.15 s | 0 / 0 |
| Heldout-v1, seed 42 | 29/32 | 82.0% | 7.43 s | 0 / 0 |
| Novel-v1, seed 42 | 17/20 | 87.5% | 5.95 s | 0 / 0 |

All reviews were AI-assisted and were not independently validated by a Magic judge. These are development-suite measurements, not estimates of accuracy on unseen questions.

## Effect of the change

Compared with the original mechanics runs, fully correct answers rose from 14/20 and 13/20 to 18/20 in both seeds. Exact expected-evidence recall rose from 48.3% to 78.3%. The model now answers the X-on-stack, X-off-stack, hybrid mana value, initiative, and copied-spell cases with the expected rules in context. Median response time stayed near seven seconds.

The first priority implementation put CR 707.10 ahead of the casualty rule and caused a wrong casualty answer. The saved candidate trace contained CR 702.153a, but the final packed prompt omitted it. The follow-up priority fixed that interaction: the corrected novel run retrieved the casualty rule and answered correctly. Expected-evidence recall and median latency returned to the earlier measured levels.

Gameplay returned 20/20 and its answers matched the previous 20/20 run. Heldout remains at 29/32; its two underspecified prompts still need better clarification behavior, and the Ward answer omits that Ward triggers. The novel suite remains 17/20 under strict application of its frozen criteria: the missed details are enlist's optional attack cost, mentor trigger timing, and myriad token characteristics.

The original `prototype-priority-novel` review reported 20/20, but it credited the same omissions on enlist, mentor, and myriad despite their explicit frozen criteria. This review correction is documented in that run's `review-addendum.md`; under the same strict criteria used here, the original answers also score 17/20. The first broad-priority result and this correction remain in history for auditability.

## Remaining mechanics misses

Both mechanics seeds still miss the poison citation’s scope: CR 904.13c is specific to Archenemy games, while the general poison loss rule is CR 104.3d. The loyalty/source-removal case is incomplete or makes an unsupported source-independence claim. The next work should tighten citation-to-claim checks and the handling of multi-part rules questions, while keeping the existing gameplay score intact.
