# conditional-general-v2-seed42

Status: **complete** · implementation commit `5abb9f298a24b44994aeaf5ef28b19ecd0b417b0`

Suite `general-questions-v2` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 5/5 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | pending / n/a/0 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 90.0% |
| Cases retrieving every expected evidence group | 4/5 |
| Answers with citations | 5/5 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | pending / n/a |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 0/0 reviewed |
| Reviewed accuracy | pending / n/a |
| Mean reviewed rubric score | pending / n/a |
| Median successful response | 7.52 s |
| p95 successful response | 9.48 s |
| Median first visible answer token | 5.89 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | pending | 8.20 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | pending | 7.52 |
| g03-fight-and-double-strike (r1) | 100.0% | pending | 6.03 |
| g04-replacement-order-general (r1) | 100.0% | pending | 9.48 |
| g05-protection-and-random-target (r1) | 50.0% | pending | 6.47 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** The card or effect determines which objects or players are eligible, and whatever physical method you use must give each eligible option an equal chance of being selected.

**Why:** MTR 3.9 establishes that for a game action using a die roll, any method that simulates the roll is acceptable as long as every result has an equal chance of occurring [MTR 3.9]. In practice, common methods include shuffling identical slips of paper (one per eligible option) and drawing one, or using a die when its faces can be mapped evenly to the options (rerolling any result that doesn't correspond to an eligible option). The eligible pool always comes from the card's text—for example, if an effect says "randomly choose one of your creatures," only your creatures are in the pool. Exact card wording can add restrictions (such as "randomly choose one of the creatures you control that is attacking"), so the specific text defines what's eligible.

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. The copy does not receive the counters, and it does not receive the +2/+2 from the Aura.

**Why:** When copying an object, the copy acquires only the copiable values (name, mana cost, color, types, rules text, power, toughness, loyalty, etc.) as modified by other copy effects and "as it enters" abilities that set power and toughness. Counters, status, and other continuous effects (such as a +2/+2 from an Aura) are explicitly not copied. [CR 707.2]

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights another creature.

**Why:** Double strike is a static ability that modifies the rules for the *combat damage step* specifically [CR 702.4a]. The "fight" action is a separate mechanic where each creature deals damage equal to its power to the other [CR 701.14a], and that damage is explicitly not combat damage [CR 701.14d]. Since double strike only applies during combat damage steps, it has no effect on the fight action.

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or the affected player, if the object has no controller) chooses which replacement effect to apply first. They do **not** both automatically happen. After one is applied, the process repeats with the *modified* event — the second effect only applies if it is still applicable to that modified event. In many cases, applying one effect changes the event enough that the second no longer applies and simply does nothing.

**Why:** [CR 616.1] establishes that the affected player/object controller makes the choice, following a priority order (self-replacement effects first, then control changes, then copy effects, then back-face entries, then any remaining effects). [CR 616.1f] states that once the chosen effect is applied, the process is repeated "taking into account only replacement or prevention effects that would now be applicable," and the example in that rule shows that after one replacement is applied, the other "does nothing" because the modified event no longer meets its condition.

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red cannot be selected, even by a random choice.

**Why:** Protection from red means the creature can't be targeted by red spells [CR 702.16b]. When a spell chooses targets—including randomly—only legal targets may be chosen [CR 601.2c]. The random selection simply picks from the pool of legal targets, and a creature with protection from red is not a legal target for a red spell, so it is excluded from that pool entirely.

Missing reference groups: CR 115.2

