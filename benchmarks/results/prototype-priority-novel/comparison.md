# pre-answer-precision → prototype-priority-novel

Implementation `9a635a80fb672bd199e3b0c2e8dec9cf334c5923` → `ad79a4ff6898c4d8fb7026fd9aeb08af3a9d7f95`

- `retrieval`: {'mode': 'lexical'} → {'mode': 'lexical'}
Declared experimental variables: retrieval. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 95.0% | 100.0% | +5.0 percentage points · improved |
| Expected-evidence recall | 82.5% | 87.5% | +5.0 percentage points · improved |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 6.36 | 5.95 | -0.41 · improved |
| p95 latency (s) | 9.85 | 8.11 | -1.74 · improved |
| Answers with unsupported claims | 1 | 0 | -1.00 · improved |
| Citation-support failures | 1 | 0 | -1.00 · improved |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 19 | 20 | +1.00 · improved |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| n01-bestow-illegal-target / r1 | correct | correct | unchanged |
| n02-mutate-illegal-target / r1 | correct | correct | unchanged |
| n03-saga-final-chapter / r1 | correct | correct | unchanged |
| n04-prototype-graveyard / r1 | incorrect | correct | incorrect → correct |
| n05-overload-hexproof / r1 | correct | correct | unchanged |
| n06-level-up / r1 | correct | correct | unchanged |
| n07-keyword-counter / r1 | correct | correct | unchanged |
| n08-adventure-exile / r1 | correct | correct | unchanged |
| n09-foretell-turn / r1 | correct | correct | unchanged |
| n10-suspend-last-counter / r1 | correct | correct | unchanged |
| n11-morph-special-action / r1 | correct | correct | unchanged |
| n12-dfc-returned / r1 | correct | correct | unchanged |
| n13-afterlife-exile / r1 | correct | correct | unchanged |
| n14-enlist-sickness / r1 | correct | correct | unchanged |
| n15-mentor-target / r1 | correct | correct | unchanged |
| n16-convoke-summoning-sickness / r1 | correct | correct | unchanged |
| n17-casualty-copy / r1 | correct | correct | unchanged |
| n18-myriad-tokens / r1 | correct | correct | unchanged |
| n19-totem-armor / r1 | correct | correct | unchanged |
| n20-bolster / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
