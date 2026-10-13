# mechanics-v1-seed42

Status: **complete** · implementation commit `8624f5228f36611fb958408704f51bae59b0fc60`

Suite `mechanics-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 14/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 48.3% |
| Cases retrieving every expected evidence group | 9/20 |
| Answers with citations | 16/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 1 |
| Reviewed citation-support failures | 4 |
| Reviewed fully correct | 14/20 reviewed |
| Reviewed accuracy | 70.0% |
| Mean reviewed rubric score | 79.2% |
| Median successful response | 7.31 s |
| p95 successful response | 14.24 s |
| Median first visible answer token | 6.04 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| m01-poison-threshold (r1) | 0.0% | partial | 14.24 |
| m02-x-on-stack (r1) | 0.0% | correct | 10.88 |
| m03-x-outside-stack (r1) | 0.0% | abstained | 10.19 |
| m04-hybrid-mana-value (r1) | 0.0% | correct | 12.10 |
| m05-loyalty-stack-window (r1) | 0.0% | correct | 5.45 |
| m06-new-planeswalker-activation (r1) | 0.0% | correct | 6.81 |
| m07-loyalty-limit-permanent (r1) | 100.0% | correct | 6.54 |
| m08-loyalty-cost-and-source (r1) | 66.7% | abstained | 14.25 |
| m09-siege-protector (r1) | 100.0% | correct | 6.62 |
| m10-siege-last-counter (r1) | 100.0% | correct | 10.21 |
| m11-monarch-combat-trigger (r1) | 100.0% | correct | 8.14 |
| m12-monarch-draw-trigger (r1) | 100.0% | correct | 8.90 |
| m13-initiative-multiple-damage (r1) | 0.0% | abstained | 4.74 |
| m14-retake-initiative (r1) | 0.0% | abstained | 7.18 |
| m15-phased-out-token (r1) | 100.0% | correct | 7.43 |
| m16-phased-out-board-wipe (r1) | 100.0% | correct | 5.21 |
| m17-regeneration-shield (r1) | 0.0% | correct | 6.78 |
| m18-extra-turn-order (r1) | 100.0% | correct | 5.03 |
| m19-land-not-a-spell (r1) | 100.0% | correct | 5.84 |
| m20-copy-not-cast (r1) | 0.0% | abstained | 13.16 |

## Answers and review notes

### m01-poison-threshold / repetition 1

I have nine poison counters. A creature deals combat damage to me that gives me one more poison counter. Does the game end the instant I reach ten, or when does the loss happen?

**Ruling:** The loss is a state-based action, not something that happens the instant the counter is added. It is checked the next time a player would receive priority, which in practice is immediately after the poisonous trigger resolves.

**Why:** [CR 904.13c] explicitly states that a player with ten or more poison counters losing the game is a state-based action. [CR 117.2d] states that state-based actions are dealt with before a player would receive priority. So after the trigger resolves and the 10th counter is added, the player loses before anyone gets a chance to act.

Review: **partial**. The timing and threshold are right, but the answer cites CR 904.13c, an Archenemy rule, as the poison-loss rule. CR 117.2d supports the state-based-action timing; the cited threshold rule is not appropriate.
Reviewer: Codex

Missing reference groups: CR 104.3d

### m02-x-on-stack / repetition 1

A spell has mana cost {X}{2}{R}. I cast it choosing X=4. What is its mana value while it is on the stack?

**Ruling:** Its mana value is 7.

**Why:** While the spell is on the stack, X equals the announced value of 4 [CR 107.3a]. The mana cost is therefore {4}{2}{R}, and the mana value is the sum of the mana values of those symbols: 4 + 2 + 1 = 7.

Review: **correct**. The X value and total are correct. CR 107.3a supports the announced X value; seed 42 also shows the correct red mana value in its calculation.
Reviewer: Codex

Missing reference groups: CR 202.3, CR 202.3e

### m03-x-outside-stack / repetition 1

A permanent has mana cost {X}{G} and is on the battlefield with several counters on it. What is its mana value?

The supplied reference excerpts do not contain the rule that defines how X is treated when calculating mana value (CR 202.2d, which states X is treated as 0). Without that rule in the references, I cannot cite a supporting source for the answer.

**What is missing:** The rule establishing that X is treated as 0 when determining mana value (CR 202.2d). If you can supply that excerpt, I can confirm the ruling with a proper citation.

Review: **abstained**. The answer gives the correct rule number but abstains instead of answering that mana value is 1 and counters do not affect it.
Reviewer: Codex

Missing reference groups: CR 202.3, CR 202.3e

### m04-hybrid-mana-value / repetition 1

A card has mana cost {2/W}{2/W}{1}. What is its mana value?

**Ruling:** The mana value is **5**.

**Why:** Each hybrid mana symbol {2/W} contributes its generic number (2) to the mana value, and the {1} contributes 1, for a total of 2 + 2 + 1 = 5. The specific rule defining how hybrid symbols are counted toward mana value is not included in the provided reference excerpts, but this is the standard calculation per the comprehensive rules.

Review: **correct**. The numerical answer 5 is correct and both criteria are satisfied. It acknowledges the hybrid-symbol rule is absent from the retrieved excerpts; it provides no supporting citation.
Reviewer: Codex

Missing reference groups: CR 202.3f

### m05-loyalty-stack-window / repetition 1

It is my main phase and I have priority, but an opponent’s instant is still on the stack. May I activate a loyalty ability of my planeswalker in response?

Ruling: No. You may not activate a loyalty ability while any spell or ability is on the stack.

Why: Rule 113.5 requires that "the stack is empty" as a condition for activating a loyalty ability, in addition to having priority during a main phase of your turn. Since your opponent's instant is still on the stack, that condition is not met. [CR 113.5]

Review: **correct**. Correctly applies the empty-stack, main-phase, active-turn timing condition; cited CR 113.5 supports the ruling.
Reviewer: Codex

Missing reference groups: CR 606.3

### m06-new-planeswalker-activation / repetition 1

I cast a planeswalker during my first main phase. After it resolves and the stack is empty, may I activate one of its loyalty abilities this turn if I have not activated one of its loyalty abilities yet?

Ruling: Yes, you may activate one of its loyalty abilities this turn.

Why: After the planeswalker spell resolves, the active player receives priority [CR 117.3b]. A loyalty ability may be activated any time you have priority and the stack is empty during a main phase of your turn, provided none of that permanent's loyalty abilities have been activated that turn [CR 306.5d]. All those conditions are met in your scenario.

Review: **correct**. Correctly explains priority after resolution and that summoning sickness does not restrict loyalty abilities; cited rules support the answer.
Reviewer: Codex

Missing reference groups: CR 606.3

### m07-loyalty-limit-permanent / repetition 1

I activated a +1 loyalty ability of one planeswalker earlier this turn. After it resolves, may I activate a different loyalty ability of that same planeswalker? What about a second planeswalker I control?

**Ruling:** No, you may not activate another loyalty ability of that same planeswalker this turn. Yes, you may activate a loyalty ability of a different planeswalker you control.

**Why:** The once-per-turn restriction on loyalty abilities is per permanent, not per player. Rule 606.3 states that a player may activate a loyalty ability of a permanent they control "only if no player has previously activated a loyalty ability of that permanent that turn" [CR 606.3]. Since the restriction is tied to the specific permanent, activating one loyalty ability of a given planeswalker blocks all other loyalty abilities of that same planeswalker for the rest of the turn, but does not affect any other planeswalker.

Review: **correct**. Correctly states the once-per-turn restriction applies to the individual permanent; cited rules support the distinction.
Reviewer: Codex

Missing reference groups: none

### m08-loyalty-cost-and-source / repetition 1

My planeswalker has exactly three loyalty counters. I activate an ability with a −3 cost. Can I wait until it resolves to remove the counters, and does the ability still resolve if the planeswalker is put into the graveyard before the ability resolves?

Ruling: No, you cannot wait until resolution to remove the counters. The loyalty counters are removed as part of the cost to activate the ability, so they are gone before the ability even hits the stack.

Why: [CR 606.4] establishes that the cost to activate a loyalty ability is to put on or remove the specified number of loyalty counters. Costs are paid as part of the activation process, not at resolution.

Regarding your second question (whether the ability still resolves if the planeswalker leaves the battlefield), the provided reference excerpts do not contain the rule that addresses whether an ability on the stack resolves independently of its source. I cannot confirm or deny that part without a supporting citation.

Review: **abstained**. Correctly says counters are paid as an activation cost. It then abstains on whether the ability survives removal of its source, so criteria 2 and 3 are not established.
Reviewer: Codex

Missing reference groups: CR 113.7a

### m09-siege-protector / repetition 1

I control a Battle — Siege in a two-opponent game. As it enters, may I choose myself as its protector, or must I choose one of my opponents?

**Ruling:** You must choose one of your opponents as the Siege's protector. You cannot choose yourself.

**Why:** Rule 310.12a explicitly states that a Siege's controller "must choose its protector from among their opponents" and that "only an opponent of a Siege's controller can be its protector" [CR 310.12a]. This is a restriction on the general rule that a battle's controller chooses a player to be its protector [CR 310.9a].

Review: **correct**. Correctly says the protector must be an opponent of the Siege controller; cited CR 310.12a supports this.
Reviewer: Codex

Missing reference groups: none

### m10-siege-last-counter / repetition 1

The last defense counter is removed from a Siege. Does it transform immediately as part of removing the counter, or does an ability trigger? What happens when that ability resolves?

**Ruling:** Removing the last defense counter from a Siege triggers its intrinsic ability; it does not transform immediately. When that ability resolves, the Siege is exiled, and then its controller may cast it transformed without paying its mana cost.

**Why:** The intrinsic ability is written as a triggered ability ("When the last defense counter is removed…"), so it triggers and goes on the stack like any other triggered ability [CR 310.12b] [CR 603.2] [CR 603.3]. Because the ability has triggered and is on the stack, the state-based action that would put a Siege with 0 defense into its owner's graveyard does not apply [CR 310.7]. Upon resolution, the Siege is exiled and the controller gets the option to cast it transformed for free [CR 310.12b].

Review: **correct**. Correctly identifies a triggered ability and the exile-then-cast effect; cited Siege rules support the timing and the zero-defense exception.
Reviewer: Codex

Missing reference groups: none

### m11-monarch-combat-trigger / repetition 1

A creature deals combat damage to the current monarch. Does its controller become the monarch immediately as damage is dealt, or only after a triggered ability resolves?

**Ruling:** The controller becomes the monarch when the triggered ability resolves, not immediately when the damage is dealt.

**Why:** The monarch rule is implemented as a triggered ability with the text "Whenever a creature deals combat damage to the monarch, its controller becomes the monarch" [CR 725.2]. Triggered abilities go on the stack and resolve as normal [CR 603.3], so the change of monarch occurs at resolution, not at the moment damage is dealt.

Review: **correct**. Correctly distinguishes the combat-damage trigger from the later change of monarch on resolution; cited rules support the answer.
Reviewer: Codex

Missing reference groups: none

### m12-monarch-draw-trigger / repetition 1

Alice is the monarch when her end step begins, so the monarch draw ability triggers. Before it resolves, an effect makes Bob the monarch. Does Alice’s already-triggered ability still make her draw a card?

Ruling: Yes, Alice still draws a card.

Why: The monarch draw ability is controlled by the player who was the monarch at the time it triggered, and its effect is "that player draws a card" — referring to the monarch at the moment of triggering, not at resolution. [CR 725.2] The ability is already on the stack with a fixed effect; a later change in who the monarch is does not alter what the ability does when it resolves.

Review: **correct**. Correctly says the pending monarch draw trigger still makes Alice draw after the monarch changes; cited rules support the result.
Reviewer: Codex

Missing reference groups: none

### m13-initiative-multiple-damage / repetition 1

I have the initiative. During one combat damage event, two creatures controlled by Bob each deal combat damage to me. How many times does the damage ability trigger, and what happens if it resolves?

Need details: What is the name or text of the "damage ability" you're referring to? Please attach the card using card search or [[Exact Card Name]] so I can determine how it interacts with multiple damage sources in a single combat damage event.

Review: **abstained**. The fully specified scenario is answerable from the rules. The response requests the card text instead of answering the trigger count and initiative result.
Reviewer: Codex

Missing reference groups: CR 726.2

### m14-retake-initiative / repetition 1

I already have the initiative, and an effect instructs me to take the initiative. Do I get a second initiative designation, and does anything trigger?

Need details: The supplied reference excerpts do not contain any rules governing the "initiative" designation. I can only answer based on the provided sources. Could you confirm which card or effect is instructing you to "take the initiative," and is there a specific rule section (e.g., a rule number like 725.x) that defines the initiative designation that you'd like me to work from?

Review: **abstained**. The response confuses initiative rules with monarch rules or asks for more context despite a specified initiative scenario. It does not state that no new designation is created while the initiative-taking trigger still occurs.
Reviewer: Codex

Missing reference groups: CR 726.5, CR 726.2

### m15-phased-out-token / repetition 1

A creature token with counters on it phases out. Does it leave the battlefield, cease to exist, or cause leaves/enters-the-battlefield abilities to trigger?

**Ruling:** The token does not leave the battlefield, does not cease to exist, and does not cause any leaves-the-battlefield or enters-the-battlefield abilities to trigger.

**Why:** The phasing event does not cause a permanent to change zones or control, and zone-change triggers do not trigger when a permanent phases in or out [CR 702.26d]. Tokens continue to exist on the battlefield while phased out, and counters remain on them [CR 702.26d]. A phased-out permanent is merely treated as though it does not exist for most game interactions [CR 702.26b], but it has not actually left the battlefield.

Review: **correct**. Correctly explains that phasing is not a zone change, the token persists, and counters remain; cited CR 702.26 supports this.
Reviewer: Codex

Missing reference groups: none

### m16-phased-out-board-wipe / repetition 1

A phased-out creature is on the battlefield in the game’s history. A spell says “Destroy all creatures.” Is that phased-out creature destroyed?

Ruling: No, the phased-out creature is not destroyed.

Why: A phased-out permanent is treated as though it does not exist and can't be affected by anything else in the game, unless a rule or effect specifically mentions phased-out permanents [CR 702.26b]. The example in that rule explicitly states that a phased-out creature is not destroyed by a spell that says "Destroy all creatures" [CR 702.26b].

Review: **correct**. Correctly explains that a phased-out permanent is unaffected by an ordinary destroy-all effect; cited CR 702.26 supports this.
Reviewer: Codex

Missing reference groups: none

### m17-regeneration-shield / repetition 1

An attacking creature has a regeneration shield. It would be destroyed by lethal damage. What does the shield do?

**Ruling:** The regeneration shield replaces the destruction. Instead of being destroyed, the creature has all damage marked on it removed, is tapped by its controller, and is removed from combat.

**Why:** Regeneration is a destruction-replacement effect that applies the next time the permanent would be destroyed that turn [CR 614.8]. When it applies, all damage marked on the creature is removed, its controller taps it, and if it's an attacking or blocking creature, it is removed from combat [CR 614.8]. The state-based action that would destroy it for lethal damage is the event that regeneration replaces [CR 704.5g].

Review: **correct**. Correctly describes the replacement result: clear damage, tap, and remove from combat; cited regeneration rules support it.
Reviewer: Codex

Missing reference groups: CR 701.19a

### m18-extra-turn-order / repetition 1

Two extra turns are created for the same player after the current turn. First one effect creates an extra turn; later another effect creates a second extra turn. Which extra turn is taken first?

Ruling: The second extra turn (the most recently created one) is taken first.

Why: Rule 500.7 explicitly states that "the most recently created turn will be taken first." Since the second effect created its extra turn after the first, it is the most recently created and therefore occurs before the first extra turn. [CR 500.7]

Review: **correct**. Correctly states that the most recently created extra turn is taken first; cited CR 500.7 supports it.
Reviewer: Codex

Missing reference groups: none

### m19-land-not-a-spell / repetition 1

I have priority in my main phase with an empty stack and play a land from my hand. Does the land go on the stack, and can my opponent respond to the land play with an instant?

**Ruling:** No, the land does not go on the stack, and your opponent cannot respond with an instant.

**Why:** Playing a land is a special action that doesn't use the stack; the player simply puts the land onto the battlefield [CR 305.1]. Since neither the land nor the action of playing it is a spell or ability, players can't respond to it with instants or activated abilities [CR 505.6b]. Special actions happen immediately [CR 405.6d].

Review: **correct**. Correctly identifies playing a land as a special action that does not use the stack; cited rules support the no-response result.
Reviewer: Codex

Missing reference groups: none

### m20-copy-not-cast / repetition 1

An effect copies a modal instant on the stack and says I may choose new targets for the copy. Does the copy count as being cast for “whenever you cast” abilities? Can I choose a different mode as well as new targets?

**Ruling:**

1. **Does the copy count as being cast?** The supplied reference excerpts do not contain the rule that addresses whether a copy of a spell is considered "cast." I cannot confirm or deny this based on the provided sources.

2. **Can you choose a different mode?** No. A copy of a modal spell copies the mode(s) chosen for the original, and the controller of the copy cannot choose a different mode. Additionally, an effect that allows choosing new targets for a modal spell does not allow changing its mode.

**Why:**

Rule 700.2g states that a copy of a modal spell copies the mode(s) chosen for it and the controller of the copy can't choose a different mode [CR 700.2g]. Rule 115.8 and 700.2f both confirm that changing a modal spell's target does not allow changing its mode [CR 115.8] [CR 700.2f]. For the first question, the excerpts lack the rule governing whether a copied spell is considered "cast" (typically rule 601.2i or related copy rules); please supply that excerpt or I can address it if you confirm the specific card involved.

Review: **abstained**. Correctly explains that the mode is copied and cannot be changed, but abstains on whether copying casts the copy. That part is answerable from the rules and is required by the first criterion.
Reviewer: Codex

Missing reference groups: CR 707.10, CR 707.10c

