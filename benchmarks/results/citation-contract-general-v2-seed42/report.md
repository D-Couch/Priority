# citation-contract-general-v2-seed42

Status: **complete** · implementation commit `6ab8b65cb3c26a8697ddcea0c62f75ff144c3dfe`

Suite `general-questions-v2` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 5/5 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 5/5 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 100.0% |
| Cases retrieving every expected evidence group | 5/5 |
| Answers with citations | 5/5 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 5/5 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 8.81 s |
| p95 successful response | 9.65 s |
| Median first visible answer token | 6.58 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | correct | 9.65 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 8.74 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 6.11 |
| g04-replacement-order-general (r1) | 100.0% | correct | 8.81 |
| g05-protection-and-random-target (r1) | 100.0% | correct | 8.83 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** The card or effect defines the eligible pool of options, and you must use a method that gives each eligible option an equal chance of being selected. Common paper methods include shuffling slips of paper (one per eligible option) and drawing one, or mapping a die's faces evenly onto the options (rerolling any face that doesn't map to an eligible option).

**Why:** For die-roll game actions specifically, the Tournament Rules state that any method that simulates the roll is acceptable as long as every result has an equal chance of occurring [MTR 3.9]. For other random choices (e.g., "randomly choose one of these cards"), the same equal-chance principle applies, but the eligible pool is determined by the card's text, not by a fixed die face. For example, if an effect says "randomly choose one of the cards in your graveyard," you'd write each card name on a slip, shuffle, and draw one. If an effect says "flip a coin," a single coin flip is the prescribed method. Avoid sequential coin-flip sequences for more than two options, since that produces unequal probabilities.

Review: **correct**. Directly answers with equal-chance paper methods, distinguishes die-roll MTR guidance from other random choices, and uses the card text to define the eligible pool. No exact card is needed for this general answer.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A copy does not acquire counters on the original creature, nor does it acquire a +2/+2 (or any other) bonus from an Aura or similar effect.

**Why:** The copiable values are limited to characteristics derived from the object's printed text (name, mana cost, color, types, rules text, power, toughness, loyalty), as modified by other copy effects and certain "as it enters" abilities. "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." [CR 707.2] So an Aura's +2/+2 is a non-copiable effect, and any counters (P/T, charge, fade, etc.) are explicitly excluded. The copy will have the original's *printed* power and toughness (or whatever a characteristic-defining ability sets), but not the Aura-modified value.

Review: **correct**. Correctly states that counters and continuous bonuses from an Aura are not part of copiable values. CR 707.2 directly supports the claim.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights another creature. It deals damage equal to its power once, the same as any other fight.

**Why:** Double strike is defined as a static ability that modifies the rules for the *combat damage step* specifically [CR 702.4a]. The fight mechanic is a separate action where each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Since double strike only applies during combat damage steps, it has no effect on fight damage.

Review: **correct**. Correct: each creature deals power damage once when it fights; fight damage is not combat damage, so double strike does not add a second event. The citations support each part.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or its owner if it has no controller) or the affected player chooses which replacement effect to apply first. They do not both automatically happen—the player picks one, applies it, then checks whether the other is still applicable to the *modified* event. If the first replacement completely changes the event so the second no longer applies, the second does nothing.

**Why:** [CR 616.1] assigns the choice to the affected object's controller or the affected player, and [CR 616.1f] states that after one effect is applied, the process repeats only with effects that are *now* applicable. Because a replaced event "never happens" and a modified event occurs instead [CR 614.6], a second replacement effect that was watching for the original event may simply have no event to replace [CR 614.7].

**Example:** If a creature would die and one effect says "instead shuffle it into its owner's library" while another says "if a card would be put into a graveyard, exile it instead," the controller chooses which to apply first; the other does nothing because the event it was watching no longer occurs [CR 616.1f].

Review: **correct**. Correctly identifies who chooses, explains re-evaluation, and gives a valid conditional example. It now uses bracketed citations to the precise rules for choice and subsequent applicability.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red is not a legal target for a red spell, so it cannot be included in the random selection pool.

**Why:** Protection from red means the permanent "can't be targeted by spells with the stated quality" [CR 702.16b]. When a spell says "target creature chosen at random," the random selection is still a targeting action, and only legal targets may be chosen [CR 601.2c]. The random mechanism determines *which* legal target is picked, not *whether* a target is legal. A creature with protection from red is simply not in the eligible pool.

Review: **correct**. Correctly excludes a creature made illegal by protection from the random target pool. CR 702.16b and CR 601.2c directly support the protection restriction and legal-target requirement.
Reviewer: Codex

Missing reference groups: none

