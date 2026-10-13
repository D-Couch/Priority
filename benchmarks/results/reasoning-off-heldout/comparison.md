# commander-damage-heldout → reasoning-off-heldout

Implementation `f2e4d929457865f16046eba4048f1cc788357f4a` → `94782cfa58dad9e250be87d2211a7094c749d0d8`

- `sampling.reasoning_effort`: ['"medium"'] → ['"none"']
Declared experimental variables: sampling.reasoning_effort. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 81.2% | 81.2% | +0.0 percentage points · unchanged |
| Expected-evidence recall | 81.2% | 81.2% | +0.0 percentage points · unchanged |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 10.50 | 4.99 | -5.51 · improved |
| p95 latency (s) | 17.42 | 13.36 | -4.06 · improved |
| Answers with unsupported claims | 5 | 6 | +1.00 · regressed |
| Citation-support failures | pending / n/a | 1 | pending / n/a |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 26 | 26 | +0.00 · unchanged |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| h01-apnap / r1 | partial | correct | partial → correct |
| h02-intervening-if / r1 | correct | correct | unchanged |
| h03-independent-trigger / r1 | correct | partial | correct → partial |
| h04-replacement-death / r1 | correct | correct | unchanged |
| h05-simultaneous-death / r1 | correct | correct | unchanged |
| h06-lifelink-prevented / r1 | correct | partial | correct → partial |
| h07-infect-lifelink / r1 | partial | correct | partial → correct |
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
| h19-equip-timing / r1 | partial | correct | partial → correct |
| h20-crew-new-creature / r1 | correct | correct | unchanged |
| h21-new-vehicle / r1 | correct | correct | unchanged |
| h22-tapped-blocker / r1 | correct | correct | unchanged |
| h23-fight-double-strike / r1 | partial | partial | unchanged |
| h24-leaving-controller / r1 | correct | correct | unchanged |
| h25-leaving-stack / r1 | correct | correct | unchanged |
| h26-commander-control / r1 | correct | correct | unchanged |
| h27-commander-hand / r1 | correct | correct | unchanged |
| h28-replacement-order / r1 | correct | partial | correct → partial |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | incorrect | incorrect | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
