# pre-vectorization → atomic-sections

Implementation `98cd7e431879a9817252d623a3ca5fe5373a06ea` → `b486636207b2f856a53c2aeaeb072191c7ff8432`

- `sampling.reasoning_effort`: ['"server default"'] → ['"medium"']
Declared experimental variables: sampling.reasoning_effort. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 60.0% | 100.0% | +40.0 percentage points · improved |
| Expected-evidence recall | 63.3% | 96.2% | +32.9 percentage points · improved |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 20.02 | 10.21 | -9.81 · improved |
| p95 latency (s) | 41.05 | 16.35 | -24.70 · improved |
| Request errors | 6 | 0 | -6.00 · improved |
| Truncated answers | pending / n/a | 0 | pending / n/a |
| Correct and normally completed | pending / n/a | 20 | pending / n/a |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| 01-mana / r1 | correct | correct | unchanged |
| 02-hold-priority / r1 | abstained | correct | abstained → correct |
| 03-illegal-target / r1 | correct | correct | unchanged |
| 04-partial-targets / r1 | correct | correct | unchanged |
| 05-trample-indestructible / r1 | correct | correct | unchanged |
| 06-deathtouch-trample / r1 | error | correct | error → correct |
| 07-zero-toughness / r1 | error | correct | error → correct |
| 08-commander-dies / r1 | error | correct | error → correct |
| 09-commander-tax / r1 | correct | correct | unchanged |
| 10-rest-in-peace / r1 | correct | correct | unchanged |
| 11-token-doublers / r1 | error | correct | error → correct |
| 12-replacement-choice / r1 | correct | correct | unchanged |
| 13-apnap / r1 | correct | correct | unchanged |
| 14-humility-anthem / r1 | correct | correct | unchanged |
| 15-own-hexproof / r1 | correct | correct | unchanged |
| 16-first-strike-blocker / r1 | error | correct | error → correct |
| 17-token-blink / r1 | error | correct | error → correct |
| 18-summoning-sacrifice / r1 | correct | correct | unchanged |
| 19-legend-response / r1 | correct | correct | unchanged |
| 20-clarify-interaction / r1 | partial | correct | partial → correct |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
