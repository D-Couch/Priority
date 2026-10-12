# gameplay-v1 verification 2026-10-12 → commander-damage-gameplay

Implementation `61bb104897f1aee2c425c7fec97902b918cbebaa` → `456390538f4da601b9f9f767d9436cec0ee0568c`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Expected-evidence recall | 96.2% | 96.2% | +0.0 percentage points · unchanged |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 11.27 | 10.87 | -0.40 · improved |
| p95 latency (s) | 19.03 | 19.58 | +0.55 · regressed |
| Answers with unsupported claims | 0 | 0 | +0.00 · unchanged |
| Citation-support failures | pending / n/a | pending / n/a | pending / n/a |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 20 | 20 | +0.00 · unchanged |

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
| 17-token-blink / r1 | correct | correct | unchanged |
| 18-summoning-sacrifice / r1 | correct | correct | unchanged |
| 19-legend-response / r1 | correct | correct | unchanged |
| 20-clarify-interaction / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
