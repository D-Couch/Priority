# focused-heldout-2026-10-26-4 → focused-heldout-2026-10-26-5

Implementation `a2be46ded16abba4fd06cadc1d07d995afaf5dd8` → `355b3487afbb597b105185bafea0c7cc76de6ee8`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 81.2% | 81.2% | +0.0 percentage points · unchanged |
| Expected-evidence recall | 78.8% | 80.6% | +1.8 percentage points · improved |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 7.50 | 7.47 | -0.03 · improved |
| p95 latency (s) | 14.51 | 10.62 | -3.89 · improved |
| Answers with unsupported claims | 3 | 4 | +1.00 · regressed |
| Citation-support failures | 4 | 3 | -1.00 · improved |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 26 | 26 | +0.00 · unchanged |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| h01-apnap / r1 | correct | correct | unchanged |
| h02-intervening-if / r1 | correct | correct | unchanged |
| h03-independent-trigger / r1 | correct | correct | unchanged |
| h04-replacement-death / r1 | correct | correct | unchanged |
| h05-simultaneous-death / r1 | correct | incorrect | correct → incorrect |
| h06-lifelink-prevented / r1 | correct | correct | unchanged |
| h07-infect-lifelink / r1 | correct | correct | unchanged |
| h08-protection-wrath / r1 | correct | correct | unchanged |
| h09-protection-aura / r1 | correct | correct | unchanged |
| h10-own-hexproof / r1 | correct | correct | unchanged |
| h11-ward-uncounterable / r1 | partial | partial | unchanged |
| h12-split-second / r1 | correct | correct | unchanged |
| h13-sacrifice-cost / r1 | correct | correct | unchanged |
| h14-flashback-countered / r1 | correct | correct | unchanged |
| h15-rebound-countered / r1 | correct | correct | unchanged |
| h16-persist-counter / r1 | correct | correct | unchanged |
| h17-undying-simultaneous-sba / r1 | correct | partial | correct → partial |
| h18-blink-target / r1 | correct | correct | unchanged |
| h19-equip-timing / r1 | partial | correct | partial → correct |
| h20-crew-new-creature / r1 | correct | correct | unchanged |
| h21-new-vehicle / r1 | correct | correct | unchanged |
| h22-tapped-blocker / r1 | correct | correct | unchanged |
| h23-fight-double-strike / r1 | correct | correct | unchanged |
| h24-leaving-controller / r1 | correct | correct | unchanged |
| h25-leaving-stack / r1 | partial | correct | partial → correct |
| h26-commander-control / r1 | correct | correct | unchanged |
| h27-commander-hand / r1 | correct | correct | unchanged |
| h28-replacement-order / r1 | partial | partial | unchanged |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | partial | partial | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
