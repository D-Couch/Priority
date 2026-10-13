# final-general-v2-seed42

Status: **complete** · implementation commit `abe822bdac50f4d6ae4fb31b32e46fadf0a28a0c`

Suite `general-questions-v2` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 5/5 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 3/5 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 90.0% |
| Cases retrieving every expected evidence group | 4/5 |
| Answers with citations | 5/5 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 2 |
| Reviewed citation-support failures | 2 |
| Reviewed fully correct | 3/5 reviewed |
| Reviewed accuracy | 60.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 8.09 s |
| p95 successful response | 12.01 s |
| Median first visible answer token | 5.01 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | partial | 12.01 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 5.09 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 4.45 |
| g04-replacement-order-general (r1) | 100.0% | partial | 8.09 |
| g05-protection-and-random-target (r1) | 50.0% | correct | 10.61 |

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

Review: **partial**. Direct answer and scope for MTR 3.9 are correct, but the response includes a visibly incorrect d6-to-four-options mapping, then self-corrects mid-example and adds a long sequential-coin-flip aside. Prefer shuffled slips for arbitrary choices and keep this simple question concise.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A copy does not acquire counters on the original creature, nor does it acquire a +2/+2 bonus from an Aura (or any other continuous effect) on that creature.

**Why:** When copying an object, the copy acquires only the copiable values of the original's characteristics. Other effects (including type-changing and text-changing effects), status, counters, and stickers are explicitly not copied. [CR 707.2] A +2/+2 from an Aura is a continuous effect applied to the original permanent, not a copiable value, so the copy enters without it. [CR 707.2]

Review: **correct**. Correctly states counters and an Aura’s continuous bonus are not copied; CR 707.2 supports the general answer.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights another creature.

**Why:** Double strike is a static ability that modifies the rules for the *combat damage step* specifically [CR 702.4a]. The fight action is a separate mechanic in which each creature deals damage equal to its power to the other, and that damage is explicitly not combat damage [CR 701.14a], [CR 701.14d]. Since double strike only applies during combat damage steps, it has no effect on the fight action.

Review: **correct**. Correct: fight damage is not combat damage, so double strike has no effect and each creature deals its power once.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or its owner if it has no controller) or the affected player chooses which replacement effect to apply first. They do not both automatically happen—the player picks one, applies it, then checks whether the other is still applicable to the *modified* event. If the modified event no longer triggers the second effect, it simply does nothing.

**Why:** [CR 616.1] establishes that the affected player chooses which replacement effect to apply when two or more are attempting to modify the same event. [CR 616.1f] explains that after one is applied, the process repeats with only the effects still applicable to the now-modified event. [CR 614.7] confirms that if a replacement effect's target event no longer happens, it simply does nothing.

For example, if one effect says "If a creature would enter the battlefield, it enters with a +1/+1 counter instead" and another says "If a creature would enter the battlefield, it enters tapped instead," the controller chooses one to apply first. If they choose the counter effect, the creature enters with a counter and untapped (the "tapped" effect no longer applies because the event was already modified). If they choose the tapped effect, the creature enters tapped without the counter.

Review: **partial**. The core process is correctly cited, but the unsolicited hypothetical is wrong. “Enters with a +1/+1 counter” and “enters tapped” replacements can both apply to the same entering event; neither automatically stops the other. Avoid invented example effect text.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red is not a legal target for a red spell, so it must be excluded from the random selection pool.

**Why:** Protection from red means the creature "can't be targeted by spells with the stated quality" [CR 702.16b]. When a spell requires a target, only legal targets may be chosen [CR 601.2c]. Since the random selection is still choosing a target, the eligible pool is limited to creatures that are legal targets—those without protection from red (or other effects that would make them illegal targets). In practice, you would shuffle the eligible creatures (or use an equivalent fair randomizer) and select from that reduced pool.

Review: **correct**. Correctly excludes the creature made illegal by protection and cites both CR 702.16b and the target legality rule. No die-roll guidance is mixed into the answer.
Reviewer: Codex

Missing reference groups: CR 115.2

