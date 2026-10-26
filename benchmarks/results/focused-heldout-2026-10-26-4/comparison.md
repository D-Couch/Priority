# focused-heldout-2026-10-26-3 → focused-heldout-2026-10-26-4

Implementation `1ce5d2185b8bed03fdb7e154914bb2778fd96134` → `a2be46ded16abba4fd06cadc1d07d995afaf5dd8`

- `answer_contract_sha256`: c5cd0cff5dbe97742fe6fdeb0932e7da31f4410630e324085432f8ea23ed1b14 → e9862c98394644e16b8a430ebb02c942f824a7734fee4b347b4ea8563168a842
Declared experimental variables: answer_contract. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 84.4% | 81.2% | -3.1 percentage points · regressed |
| Expected-evidence recall | 78.8% | 78.8% | +0.0 percentage points · unchanged |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 7.74 | 7.50 | -0.24 · improved |
| p95 latency (s) | 11.76 | 14.51 | +2.75 · regressed |
| Answers with unsupported claims | 1 | 3 | +2.00 · regressed |
| Citation-support failures | 1 | 4 | +3.00 · regressed |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 27 | 26 | -1.00 · regressed |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| h01-apnap / r1 | correct | correct | unchanged |
| h02-intervening-if / r1 | correct | correct | unchanged |
| h03-independent-trigger / r1 | correct | correct | unchanged |
| h04-replacement-death / r1 | correct | correct | unchanged |
| h05-simultaneous-death / r1 | correct | correct | unchanged |
| h06-lifelink-prevented / r1 | correct | correct | unchanged |
| h07-infect-lifelink / r1 | correct | correct | unchanged |
| h08-protection-wrath / r1 | correct | correct | unchanged |
| h09-protection-aura / r1 | correct | correct | unchanged |
| h10-own-hexproof / r1 | correct | correct | unchanged |
| h11-ward-uncounterable / r1 | correct | partial | correct → partial |
| h12-split-second / r1 | correct | correct | unchanged |
| h13-sacrifice-cost / r1 | correct | correct | unchanged |
| h14-flashback-countered / r1 | correct | correct | unchanged |
| h15-rebound-countered / r1 | correct | correct | unchanged |
| h16-persist-counter / r1 | correct | correct | unchanged |
| h17-undying-simultaneous-sba / r1 | correct | correct | unchanged |
| h18-blink-target / r1 | correct | correct | unchanged |
| h19-equip-timing / r1 | correct | partial | correct → partial |
| h20-crew-new-creature / r1 | correct | correct | unchanged |
| h21-new-vehicle / r1 | correct | correct | unchanged |
| h22-tapped-blocker / r1 | correct | correct | unchanged |
| h23-fight-double-strike / r1 | correct | correct | unchanged |
| h24-leaving-controller / r1 | correct | correct | unchanged |
| h25-leaving-stack / r1 | correct | partial | correct → partial |
| h26-commander-control / r1 | correct | correct | unchanged |
| h27-commander-hand / r1 | incorrect | correct | incorrect → correct |
| h28-replacement-order / r1 | partial | partial | unchanged |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | partial | partial | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | partial | correct | partial → correct |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
