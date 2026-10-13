# reasoning-low-default-gameplay → low-prompt2800-gameplay

Implementation `7901fc5fb15b2189b1d8c4d64065b8b19e6ce16e` → `be096dc87615d993e7e9c5eba8e55a31227947b7`

- `context_budget.max_prompt_tokens`: 4628 → 2800
Declared experimental variables: context_budget.max_prompt_tokens. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 100.0% | 85.0% | -15.0 percentage points · regressed |
| Expected-evidence recall | 96.2% | 86.2% | -10.0 percentage points · regressed |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 8.49 | 7.80 | -0.69 · improved |
| p95 latency (s) | 11.26 | 15.54 | +4.28 · regressed |
| Answers with unsupported claims | 0 | 1 | +1.00 · regressed |
| Citation-support failures | 0 | 1 | +1.00 · regressed |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 20 | 17 | -3.00 · regressed |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| 01-mana / r1 | correct | correct | unchanged |
| 02-hold-priority / r1 | correct | correct | unchanged |
| 03-illegal-target / r1 | correct | correct | unchanged |
| 04-partial-targets / r1 | correct | correct | unchanged |
| 05-trample-indestructible / r1 | correct | correct | unchanged |
| 06-deathtouch-trample / r1 | correct | correct | unchanged |
| 07-zero-toughness / r1 | correct | correct | unchanged |
| 08-commander-dies / r1 | correct | partial | correct → partial |
| 09-commander-tax / r1 | correct | correct | unchanged |
| 10-rest-in-peace / r1 | correct | correct | unchanged |
| 11-token-doublers / r1 | correct | correct | unchanged |
| 12-replacement-choice / r1 | correct | partial | correct → partial |
| 13-apnap / r1 | correct | correct | unchanged |
| 14-humility-anthem / r1 | correct | correct | unchanged |
| 15-own-hexproof / r1 | correct | correct | unchanged |
| 16-first-strike-blocker / r1 | correct | correct | unchanged |
| 17-token-blink / r1 | correct | correct | unchanged |
| 18-summoning-sacrifice / r1 | correct | correct | unchanged |
| 19-legend-response / r1 | correct | partial | correct → partial |
| 20-clarify-interaction / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
