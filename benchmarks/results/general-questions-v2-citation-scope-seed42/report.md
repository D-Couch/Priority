# general-questions-v2-citation-scope-seed42

Status: **complete** · implementation commit `b8511153106a2323461f5c28ec67bcefe4928684`

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
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 5/5 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 7.46 s |
| p95 successful response | 9.68 s |
| Median first visible answer token | 6.08 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | correct | 9.68 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 6.63 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 5.30 |
| g04-replacement-order-general (r1) | 100.0% | correct | 9.37 |
| g05-protection-and-random-target (r1) | 100.0% | correct | 7.46 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** The card or effect defines the eligible pool of options, and players must use a method that gives each eligible option an equal chance of being selected.

**Why:** For die-roll game actions specifically, any method that simulates the roll is acceptable as long as every result has an equal chance of occurring (e.g., a standard d6, or mapping a die's faces evenly to the available choices) [MTR 3.9]. For other random choices (such as "choose one of these at random"), the same equal-chance principle applies in practice—common paper methods include writing each option on a slip and drawing one, or mapping a die's faces evenly to the options and rerolling any face that doesn't correspond to an eligible choice. The eligible pool always comes from the card's text, not from the randomizer itself.

Review: **correct**. Direct practical answer with fair methods, distinguishes the die-roll-only MTR guidance, and includes only legal targets in a random target pool. Citations support the claims.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A copy does not acquire counters on the original creature, nor does it acquire a +2/+2 (or any other) bonus from an Aura or other noncopy effect on that creature.

**Why:** Rule 707.2 explicitly states that "counters" are not copied, and that "other effects (including type-changing and text-changing effects)" are not copied. A +2/+2 from an Aura is a noncopy effect affecting the permanent, so it does not transfer to the copy. Rule 707.4 reinforces this by noting that when a permanent becomes a copy of something else, "this also doesn't change any noncopy effects presently affecting the permanent." [CR 707.2] [CR 707.4]

Review: **correct**. Correct general copy rule; counters and an Aura’s continuous bonus are not copied. CR 707.2 and 707.4 support the answer.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights another creature.

**Why:** Double strike is a static ability that modifies the rules for the *combat damage step* specifically [CR 702.4a]. The "fight" action is a separate mechanic where each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Since double strike only applies during combat damage steps, it has no effect on fight actions. A creature with double strike that fights another creature deals damage equal to its power once, just as it would without double strike.

Review: **correct**. Correctly explains fight damage is once per creature and not combat damage, so double strike has no effect.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or its owner if it has no controller), or the affected player, chooses which replacement effect to apply first. They do not both automatically happen—the player picks one, applies it, then checks whether the other is still applicable to the *modified* event. If the modified event no longer matches the second effect's trigger, that effect does nothing.

**Why:** Rule 616.1 establishes that the affected player makes the choice, and rule 616.1f states the process repeats only for effects that are *still applicable* after the first one is applied. If the first replacement changes the event so the second no longer matches, the second simply has no event to replace and does nothing [CR 614.7]. There is also a priority order: self-replacement effects must be chosen first, then effects modifying control, then copy effects, then back-face-up effects, and finally any remaining applicable effects may be chosen in any order [CR 616.1a–e].

Review: **correct**. The answer accurately describes affected-player choice and sequential applicability. However, it mentions Rules 616.1 and 616.1f only in unlinked prose and cites CR 614.7 for the final statement. The cited excerpt does not support who chooses or the repeated process; those central claims need bracketed [CR 616.1] and [CR 616.1f] citations.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red cannot be selected, even by a random choice.

**Why:** Protection from red means the creature can't be targeted by red spells [CR 702.16b]. When a spell requires a target, only legal targets may be chosen [CR 601.2c]. "Chosen at random" simply determines *which* legal target is picked from the eligible pool; it does not expand that pool to include illegal targets. So the creature with protection from red is excluded from the random selection entirely.

Review: **correct**. Correctly excludes a creature made illegal by protection and cites both CR 702.16b and the targeting rule. No unrelated tournament-randomization claim was added.
Reviewer: Codex

Missing reference groups: none

