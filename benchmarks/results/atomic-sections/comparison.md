# answer-contract → atomic-sections

Implementation `1432d4563ff7bf68cd3eb6f58f4416ce23272ce7` → `b486636207b2f856a53c2aeaeb072191c7ff8432`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 95.0% | 100.0% | +5.0 percentage points · improved |
| Expected-evidence recall | 93.8% | 96.2% | +2.5 percentage points · improved |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 12.11 | 10.21 | -1.90 · improved |
| p95 latency (s) | 17.99 | 16.35 | -1.64 · improved |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 1 | 0 | -1.00 · improved |
| Correct and normally completed | 19 | 20 | +1.00 · improved |

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
| 16-first-strike-blocker / r1 | correct | correct | unchanged |
| 17-token-blink / r1 | incorrect | correct | incorrect → correct |
| 18-summoning-sacrifice / r1 | correct | correct | unchanged |
| 19-legend-response / r1 | correct | correct | unchanged |
| 20-clarify-interaction / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
