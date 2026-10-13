# copy-priority-fix-mechanics-seed43 → poison-loyalty-retrieval-seed43

Implementation `855024db872f940013d5d90071b234da601e493f` → `7b7297d9aae78fdafe8b311fd541666794edc9f2`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 90.0% | 100.0% | +10.0 percentage points · improved |
| Expected-evidence recall | 78.3% | 95.0% | +16.7 percentage points · improved |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 7.14 | 6.34 | -0.80 · improved |
| p95 latency (s) | 10.14 | 9.68 | -0.46 · improved |
| Answers with unsupported claims | 2 | 0 | -2.00 · improved |
| Citation-support failures | 1 | 0 | -1.00 · improved |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 18 | 20 | +2.00 · improved |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| m01-poison-threshold / r1 | partial | correct | partial → correct |
| m02-x-on-stack / r1 | correct | correct | unchanged |
| m03-x-outside-stack / r1 | correct | correct | unchanged |
| m04-hybrid-mana-value / r1 | correct | correct | unchanged |
| m05-loyalty-stack-window / r1 | correct | correct | unchanged |
| m06-new-planeswalker-activation / r1 | correct | correct | unchanged |
| m07-loyalty-limit-permanent / r1 | correct | correct | unchanged |
| m08-loyalty-cost-and-source / r1 | partial | correct | partial → correct |
| m09-siege-protector / r1 | correct | correct | unchanged |
| m10-siege-last-counter / r1 | correct | correct | unchanged |
| m11-monarch-combat-trigger / r1 | correct | correct | unchanged |
| m12-monarch-draw-trigger / r1 | correct | correct | unchanged |
| m13-initiative-multiple-damage / r1 | correct | correct | unchanged |
| m14-retake-initiative / r1 | correct | correct | unchanged |
| m15-phased-out-token / r1 | correct | correct | unchanged |
| m16-phased-out-board-wipe / r1 | correct | correct | unchanged |
| m17-regeneration-shield / r1 | correct | correct | unchanged |
| m18-extra-turn-order / r1 | correct | correct | unchanged |
| m19-land-not-a-spell / r1 | correct | correct | unchanged |
| m20-copy-not-cast / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
