# mechanics-v1-seed42 → copy-priority-fix-mechanics-seed42

Implementation `8624f5228f36611fb958408704f51bae59b0fc60` → `855024db872f940013d5d90071b234da601e493f`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 70.0% | 90.0% | +20.0 percentage points · improved |
| Expected-evidence recall | 48.3% | 78.3% | +30.0 percentage points · improved |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 7.31 | 6.81 | -0.50 · improved |
| p95 latency (s) | 14.24 | 13.63 | -0.60 · improved |
| Answers with unsupported claims | 1 | 1 | +0.00 · unchanged |
| Citation-support failures | 4 | 1 | -3.00 · improved |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 14 | 18 | +4.00 · improved |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| m01-poison-threshold / r1 | partial | partial | unchanged |
| m02-x-on-stack / r1 | correct | correct | unchanged |
| m03-x-outside-stack / r1 | abstained | correct | abstained → correct |
| m04-hybrid-mana-value / r1 | correct | correct | unchanged |
| m05-loyalty-stack-window / r1 | correct | correct | unchanged |
| m06-new-planeswalker-activation / r1 | correct | correct | unchanged |
| m07-loyalty-limit-permanent / r1 | correct | correct | unchanged |
| m08-loyalty-cost-and-source / r1 | abstained | abstained | unchanged |
| m09-siege-protector / r1 | correct | correct | unchanged |
| m10-siege-last-counter / r1 | correct | correct | unchanged |
| m11-monarch-combat-trigger / r1 | correct | correct | unchanged |
| m12-monarch-draw-trigger / r1 | correct | correct | unchanged |
| m13-initiative-multiple-damage / r1 | abstained | correct | abstained → correct |
| m14-retake-initiative / r1 | abstained | correct | abstained → correct |
| m15-phased-out-token / r1 | correct | correct | unchanged |
| m16-phased-out-board-wipe / r1 | correct | correct | unchanged |
| m17-regeneration-shield / r1 | correct | correct | unchanged |
| m18-extra-turn-order / r1 | correct | correct | unchanged |
| m19-land-not-a-spell / r1 | correct | correct | unchanged |
| m20-copy-not-cast / r1 | abstained | correct | abstained → correct |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
