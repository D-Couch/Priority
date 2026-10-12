# low-reasoning → structural-retrieval

Implementation `6a176bd62b197dfc27ebe1eefa20c8adc2923674` → `43d9d2a2dc1c68f5f4eaf5ea440f0e418c5b8d52`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 80.0% | 90.0% | +10.0 percentage points · improved |
| Expected-evidence recall | 63.3% | 96.2% | +32.9 percentage points · improved |
| Citation ID validity | 97.6% | 100.0% | +2.4 percentage points · improved |
| Median latency (s) | 12.37 | 11.22 | -1.15 · improved |
| p95 latency (s) | 18.61 | 16.16 | -2.44 · improved |
| Request errors | 0 | 0 | +0.00 · unchanged |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| 01-mana / r1 | correct | correct | unchanged |
| 02-hold-priority / r1 | abstained | correct | abstained → correct |
| 03-illegal-target / r1 | correct | correct | unchanged |
| 04-partial-targets / r1 | correct | correct | unchanged |
| 05-trample-indestructible / r1 | correct | correct | unchanged |
| 06-deathtouch-trample / r1 | correct | correct | unchanged |
| 07-zero-toughness / r1 | incorrect | correct | incorrect → correct |
| 08-commander-dies / r1 | correct | partial | correct → partial |
| 09-commander-tax / r1 | correct | correct | unchanged |
| 10-rest-in-peace / r1 | correct | correct | unchanged |
| 11-token-doublers / r1 | correct | correct | unchanged |
| 12-replacement-choice / r1 | correct | correct | unchanged |
| 13-apnap / r1 | correct | correct | unchanged |
| 14-humility-anthem / r1 | correct | correct | unchanged |
| 15-own-hexproof / r1 | correct | correct | unchanged |
| 16-first-strike-blocker / r1 | correct | correct | unchanged |
| 17-token-blink / r1 | partial | correct | partial → correct |
| 18-summoning-sacrifice / r1 | correct | correct | unchanged |
| 19-legend-response / r1 | correct | correct | unchanged |
| 20-clarify-interaction / r1 | partial | partial | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
