# focused-general-v2-2026-10-26-3

Status: **complete** · implementation commit `1ce5d2185b8bed03fdb7e154914bb2778fd96134`

Suite `general-questions-v2` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 5/5 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 5/5 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 90.0% |
| Cases retrieving every expected evidence group | 4/5 |
| Answers with citations | 5/5 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 5/5 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 8.39 s |
| p95 successful response | 8.79 s |
| Median first visible answer token | 6.03 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | correct | 8.42 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 6.23 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 5.92 |
| g04-replacement-order-general (r1) | 100.0% | correct | 8.79 |
| g05-protection-and-random-target (r1) | 50.0% | correct | 8.39 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** The card or effect determines which objects or players are eligible (if it's a random target, only legal targets qualify [CR 115.2]). Each eligible option must have an equal chance of being selected. Physically, use a method that gives every option an equal probability: shuffled identical slips of paper (one per option) works for any number of options; a die works if its faces map evenly onto the options (reroll any face that doesn't correspond to an option).

**Why:** MTR 3.9 establishes the tournament standard for die-roll game actions: "any method that simulates the roll is acceptable if every result has an equal chance of occurring" [MTR 3.9]. The same equal-chance principle applies to any random selection in paper play. Avoid methods that give some options more chance than others (e.g., sequential coin flips for more than two options, or dice with clustered values like spindown life counters) [MTR 3.9].

Review: **correct**. Correctly gives fair physical methods, distinguishes MTR 3.9 die-roll guidance, and states legal-target pool restriction.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A copy does not acquire counters on the original creature, nor does it acquire a +2/+2 bonus from an Aura (or any other effect) on that creature.

**Why:** When copying an object, the copy acquires only the copiable values derived from the text printed on the object (as modified by other copy effects, face-down status, and "as . . . enters" abilities that set power and toughness). Other effects, status, counters, and stickers are explicitly not copied [CR 707.2]. A +2/+2 from an Aura is an "other effect" and counters are separately listed as not copied, so neither transfers to the copy.

Review: **correct**. Correctly distinguishes copiable values from counters and the Aura’s continuous effect.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights.

**Why:** Double strike is a static ability that modifies the rules for the combat damage step [CR 702.4a]. Fight damage is explicitly not combat damage [CR 701.14d], and the fight action simply has each creature deal damage equal to its power to the other [CR 701.14a]. Since double strike only applies during the combat damage step, it has no effect on fight damage.

Review: **correct**. Correctly explains fight damage is not combat damage and double strike does not add a second event.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or its owner if it has no controller), or the affected player, chooses which replacement effect to apply first. They do not both automatically happen — after one is applied, the process is repeated, but only effects that are still applicable to the modified event are considered; the other may do nothing.

**Why:** [CR 616.1] establishes that the affected player or object's controller makes the choice, following a priority order (self-replacement effects first, then control-modifying, then copy, then back-face, then any remaining). [CR 616.1f] states that once the chosen effect is applied, the process repeats "taking into account only replacement or prevention effects that would now be applicable," meaning the second effect may no longer apply to the modified event.

Review: **correct**. Correctly identifies the chooser and explains that applicability is reevaluated after the first effect.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red is not a legal target for a red spell, so it cannot be included in the random selection pool.

**Why:** Protection from red means the creature can't be targeted by red spells [CR 702.16b]. The "chosen at random" mechanism determines *which* legal target is selected, but it doesn't expand the pool to include objects that aren't legal targets. Only creatures that are legal targets for that red spell belong in the random pool.

Review: **correct**. Correct; protection makes the creature illegal to target and random selection does not bypass legality.
Reviewer: Codex

Missing reference groups: CR 115.2

