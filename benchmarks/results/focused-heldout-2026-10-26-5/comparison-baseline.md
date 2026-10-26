# focused-heldout-seed42 → focused-heldout-2026-10-26-5

Implementation `9bd6927e08e72f4dd5eee8de720e79ced44746bf` → `355b3487afbb597b105185bafea0c7cc76de6ee8`

- `answer_contract_sha256`: ab098cb019c3f97f0d1acccb45c74c47ff52421c24f5a1a6ce0c9ff9d162a7cd → e9862c98394644e16b8a430ebb02c942f824a7734fee4b347b4ea8563168a842
Declared experimental variables: answer_contract. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 87.5% | 81.2% | -6.2 percentage points · regressed |
| Expected-evidence recall | 80.4% | 80.6% | +0.3 percentage points · improved |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 7.49 | 7.47 | -0.01 · improved |
| p95 latency (s) | 11.88 | 10.62 | -1.26 · improved |
| Answers with unsupported claims | 0 | 4 | +4.00 · regressed |
| Citation-support failures | 1 | 3 | +2.00 · regressed |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 28 | 26 | -2.00 · regressed |

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
| h19-equip-timing / r1 | correct | correct | unchanged |
| h20-crew-new-creature / r1 | correct | correct | unchanged |
| h21-new-vehicle / r1 | correct | correct | unchanged |
| h22-tapped-blocker / r1 | correct | correct | unchanged |
| h23-fight-double-strike / r1 | correct | correct | unchanged |
| h24-leaving-controller / r1 | correct | correct | unchanged |
| h25-leaving-stack / r1 | correct | correct | unchanged |
| h26-commander-control / r1 | correct | correct | unchanged |
| h27-commander-hand / r1 | correct | correct | unchanged |
| h28-replacement-order / r1 | correct | partial | correct → partial |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | partial | partial | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | incorrect | correct | incorrect → correct |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
