# answer-contract-baseline-heldout → explicit-clarification-heldout

Implementation `d5c6fd8959c75cf6ab70d942c4ee1b2c69c6e172` → `23b765f61e3d1cb7fd96869fd40ae0ff896fe3bf`

- `answer_contract_sha256`: 81b6351dd895ecdffc3e220f9200c6f5cf1cb6fa2d9f2b13269805d48975c67c → 4401ddd2f2c7da15d570530f8add7ea7ae0b4b93c7d4a99dcf40f6ceed08d176
Declared experimental variables: answer_contract. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 93.8% | 90.6% | -3.1 percentage points · regressed |
| Expected-evidence recall | 82.0% | 81.2% | -0.8 percentage points · regressed |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 7.48 | 7.42 | -0.06 · improved |
| p95 latency (s) | 12.17 | 14.04 | +1.87 · regressed |
| Answers with unsupported claims | 2 | 3 | +1.00 · regressed |
| Citation-support failures | 0 | 1 | +1.00 · regressed |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 30 | 29 | -1.00 · regressed |

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
| h11-ward-uncounterable / r1 | correct | correct | unchanged |
| h12-split-second / r1 | correct | correct | unchanged |
| h13-sacrifice-cost / r1 | correct | correct | unchanged |
| h14-flashback-countered / r1 | correct | correct | unchanged |
| h15-rebound-countered / r1 | correct | correct | unchanged |
| h16-persist-counter / r1 | correct | correct | unchanged |
| h17-undying-simultaneous-sba / r1 | correct | correct | unchanged |
| h18-blink-target / r1 | correct | correct | unchanged |
| h19-equip-timing / r1 | correct | correct | unchanged |
| h20-crew-new-creature / r1 | correct | correct | unchanged |
| h21-new-vehicle / r1 | correct | correct | unchanged |
| h22-tapped-blocker / r1 | correct | correct | unchanged |
| h23-fight-double-strike / r1 | correct | correct | unchanged |
| h24-leaving-controller / r1 | correct | correct | unchanged |
| h25-leaving-stack / r1 | correct | partial | correct → partial |
| h26-commander-control / r1 | correct | correct | unchanged |
| h27-commander-hand / r1 | correct | correct | unchanged |
| h28-replacement-order / r1 | correct | correct | unchanged |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | incorrect | incorrect | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
