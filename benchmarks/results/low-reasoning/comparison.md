# pre-vectorization → low-reasoning

Implementation `98cd7e431879a9817252d623a3ca5fe5373a06ea` → `6a176bd62b197dfc27ebe1eefa20c8adc2923674`

- `sampling.reasoning_effort`: ['"server default"'] → ['"low"']
Declared experimental variables: sampling.reasoning_effort. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 60.0% | 80.0% | +20.0 percentage points · improved |
| Expected-evidence recall | 63.3% | 63.3% | +0.0 percentage points · unchanged |
| Citation ID validity | 100.0% | 97.6% | -2.4 percentage points · regressed |
| Median latency (s) | 20.02 | 12.37 | -7.66 · improved |
| p95 latency (s) | 41.05 | 18.61 | -22.44 · improved |
| Request errors | 6 | 0 | -6.00 · improved |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| 01-mana / r1 | correct | correct | unchanged |
| 02-hold-priority / r1 | abstained | abstained | unchanged |
| 03-illegal-target / r1 | correct | correct | unchanged |
| 04-partial-targets / r1 | correct | correct | unchanged |
| 05-trample-indestructible / r1 | correct | correct | unchanged |
| 06-deathtouch-trample / r1 | error | correct | error → correct |
| 07-zero-toughness / r1 | error | incorrect | error → incorrect |
| 08-commander-dies / r1 | error | correct | error → correct |
| 09-commander-tax / r1 | correct | correct | unchanged |
| 10-rest-in-peace / r1 | correct | correct | unchanged |
| 11-token-doublers / r1 | error | correct | error → correct |
| 12-replacement-choice / r1 | correct | correct | unchanged |
| 13-apnap / r1 | correct | correct | unchanged |
| 14-humility-anthem / r1 | correct | correct | unchanged |
| 15-own-hexproof / r1 | correct | correct | unchanged |
| 16-first-strike-blocker / r1 | error | correct | error → correct |
| 17-token-blink / r1 | error | partial | error → partial |
| 18-summoning-sacrifice / r1 | correct | correct | unchanged |
| 19-legend-response / r1 | correct | correct | unchanged |
| 20-clarify-interaction / r1 | partial | partial | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
