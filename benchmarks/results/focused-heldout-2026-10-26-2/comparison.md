# focused-heldout-2026-10-26 → focused-heldout-2026-10-26-2

Implementation `8b30a311015f6b7df72a8522ec3d89522ef45572` → `31e05b08fe647d5cd8dbe29e6f3b7c64c109837d`

- `answer_contract_sha256`: 98780f9a73d8c51d60687aa5daeaad3546fcdf4cd25bd8e47cee3957586cf37f → d5b31f3a741c1675c7092c8cb0c3d0445af8cb1baaf55c237c6e25e2da7bdc53
Declared experimental variables: answer_contract. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 87.5% | 87.5% | +0.0 percentage points · unchanged |
| Expected-evidence recall | 82.7% | 79.6% | -3.1 percentage points · regressed |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 7.46 | 7.48 | +0.02 · regressed |
| p95 latency (s) | 11.13 | 11.81 | +0.68 · regressed |
| Answers with unsupported claims | 2 | 0 | -2.00 · improved |
| Citation-support failures | 0 | 0 | +0.00 · unchanged |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 28 | 28 | +0.00 · unchanged |

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
| h23-fight-double-strike / r1 | partial | correct | partial → correct |
| h24-leaving-controller / r1 | correct | correct | unchanged |
| h25-leaving-stack / r1 | correct | correct | unchanged |
| h26-commander-control / r1 | correct | correct | unchanged |
| h27-commander-hand / r1 | correct | incorrect | correct → incorrect |
| h28-replacement-order / r1 | partial | correct | partial → correct |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | partial | partial | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | correct | incorrect | correct → incorrect |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
