# packed-target-rules-general-v2-seed42

Status: **complete** · implementation commit `1ae326ef82422324e9a5d040cf2c7061da3c6e28`

Suite `general-questions-v2` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 5/5 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | pending / n/a/0 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 100.0% |
| Cases retrieving every expected evidence group | 5/5 |
| Answers with citations | 5/5 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | pending / n/a |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 0/0 reviewed |
| Reviewed accuracy | pending / n/a |
| Mean reviewed rubric score | pending / n/a |
| Median successful response | 7.33 s |
| p95 successful response | 12.48 s |
| Median first visible answer token | 5.01 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | pending | 12.48 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | pending | 5.36 |
| g03-fight-and-double-strike (r1) | 100.0% | pending | 4.71 |
| g04-replacement-order-general (r1) | 100.0% | pending | 8.13 |
| g05-protection-and-random-target (r1) | 100.0% | pending | 7.33 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** The card or effect determines the eligible pool of options, and you must use a physical method that gives each eligible option an equal chance of being selected.

**Why:**

- For **die-roll game actions** specifically, the Tournament Rules state that any method that simulates the roll is acceptable as long as every result has an equal chance of occurring [MTR 3.9]. So a standard d6 works, but so does shuffling six numbered slips and drawing one.

- For **other random selections** (e.g., "choose one of these at random"), the same fairness principle applies in practice: each eligible option must have an equal probability. Common paper methods include:
  - **Shuffled slips:** Write each eligible option on a separate slip, shuffle, and draw one.
  - **Evenly mapped die results:** If there are 4 options, map a d6 so that options 1–2 each get two faces (e.g., 1–2 → option A, 3–4 → option B, 5–6 → option C… wait, that's only 3). For 4 options, use a d8 (1–2 → A, 3–4 → B, 5–6 → C, 7–8 → D) or reroll any result that doesn't map evenly.
  - **Coin flips** work cleanly for exactly 2 options.

The key constraint is equal probability per option. A sequential coin-flip elimination (flip heads → remove option 1, tails → remove option 2, etc.) does **not** give each option an equal chance when there are more than two options, so it should be avoided.

If you have a specific card in mind, share it and I can help identify the exact eligible pool and suggest the cleanest physical method.

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A copy does not acquire counters on the original creature, nor does it acquire a +2/+2 bonus from an Aura (or any other continuous effect) on that creature.

**Why:** When copying an object, the copy acquires only the copiable values of the original's characteristics. Other effects (including type-changing and text-changing effects), status, counters, and stickers are explicitly not copied. [CR 707.2] A +2/+2 from an Aura is a continuous effect applied to the original permanent, not a copiable value, so the copy enters without it. [CR 707.2]

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights another creature.

**Why:** Double strike is a static ability that modifies the rules for the *combat damage step* specifically [CR 702.4a]. The fight action is a separate mechanic in which each creature deals damage equal to its power to the other, and that damage is explicitly not combat damage [CR 701.14a], [CR 701.14d]. Since double strike only applies during combat damage steps, it has no effect on the fight action.

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or its owner if it has no controller) or the affected player chooses which replacement effect to apply first. They do not both automatically happen—the player picks one, applies it, then checks whether the other is still applicable to the *modified* event. If the modified event no longer triggers the second effect, it simply does nothing.

**Why:** [CR 616.1] establishes that the affected player chooses which replacement effect to apply when two or more are attempting to modify the same event. [CR 616.1f] explains that after one is applied, the process repeats with only the effects still applicable to the now-modified event. [CR 614.7] confirms that if a replacement effect's target event no longer happens, it simply does nothing.

For example, if one effect says "If a creature would enter the battlefield, it enters with a +1/+1 counter instead" and another says "If a creature would enter the battlefield, it enters tapped instead," the controller chooses one to apply first. If they choose the counter effect, the creature enters with a counter and untapped (the "tapped" effect no longer applies because the event was already modified). If they choose the tapped effect, the creature enters tapped without the counter.

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red cannot be selected, even if the target is chosen at random.

**Why:** Protection from red means the creature can't be targeted by red spells [CR 702.16b]. When a spell requires a target, only legal targets may be chosen [CR 601.2c]. A random selection mechanism doesn't override the targeting restriction—the eligible pool is limited to creatures that are legal targets, and a protected creature is not one of them.

Missing reference groups: none

