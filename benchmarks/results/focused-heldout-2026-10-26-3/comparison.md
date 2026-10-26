# focused-heldout-2026-10-26-2 → focused-heldout-2026-10-26-3

Implementation `31e05b08fe647d5cd8dbe29e6f3b7c64c109837d` → `1ce5d2185b8bed03fdb7e154914bb2778fd96134`

- `answer_contract_sha256`: d5b31f3a741c1675c7092c8cb0c3d0445af8cb1baaf55c237c6e25e2da7bdc53 → c5cd0cff5dbe97742fe6fdeb0932e7da31f4410630e324085432f8ea23ed1b14
Declared experimental variables: answer_contract. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 87.5% | 84.4% | -3.1 percentage points · regressed |
| Expected-evidence recall | 79.6% | 78.8% | -0.8 percentage points · regressed |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 7.48 | 7.74 | +0.26 · regressed |
| p95 latency (s) | 11.81 | 11.76 | -0.05 · improved |
| Answers with unsupported claims | 0 | 1 | +1.00 · regressed |
| Citation-support failures | 0 | 1 | +1.00 · regressed |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 28 | 27 | -1.00 · regressed |

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
| h25-leaving-stack / r1 | correct | correct | unchanged |
| h26-commander-control / r1 | correct | correct | unchanged |
| h27-commander-hand / r1 | incorrect | incorrect | unchanged |
| h28-replacement-order / r1 | correct | partial | correct → partial |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | partial | partial | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | incorrect | partial | incorrect → partial |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
