# structural-retrieval → token-budget

Implementation `43d9d2a2dc1c68f5f4eaf5ea440f0e418c5b8d52` → `6cf5cc3f7153454a9d60510df64e49bc09bb6438`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 90.0% | 90.0% | +0.0 percentage points · unchanged |
| Expected-evidence recall | 96.2% | 93.8% | -2.5 percentage points · regressed |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 11.22 | 10.83 | -0.39 · improved |
| p95 latency (s) | 16.16 | 14.31 | -1.86 · improved |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 3 | 0 | -3.00 · improved |
| Correct and normally completed | 16 | 18 | +2.00 · improved |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| 01-mana / r1 | correct | correct | unchanged |
| 02-hold-priority / r1 | correct | correct | unchanged |
| 03-illegal-target / r1 | correct | correct | unchanged |
| 04-partial-targets / r1 | correct | correct | unchanged |
| 05-trample-indestructible / r1 | correct | correct | unchanged |
| 06-deathtouch-trample / r1 | correct | correct | unchanged |
| 07-zero-toughness / r1 | correct | correct | unchanged |
| 08-commander-dies / r1 | partial | partial | unchanged |
| 09-commander-tax / r1 | correct | correct | unchanged |
| 10-rest-in-peace / r1 | correct | correct | unchanged |
| 11-token-doublers / r1 | correct | correct | unchanged |
| 12-replacement-choice / r1 | correct | correct | unchanged |
| 13-apnap / r1 | correct | correct | unchanged |
| 14-humility-anthem / r1 | correct | correct | unchanged |
| 15-own-hexproof / r1 | correct | correct | unchanged |
| 16-first-strike-blocker / r1 | correct | correct | unchanged |
| 17-token-blink / r1 | correct | correct | unchanged |
| 18-summoning-sacrifice / r1 | correct | correct | unchanged |
| 19-legend-response / r1 | correct | correct | unchanged |
| 20-clarify-interaction / r1 | partial | partial | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
