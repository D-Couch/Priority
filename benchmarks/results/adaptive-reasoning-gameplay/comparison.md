# parallel1-gameplay-repeat → adaptive-reasoning-gameplay

Implementation `82bd05be6da0be624d97624c27336eeea9b70c85` → `9f14ea9b4f752c0cc86005187131431e2e838082`

- `sampling.reasoning_effort`: ['"low"'] → ['"low"', '"none"']
Declared experimental variables: sampling.reasoning_effort. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 100.0% | 95.0% | -5.0 percentage points · regressed |
| Expected-evidence recall | 96.2% | 92.5% | -3.7 percentage points · regressed |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 6.89 | 4.58 | -2.31 · improved |
| p95 latency (s) | 9.73 | 11.30 | +1.57 · regressed |
| Answers with unsupported claims | 0 | 0 | +0.00 · unchanged |
| Citation-support failures | 0 | 1 | +1.00 · regressed |
| Request errors | 0 | 1 | +1.00 · regressed |
| Truncated answers | 0 | pending / n/a | pending / n/a |
| Correct and normally completed | 20 | pending / n/a | pending / n/a |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| 01-mana / r1 | correct | correct | unchanged |
| 02-hold-priority / r1 | correct | correct | unchanged |
| 03-illegal-target / r1 | correct | correct | unchanged |
| 04-partial-targets / r1 | correct | correct | unchanged |
| 05-trample-indestructible / r1 | correct | correct | unchanged |
| 06-deathtouch-trample / r1 | correct | correct | unchanged |
| 07-zero-toughness / r1 | correct | correct | unchanged |
| 08-commander-dies / r1 | correct | correct | unchanged |
| 09-commander-tax / r1 | correct | correct | unchanged |
| 10-rest-in-peace / r1 | correct | error | correct → error |
| 11-token-doublers / r1 | correct | correct | unchanged |
| 12-replacement-choice / r1 | correct | correct | unchanged |
| 13-apnap / r1 | correct | correct | unchanged |
| 14-humility-anthem / r1 | correct | correct | unchanged |
| 15-own-hexproof / r1 | correct | correct | unchanged |
| 16-first-strike-blocker / r1 | correct | correct | unchanged |
| 17-token-blink / r1 | correct | correct | unchanged |
| 18-summoning-sacrifice / r1 | correct | correct | unchanged |
| 19-legend-response / r1 | correct | correct | unchanged |
| 20-clarify-interaction / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
