# focused-general-v2-2026-10-26-5

Status: **complete** · implementation commit `355b3487afbb597b105185bafea0c7cc76de6ee8`

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
| Median successful response | 9.20 s |
| p95 successful response | 11.16 s |
| Median first visible answer token | 7.57 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | correct | 8.59 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 11.16 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 6.43 |
| g04-replacement-order-general (r1) | 100.0% | correct | 9.67 |
| g05-protection-and-random-target (r1) | 100.0% | correct | 9.20 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** Whatever method you use to resolve a random instruction in paper play, every eligible option must have an equal chance of being selected. The card or effect determines which objects or players are in the eligible pool; if the random choice is a target, only legal targets belong in that pool [CR 115.2].

**Why:** In tournaments, MTR 3.9 specifically addresses die-roll game actions and states that any method that simulates the roll is acceptable as long as every result has an equal chance of occurring [MTR 3.9]. The same equal-chance principle applies to any random instruction in casual or paper play. Practical methods include: shuffling identical slips of paper (one per eligible option) and drawing one; using a die with results evenly mapped to the options (rerolling any result that doesn't map to an option); or flipping a coin when there are exactly two options. Avoid methods that give some options more chance than others, such as a sequence of coin flips for more than two options.

Review: **correct**. Gives equal-chance physical methods, scopes MTR 3.9 to tournament die-roll guidance, and notes random targets must be legal.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A copy does not acquire counters on the original creature, nor does it acquire a +2/+2 bonus from an Aura attached to that creature.

**Why:** When copying an object, the copy acquires only its copiable values — those derived from the text printed on the object (name, mana cost, color, type, rules text, power, toughness, loyalty), as modified by other copy effects and certain "as it enters" abilities. The rule explicitly states that "other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied" [CR 707.2]. A +2/+2 from an Aura is an external continuous effect modifying the object's characteristics, not a copiable value, so it is not transferred to the copy. The same principle is illustrated in the Giant Growth example, where a creature that becomes a copy of another still retains its own +3/+3 from Giant Growth as a separate effect [CR 707.4].

Review: **correct**. Correctly distinguishes copiable values from counters and external Aura effects under CR 707.2.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike only modifies the combat damage step; it has no effect on the "fight" action.

**Why:** Double strike is defined as a static ability that modifies the rules for the combat damage step [CR 702.4a]. The fight action is a separate mechanic where each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Since double strike only applies during combat damage steps, it does not cause a creature to deal damage a second time when it fights.

Review: **correct**. Correctly explains fight damage is not combat damage and each creature deals damage once.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or the affected player, if the object has no controller) chooses which replacement effect to apply first. They do not both automatically happen — once the first effect is applied, the process is repeated, but the second effect only applies if it is still applicable to the modified event.

**Why:** [CR 616.1] establishes that the affected object's controller or affected player makes the choice. [CR 616.1f] states that after the chosen effect is applied, the process is repeated "taking into account only replacement or prevention effects that would now be applicable," and the example in that rule shows a case where the second effect simply does nothing because the event it was watching for no longer occurs. This is consistent with [CR 614.6], which says a replaced event never happens, and [CR 614.7], which says a replacement effect whose event never happens simply does nothing.

Review: **correct**. Correctly identifies the chooser and explains that effects are reevaluated sequentially rather than automatically all applying.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red cannot be selected because it is not a legal target for a red spell.

**Why:** Protection from red means the creature can't be targeted by red spells [CR 702.16b]. Since the spell is red, that creature is an illegal target and must be excluded from the random selection pool. Only legal targets may be included when a spell randomly selects a target [CR 115.2].

Review: **correct**. Correctly excludes an illegal target from random target selection; randomness does not bypass protection.
Reviewer: Codex

Missing reference groups: none

