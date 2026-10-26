# focused-general-v2-2026-10-26-2

Status: **complete** · implementation commit `31e05b08fe647d5cd8dbe29e6f3b7c64c109837d`

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
| Median successful response | 8.18 s |
| p95 successful response | 9.28 s |
| Median first visible answer token | 6.13 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| g01-random-paper-procedure (r1) | 100.0% | correct | 9.28 |
| g02-copy-counters-and-bonuses (r1) | 100.0% | correct | 7.01 |
| g03-fight-and-double-strike (r1) | 100.0% | correct | 5.30 |
| g04-replacement-order-general (r1) | 100.0% | correct | 8.18 |
| g05-protection-and-random-target (r1) | 50.0% | correct | 8.87 |

## Answers and review notes

### g01-random-paper-procedure / repetition 1

How does an instruction to do something randomly work in paper Magic? What should we physically do?

**Ruling:** In paper Magic, when an effect instructs a player to do something randomly, that player must use a method that gives each eligible option an equal chance of being selected. The eligible pool is determined by the card or effect's text (e.g., "randomly choose one of your creatures" means only your creatures are in the pool).

**Why:** The standard physical methods are: (1) write each eligible option on an identical slip, shuffle, and draw one; or (2) use a die with results evenly mapped to the options (rerolling any result that doesn't map to an option). For die-roll game actions specifically in tournaments, any method that simulates the roll is acceptable as long as every result has an equal chance of occurring [MTR 3.9]. The key requirement across all methods is equal probability for each eligible option — sequential coin flips over more than two options would violate this because they produce unequal probabilities.

Review: **correct**. Correctly gives equal-chance methods, limits MTR 3.9 to die-roll actions, and states random targets must be legal.
Reviewer: Codex

Missing reference groups: none

### g02-copy-counters-and-bonuses / repetition 1

When a creature copies another creature, does it copy the counters and a +2/+2 bonus from an Aura on that creature?

**Ruling:** No. A copy does not acquire counters on the original creature, nor does it acquire a +2/+2 bonus from an Aura (or any other continuous effect) on that creature.

**Why:** When copying an object, the copy acquires only the copiable values—those derived from the text printed on the object, as modified by other copy effects, face-down status, and "as it enters" abilities that set power and toughness. Other effects (including type-changing and text-changing effects), status, counters, and stickers are explicitly not copied [CR 707.2]. A +2/+2 from an Aura is a continuous effect, not a copiable value, so it does not transfer to the copy.

Review: **correct**. Correctly distinguishes copiable values from counters and the Aura’s continuous effect.
Reviewer: Codex

Missing reference groups: none

### g03-fight-and-double-strike / repetition 1

Does double strike make a creature deal damage twice when it fights another creature?

**Ruling:** No. Double strike does not cause a creature to deal damage twice when it fights another creature.

**Why:** Double strike is a static ability that modifies the rules for the combat damage step [CR 702.4a]. The damage dealt when a creature fights is explicitly not combat damage [CR 701.14d], so double strike has no effect on it. A creature that fights deals damage equal to its power once, as stated in the fight rule [CR 701.14a].

Review: **correct**. Correctly explains fight damage is not combat damage and double strike does not add a second event.
Reviewer: Codex

Missing reference groups: none

### g04-replacement-order-general / repetition 1

Two replacement effects apply to the same event. Who chooses which to apply first, and do they both automatically happen?

**Ruling:** The affected object's controller (or its owner if it has no controller) or the affected player chooses which replacement effect to apply first. They do not both automatically happen—after one is applied, the process is repeated, but only effects that are still applicable to the modified event are considered.

**Why:** [CR 616.1] establishes that the affected player (or controller/owner) makes the choice. [CR 616.1f] states that once the chosen effect is applied, the process repeats "taking into account only replacement or prevention effects that would now be applicable," meaning the second effect may no longer apply if the first one changed the event. Certain categories have mandatory priority (e.g., self-replacement effects must be chosen first per [CR 616.1a]), but among effects of the same category, the player chooses freely.

Review: **correct**. Correctly identifies who chooses and that applicability is reevaluated after applying one effect.
Reviewer: Codex

Missing reference groups: none

### g05-protection-and-random-target / repetition 1

A red spell says “target creature chosen at random.” Could a creature with protection from red be selected?

**Ruling:** No. A creature with protection from red is not a legal target for a red spell, so it cannot be included in the random selection pool.

**Why:** Protection from red means the creature can't be targeted by red spells [CR 702.16b]. When choosing targets (including randomly), the player must choose an appropriate legal target [CR 601.2c]. Since the protected creature is not a legal target for that red spell, it is excluded from the pool of creatures that can be randomly selected.

Review: **correct**. Correct; protection makes the creature an illegal target and random selection does not bypass legality.
Reviewer: Codex

Missing reference groups: CR 115.2

