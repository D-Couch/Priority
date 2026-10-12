# focused-rulings → medium-reasoning

Implementation `c9ceef4f9720abcb28ebd8ca228b6289dcd7b42b` → `9a9dafd5e7dfad2f442f0d2a6d893e86373bb95e`

- `sampling.reasoning_effort`: ['"low"'] → ['"medium"']
Declared experimental variables: sampling.reasoning_effort. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 85.0% | 80.0% | -5.0 percentage points · regressed |
| Expected-evidence recall | 93.8% | 93.8% | +0.0 percentage points · unchanged |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 9.88 | 12.12 | +2.23 · regressed |
| p95 latency (s) | 17.72 | 19.39 | +1.67 · regressed |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 17 | 16 | -1.00 · regressed |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| 01-mana / r1 | correct | correct | unchanged |
| 02-hold-priority / r1 | correct | correct | unchanged |
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
| 17-token-blink / r1 | incorrect | incorrect | unchanged |
| 18-summoning-sacrifice / r1 | correct | partial | correct → partial |
| 19-legend-response / r1 | correct | correct | unchanged |
| 20-clarify-interaction / r1 | partial | partial | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
