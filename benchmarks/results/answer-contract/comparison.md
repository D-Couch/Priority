# precise-topics → answer-contract

Implementation `a45cb97eda13331fbb49fe87b6d81363918cdb9b` → `1432d4563ff7bf68cd3eb6f58f4416ce23272ce7`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 85.0% | 95.0% | +10.0 percentage points · improved |
| Expected-evidence recall | 96.2% | 93.8% | -2.5 percentage points · regressed |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 12.09 | 12.11 | +0.03 · regressed |
| p95 latency (s) | 15.97 | 17.99 | +2.01 · regressed |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 1 | +1.00 · regressed |
| Correct and normally completed | 17 | 19 | +2.00 · improved |

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
| 10-rest-in-peace / r1 | correct | correct | unchanged |
| 11-token-doublers / r1 | correct | correct | unchanged |
| 12-replacement-choice / r1 | correct | correct | unchanged |
| 13-apnap / r1 | correct | correct | unchanged |
| 14-humility-anthem / r1 | correct | correct | unchanged |
| 15-own-hexproof / r1 | correct | correct | unchanged |
| 16-first-strike-blocker / r1 | partial | correct | partial → correct |
| 17-token-blink / r1 | correct | incorrect | correct → incorrect |
| 18-summoning-sacrifice / r1 | partial | correct | partial → correct |
| 19-legend-response / r1 | correct | correct | unchanged |
| 20-clarify-interaction / r1 | partial | correct | partial → correct |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
