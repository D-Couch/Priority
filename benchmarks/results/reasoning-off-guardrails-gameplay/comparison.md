# final-guardrails-low-gameplay → reasoning-off-guardrails-gameplay

Implementation `22ed98ddf31574780c627d0ea155d28ecdac5e4c` → `a025a91ec32f03256f8a01632b60c2c8cc0682d1`

- `sampling.reasoning_effort`: ['"low"'] → ['"none"']
Declared experimental variables: sampling.reasoning_effort. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 90.0% | 75.0% | -15.0 percentage points · regressed |
| Expected-evidence recall | 96.2% | 96.2% | +0.0 percentage points · unchanged |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 7.85 | 3.79 | -4.05 · improved |
| p95 latency (s) | 12.55 | 4.43 | -8.13 · improved |
| Answers with unsupported claims | 1 | 4 | +3.00 · regressed |
| Citation-support failures | 1 | 3 | +2.00 · regressed |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 18 | 15 | -3.00 · regressed |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| 01-mana / r1 | correct | correct | unchanged |
| 02-hold-priority / r1 | correct | partial | correct → partial |
| 03-illegal-target / r1 | correct | correct | unchanged |
| 04-partial-targets / r1 | correct | correct | unchanged |
| 05-trample-indestructible / r1 | correct | correct | unchanged |
| 06-deathtouch-trample / r1 | correct | correct | unchanged |
| 07-zero-toughness / r1 | incorrect | correct | incorrect → correct |
| 08-commander-dies / r1 | correct | correct | unchanged |
| 09-commander-tax / r1 | correct | correct | unchanged |
| 10-rest-in-peace / r1 | correct | correct | unchanged |
| 11-token-doublers / r1 | correct | partial | correct → partial |
| 12-replacement-choice / r1 | correct | correct | unchanged |
| 13-apnap / r1 | correct | incorrect | correct → incorrect |
| 14-humility-anthem / r1 | correct | correct | unchanged |
| 15-own-hexproof / r1 | correct | correct | unchanged |
| 16-first-strike-blocker / r1 | correct | correct | unchanged |
| 17-token-blink / r1 | correct | correct | unchanged |
| 18-summoning-sacrifice / r1 | correct | correct | unchanged |
| 19-legend-response / r1 | partial | partial | unchanged |
| 20-clarify-interaction / r1 | correct | incorrect | correct → incorrect |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
