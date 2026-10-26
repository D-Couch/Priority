# focused-heldout-2026-10-26-5 → focused-heldout-2026-10-26-6

Implementation `355b3487afbb597b105185bafea0c7cc76de6ee8` → `ede0095c1ceea2f1e9ce845330abb457fd4f33d5`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 81.2% | 87.5% | +6.2 percentage points · improved |
| Expected-evidence recall | 80.6% | 80.6% | +0.0 percentage points · unchanged |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 7.47 | 7.65 | +0.18 · regressed |
| p95 latency (s) | 10.62 | 12.31 | +1.69 · regressed |
| Answers with unsupported claims | 4 | 2 | -2.00 · improved |
| Citation-support failures | 3 | 1 | -2.00 · improved |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 26 | 28 | +2.00 · improved |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| h01-apnap / r1 | correct | correct | unchanged |
| h02-intervening-if / r1 | correct | correct | unchanged |
| h03-independent-trigger / r1 | correct | correct | unchanged |
| h04-replacement-death / r1 | correct | correct | unchanged |
| h05-simultaneous-death / r1 | incorrect | correct | incorrect → correct |
| h06-lifelink-prevented / r1 | correct | correct | unchanged |
| h07-infect-lifelink / r1 | correct | correct | unchanged |
| h08-protection-wrath / r1 | correct | correct | unchanged |
| h09-protection-aura / r1 | correct | correct | unchanged |
| h10-own-hexproof / r1 | correct | correct | unchanged |
| h11-ward-uncounterable / r1 | partial | correct | partial → correct |
| h12-split-second / r1 | correct | correct | unchanged |
| h13-sacrifice-cost / r1 | correct | correct | unchanged |
| h14-flashback-countered / r1 | correct | correct | unchanged |
| h15-rebound-countered / r1 | correct | correct | unchanged |
| h16-persist-counter / r1 | correct | correct | unchanged |
| h17-undying-simultaneous-sba / r1 | partial | correct | partial → correct |
| h18-blink-target / r1 | correct | correct | unchanged |
| h19-equip-timing / r1 | correct | correct | unchanged |
| h20-crew-new-creature / r1 | correct | correct | unchanged |
| h21-new-vehicle / r1 | correct | correct | unchanged |
| h22-tapped-blocker / r1 | correct | correct | unchanged |
| h23-fight-double-strike / r1 | correct | correct | unchanged |
| h24-leaving-controller / r1 | correct | correct | unchanged |
| h25-leaving-stack / r1 | correct | correct | unchanged |
| h26-commander-control / r1 | correct | correct | unchanged |
| h27-commander-hand / r1 | correct | correct | unchanged |
| h28-replacement-order / r1 | partial | partial | unchanged |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | partial | partial | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | correct | partial | correct → partial |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
