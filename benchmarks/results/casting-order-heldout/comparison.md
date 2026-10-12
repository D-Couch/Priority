# leave-game-phrase-heldout → casting-order-heldout

Implementation `6a78d5fa695aa3647f4a31435c4bd159bd962953` → `7c10de49239b03725b9e22e27a8e7dc49c8d27c6`

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 81.2% | 84.4% | +3.1 percentage points · improved |
| Expected-evidence recall | 78.6% | 79.7% | +1.0 percentage points · improved |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 9.94 | 10.40 | +0.46 · regressed |
| p95 latency (s) | 17.12 | 17.38 | +0.27 · regressed |
| Answers with unsupported claims | 4 | 3 | -1.00 · improved |
| Citation-support failures | 8 | pending / n/a | pending / n/a |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 26 | 27 | +1.00 · improved |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| h01-apnap / r1 | correct | correct | unchanged |
| h02-intervening-if / r1 | correct | correct | unchanged |
| h03-independent-trigger / r1 | correct | correct | unchanged |
| h04-replacement-death / r1 | correct | correct | unchanged |
| h05-simultaneous-death / r1 | correct | correct | unchanged |
| h06-lifelink-prevented / r1 | correct | correct | unchanged |
| h07-infect-lifelink / r1 | partial | partial | unchanged |
| h08-protection-wrath / r1 | correct | correct | unchanged |
| h09-protection-aura / r1 | correct | correct | unchanged |
| h10-own-hexproof / r1 | correct | correct | unchanged |
| h11-ward-uncounterable / r1 | correct | correct | unchanged |
| h12-split-second / r1 | correct | correct | unchanged |
| h13-sacrifice-cost / r1 | partial | correct | partial → correct |
| h14-flashback-countered / r1 | correct | correct | unchanged |
| h15-rebound-countered / r1 | correct | correct | unchanged |
| h16-persist-counter / r1 | correct | correct | unchanged |
| h17-undying-simultaneous-sba / r1 | correct | correct | unchanged |
| h18-blink-target / r1 | correct | correct | unchanged |
| h19-equip-timing / r1 | partial | partial | unchanged |
| h20-crew-new-creature / r1 | correct | correct | unchanged |
| h21-new-vehicle / r1 | correct | correct | unchanged |
| h22-tapped-blocker / r1 | correct | correct | unchanged |
| h23-fight-double-strike / r1 | partial | partial | unchanged |
| h24-leaving-controller / r1 | correct | correct | unchanged |
| h25-leaving-stack / r1 | correct | correct | unchanged |
| h26-commander-control / r1 | abstained | abstained | unchanged |
| h27-commander-hand / r1 | correct | correct | unchanged |
| h28-replacement-order / r1 | correct | correct | unchanged |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | correct | correct | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
