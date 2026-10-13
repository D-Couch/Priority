# general-questions-v2-seed42

Status: **complete** · implementation commit `493941e021cda12f3d38948e50b3b260dd4be1b1`

Suite `general-questions-v2` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 5/5 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 4/5 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 90.0% |
| Cases retrieving every expected evidence group | 4/5 |
| Answers with citations | 5/5 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 1 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 4/5 reviewed |
| Reviewed accuracy | 80.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 8.02 s |
| p95 successful response | 15.87 s |
| Median first visible answer token | 5.75 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | correct | 6.99 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 8.02 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 6.83 |
| g04-replacement-order-general (r1) | 100.0% | correct | 9.83 |
| g05-protection-and-random-target (r1) | 50.0% | partial | 15.87 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** The card or effect defines the eligible pool of options, and you must use a method that gives each eligible option an equal chance of being selected.

**Why:** If the random choice is a target, only legal targets belong in the pool [CR 115.2] [CR 601.2c]. For die-roll game actions in tournaments, any method that simulates the roll is acceptable as long as every result has an equal chance [MTR 3.9]. For other random choices (e.g., "choose one of these cards at random"), write each eligible option on a separate slip of paper, shuffle, and draw one — or map a die evenly to the options and reroll any result that doesn't correspond to an eligible choice. The key principle is equal probability across the eligible set, not a specific physical object.

Review: **correct**. Directly answers with fair physical methods, scopes MTR 3.9 to die rolls, and limits random targets to legal targets. Each citation is present and supports the associated claim.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A creature that copies another creature does not copy counters on it, nor does it copy a +2/+2 bonus from an Aura (or any other noncopy effect).

**Why:** When copying an object, the copy acquires only the copiable values derived from the text printed on the object (name, mana cost, color, types, rules text, power, toughness, loyalty), as modified by other copy effects and certain "as it enters" abilities. "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." [CR 707.2] An Aura's +2/+2 is a continuous effect applied to the original creature, not part of its printed or copiable values, so the copy enters without it. Similarly, any counters (damage, +1/+1, charge, etc.) on the original are not transferred to the copy. [CR 707.2]

Review: **correct**. Correctly distinguishes copiable values from counters and continuous effects. CR 707.2 directly supports the answer; no exact card name is needed for this general question.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights another creature.

**Why:** Double strike is a static ability that modifies only the combat damage step [CR 702.4a]. The "fight" action is a separate mechanic in which each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Since double strike has no effect outside the combat damage step, a creature with double strike that fights another creature deals its power in damage exactly once, just as it would without the ability.

Review: **correct**. Correctly explains that fight damage occurs once per creature and is not combat damage, so double strike does not add another fight damage event. All three cited rules support the answer.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or its owner if it has no controller), or the affected player, chooses which replacement effect to apply first. They do not both automatically happen—the player picks one, applies it, then checks whether the second is still applicable to the *modified* event. If the modified event no longer triggers the second effect, it simply does nothing.

**Why:** Rule 616.1 assigns the choice to the affected object's controller or the affected player, and rule 616.1f states that after one effect is applied, the process repeats only for effects that are *now* applicable to the resulting event. Because a replaced event "never happens" and a modified event occurs instead [CR 614.6], a second replacement effect that was watching for the original event may find no event to replace and simply does nothing [CR 614.7].

**Example:** If one effect says "If a creature would enter the battlefield, it enters with a +1/+1 counter instead" and another says "If a creature would enter the battlefield, it enters tapped instead," the controller chooses which applies first. If the counter effect is chosen first, the creature enters with a counter; the "enters tapped" effect is then checked against the modified event and still applies (the creature enters tapped *and* with a counter). But if the "enters tapped" effect were chosen first and the counter effect required the creature to enter *untapped* as a condition, the counter effect would no longer be applicable and would do nothing.

Review: **correct**. Correctly identifies the affected player/object controller and explains sequential re-evaluation. CR 616.1/616.1f support the core answer; cited 614.6/614.7 excerpts support the explanation. The hypothetical example is conditional and does not invent a result for the user’s unspecified effects.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red is not a legal target of a red spell, so it cannot be included in the random selection pool.

**Why:** When a spell requires a target, only appropriate (i.e., legal) objects or players may be chosen [CR 601.2c]. Protection from red makes a creature an illegal target of red spells and abilities, so it is excluded from the eligible pool regardless of how the target is selected. The random procedure simply picks from among the creatures that *are* legal targets.

(Note: the specific protection rule, CR 702.16, is not in the supplied excerpts, but the principle that only legal targets may be chosen is established by the targeting rules above.)

Review: **partial**. The ruling is substantively correct and gives a direct general answer, but the response says CR 702.16 is absent. Its only citation is CR 601.2c, which establishes target selection, not that protection from red makes this target illegal. The needed protection rule was not retrieved; this is a retrieval/evidence gap and should not be counted fully correct.
Reviewer: Codex

Missing reference groups: CR 702.16b

