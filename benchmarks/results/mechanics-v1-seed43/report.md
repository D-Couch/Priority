# mechanics-v1-seed43

Status: **complete** · implementation commit `8624f5228f36611fb958408704f51bae59b0fc60`

Suite `mechanics-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [43]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 13/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 48.3% |
| Cases retrieving every expected evidence group | 9/20 |
| Answers with citations | 18/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 3 |
| Reviewed citation-support failures | 2 |
| Reviewed fully correct | 13/20 reviewed |
| Reviewed accuracy | 65.0% |
| Mean reviewed rubric score | 78.3% |
| Median successful response | 7.48 s |
| p95 successful response | 15.90 s |
| Median first visible answer token | 6.20 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| m01-poison-threshold (r1) | 0.0% | correct | 9.05 |
| m02-x-on-stack (r1) | 0.0% | partial | 7.35 |
| m03-x-outside-stack (r1) | 0.0% | abstained | 12.33 |
| m04-hybrid-mana-value (r1) | 0.0% | partial | 16.05 |
| m05-loyalty-stack-window (r1) | 0.0% | correct | 5.52 |
| m06-new-planeswalker-activation (r1) | 0.0% | correct | 7.31 |
| m07-loyalty-limit-permanent (r1) | 100.0% | correct | 7.37 |
| m08-loyalty-cost-and-source (r1) | 66.7% | partial | 15.90 |
| m09-siege-protector (r1) | 100.0% | correct | 6.31 |
| m10-siege-last-counter (r1) | 100.0% | correct | 8.58 |
| m11-monarch-combat-trigger (r1) | 100.0% | correct | 7.63 |
| m12-monarch-draw-trigger (r1) | 100.0% | correct | 10.04 |
| m13-initiative-multiple-damage (r1) | 0.0% | abstained | 4.68 |
| m14-retake-initiative (r1) | 0.0% | abstained | 8.83 |
| m15-phased-out-token (r1) | 100.0% | correct | 7.59 |
| m16-phased-out-board-wipe (r1) | 100.0% | correct | 5.35 |
| m17-regeneration-shield (r1) | 0.0% | correct | 6.57 |
| m18-extra-turn-order (r1) | 100.0% | correct | 5.26 |
| m19-land-not-a-spell (r1) | 100.0% | correct | 5.90 |
| m20-copy-not-cast (r1) | 0.0% | abstained | 14.24 |

## Answers and review notes

### m01-poison-threshold / repetition 1

I have nine poison counters. A creature deals combat damage to me that gives me one more poison counter. Does the game end the instant I reach ten, or when does the loss happen?

**Ruling:** You don't lose the game the instant the counter is applied. Losing due to ten or more poison counters is a state-based action, which is checked when a player would next receive priority.

**Why:** Rule 904.13c explicitly states that having ten or more poison counters causes a player to lose the game and labels it a state-based action [CR 904.13c]. State-based actions are dealt with automatically before a player would receive priority [CR 117.2d]. So the loss is recognized at the next point where the game checks state-based actions (i.e., before the next player is about to get priority), not at the exact moment the counter is added.

Review: **correct**. Correctly places the loss at the next state-based-action check and cites CR 904.13c and 117.2d, which support the threshold and timing.
Reviewer: Codex

Missing reference groups: CR 104.3d

### m02-x-on-stack / repetition 1

A spell has mana cost {X}{2}{R}. I cast it choosing X=4. What is its mana value while it is on the stack?

Ruling: Its mana value is 6.

Why: While the spell is on the stack, X equals the announced value of 4 [CR 107.3a]. The mana cost is therefore {4}{2}{R}, and the mana value is the sum of the numeric values in that cost: 4 + 2 = 6.

Review: **partial**. Correctly substitutes X=4, but computes mana value as 6 by omitting the red symbol, whose mana value is 1. CR 107.3a does not support that incorrect total.
Reviewer: Codex

Missing reference groups: CR 202.3, CR 202.3e

### m03-x-outside-stack / repetition 1

A permanent has mana cost {X}{G} and is on the battlefield with several counters on it. What is its mana value?

Need details: The provided reference excerpts do not include the rule that defines mana value (rule 202.3) or the rule explaining how X in a mana cost is treated for that purpose. I cannot cite a supporting source from the supplied excerpts to confirm the answer. If you can supply the relevant rule text (e.g., rule 202.3 and 107.3), I can give a fully cited ruling.

Review: **abstained**. The answer declines to give the rules-based mana value of 1. X is 0 for mana value outside the stack, and counters do not affect mana value.
Reviewer: Codex

Missing reference groups: CR 202.3, CR 202.3e

### m04-hybrid-mana-value / repetition 1

A card has mana cost {2/W}{2/W}{1}. What is its mana value?

**Ruling:** The mana value is **5**.

**Why:** Each hybrid mana symbol {2/W} contributes its generic number (2) to the mana value, and the {1} contributes 1, for a total of 2 + 2 + 1 = 5. The supplied excerpts confirm that mana value is determined from the mana cost [CR 709.4b], but the specific rule defining how hybrid symbols contribute their generic number to mana value (rule 119.5f) is not included in the reference excerpts provided.

Review: **partial**. The numerical answer is correct, but CR 709.4b concerns split cards and does not support the hybrid-symbol calculation; the answer itself acknowledges that the needed rule was not retrieved.
Reviewer: Codex

Missing reference groups: CR 202.3f

### m05-loyalty-stack-window / repetition 1

It is my main phase and I have priority, but an opponent’s instant is still on the stack. May I activate a loyalty ability of my planeswalker in response?

Ruling: No. You may not activate a loyalty ability while an opponent's instant is on the stack.

Why: A loyalty ability may only be activated "any time [you] have priority and the stack is empty during a main phase of your turn" [CR 113.5]. Since the opponent's instant is still on the stack, the stack is not empty, so the condition is not met.

Review: **correct**. Correctly applies the empty-stack, main-phase, active-turn timing condition; cited CR 113.5 supports the ruling.
Reviewer: Codex

Missing reference groups: CR 606.3

### m06-new-planeswalker-activation / repetition 1

I cast a planeswalker during my first main phase. After it resolves and the stack is empty, may I activate one of its loyalty abilities this turn if I have not activated one of its loyalty abilities yet?

Ruling: Yes. After the planeswalker spell resolves, you receive priority, the stack is empty, it is still your main phase, and you have not activated any of that permanent's loyalty abilities this turn, so all conditions are met.

Why: A player may activate a loyalty ability of a permanent they control any time they have priority and the stack is empty during a main phase of their turn, provided none of that permanent's loyalty abilities have been activated that turn [CR 306.5d]. The active player receives priority after a spell resolves [CR 117.3b], so you have priority at the moment you need it.

Review: **correct**. Correctly explains priority after resolution and that summoning sickness does not restrict loyalty abilities; cited rules support the answer.
Reviewer: Codex

Missing reference groups: CR 606.3

### m07-loyalty-limit-permanent / repetition 1

I activated a +1 loyalty ability of one planeswalker earlier this turn. After it resolves, may I activate a different loyalty ability of that same planeswalker? What about a second planeswalker I control?

**Ruling:** No, you may not activate a different loyalty ability of that same planeswalker this turn. Yes, you may activate a loyalty ability of a second planeswalker you control.

**Why:** The once-per-turn restriction on loyalty abilities is tied to each individual permanent, not to the player. Once any player has activated a loyalty ability of a given planeswalker that turn, no further loyalty abilities of that same permanent may be activated [CR 606.3]. A different planeswalker is a different permanent, so its loyalty abilities remain available [CR 306.5d].

Review: **correct**. Correctly states the once-per-turn restriction applies to the individual permanent; cited rules support the distinction.
Reviewer: Codex

Missing reference groups: none

### m08-loyalty-cost-and-source / repetition 1

My planeswalker has exactly three loyalty counters. I activate an ability with a −3 cost. Can I wait until it resolves to remove the counters, and does the ability still resolve if the planeswalker is put into the graveyard before the ability resolves?

**Ruling:** No, you cannot wait until resolution to remove the counters. The loyalty counters are removed as part of the cost to activate the ability, which happens before the ability is on the stack. Yes, the ability will still resolve even if the planeswalker is put into the graveyard before it resolves, because once an ability is on the stack it is independent of its source.

**Why:** [CR 606.4] states that the cost to activate a loyalty ability is to remove the specified number of loyalty counters, and [CR 606.6] confirms the permanent must have at least that many counters to activate. Costs are paid as part of the activation process, not at resolution. The provided excerpts do not include the specific rule establishing that an ability on the stack resolves independently of its source's continued presence on the battlefield, so I cannot cite a supporting excerpt for that portion.

Review: **partial**. Correctly explains that counters are paid as the activation cost and that removal of the source does not remove the ability. However, the second ruling is explicitly unsupported by the supplied excerpts, so criterion 2 is not supported and the answer makes an unsupported claim.
Reviewer: Codex

Missing reference groups: CR 113.7a

### m09-siege-protector / repetition 1

I control a Battle — Siege in a two-opponent game. As it enters, may I choose myself as its protector, or must I choose one of my opponents?

**Ruling:** You must choose one of your opponents as the Siege's protector. You cannot choose yourself.

**Why:** Rule 310.12a explicitly states that "As a Siege enters the battlefield, its controller must choose its protector from among their opponents. Only an opponent of a Siege's controller can be its protector." [CR 310.12a] This is the specific restriction for Sieges under rule 310.12, which rule 310.9a references when determining which players may be chosen. [CR 310.9a]

Review: **correct**. Correctly says the protector must be an opponent of the Siege controller; cited CR 310.12a supports this.
Reviewer: Codex

Missing reference groups: none

### m10-siege-last-counter / repetition 1

The last defense counter is removed from a Siege. Does it transform immediately as part of removing the counter, or does an ability trigger? What happens when that ability resolves?

**Ruling:** A triggered ability triggers. It is not an immediate transformation. When the ability resolves, the Siege is exiled, and then its controller may cast it transformed without paying its mana cost.

**Why:** The intrinsic ability on Sieges is written as a triggered ability: "When the last defense counter is removed from this permanent, exile it, then you may cast it transformed without paying its mana cost." [CR 310.12b] Because it is a triggered ability, it goes on the stack and resolves at the next opportunity rather than happening as part of the counter removal itself. Additionally, the Siege does not immediately go to the graveyard when its defense reaches 0, because the state-based action that would do so is suspended while it is the source of an ability that has triggered but not yet left the stack. [CR 310.7]

Review: **correct**. Correctly identifies a triggered ability and the exile-then-cast effect; cited Siege rules support the timing and the zero-defense exception.
Reviewer: Codex

Missing reference groups: none

### m11-monarch-combat-trigger / repetition 1

A creature deals combat damage to the current monarch. Does its controller become the monarch immediately as damage is dealt, or only after a triggered ability resolves?

**Ruling:** The controller becomes the monarch when the triggered ability resolves, not immediately when the damage is dealt.

**Why:** The monarch's damage-triggered ability is a triggered ability with the text "Whenever a creature deals combat damage to the monarch, its controller becomes the monarch" [CR 725.2]. Triggered abilities trigger on the event, then go on the stack the next time a player would receive priority, and only take effect when they resolve [CR 603.2] [CR 603.3].

Review: **correct**. Correctly distinguishes the combat-damage trigger from the later change of monarch on resolution; cited rules support the answer.
Reviewer: Codex

Missing reference groups: none

### m12-monarch-draw-trigger / repetition 1

Alice is the monarch when her end step begins, so the monarch draw ability triggers. Before it resolves, an effect makes Bob the monarch. Does Alice’s already-triggered ability still make her draw a card?

Ruling: Yes, Alice still draws a card.

Why: The monarch draw ability is controlled by the player who was the monarch at the time it triggered, and its effect is to make "that player" (i.e., Alice) draw a card [CR 725.2]. Once the ability is on the stack, its effect is fixed; there is no intervening "if" clause or condition that re-checks who is the monarch at resolution [CR 603.4]. Bob becoming the monarch afterward does not alter what the already-triggered ability does.

Review: **correct**. Correctly says the pending monarch draw trigger still makes Alice draw after the monarch changes; cited rules support the result.
Reviewer: Codex

Missing reference groups: none

### m13-initiative-multiple-damage / repetition 1

I have the initiative. During one combat damage event, two creatures controlled by Bob each deal combat damage to me. How many times does the damage ability trigger, and what happens if it resolves?

Need details: What is the specific card or ability you're referring to when you say "the damage ability"? Please provide the card name or its text so I can determine how it interacts with multiple damage sources in a single combat damage event.

Review: **abstained**. The scenario specifies the initiative damage ability sufficiently to answer. The response unnecessarily requests card details and does not give the one-trigger result or the initiative/Undercity consequence.
Reviewer: Codex

Missing reference groups: CR 726.2

### m14-retake-initiative / repetition 1

I already have the initiative, and an effect instructs me to take the initiative. Do I get a second initiative designation, and does anything trigger?

Need details: The reference excerpts provided only cover the **monarch** designation ([CR 725.1]), not the **initiative** designation. Could you clarify whether you're asking about the monarch or the initiative? If it's the initiative, I'd need the relevant rule text or card text to give an accurate ruling.

Review: **abstained**. The response appropriately avoids inventing a monarch ruling, but the scenario specifies initiative and is answerable from CR 726. It abstains instead of answering both criteria.
Reviewer: Codex

Missing reference groups: CR 726.5, CR 726.2

### m15-phased-out-token / repetition 1

A creature token with counters on it phases out. Does it leave the battlefield, cease to exist, or cause leaves/enters-the-battlefield abilities to trigger?

**Ruling:** The token does not leave the battlefield, does not cease to exist, and does not cause any enters- or leaves-the-battlefield abilities to trigger.

**Why:** The phasing event does not cause a permanent to change zones or control, and zone-change triggers do not trigger when a permanent phases in or out [CR 702.26d]. Tokens continue to exist on the battlefield while phased out, and counters remain on them [CR 702.26d]. A phased-out permanent is merely treated as though it does not exist for most game purposes, but it has not actually left the battlefield [CR 702.26b].

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

**Why:** Regeneration is a destruction-replacement effect that applies the next time the permanent would be destroyed that turn [CR 614.8]. When a creature with lethal damage would be destroyed as a state-based action, regeneration can replace that event [CR 704.5g]. Since the creature is attacking, it is also removed from combat [CR 614.8].

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

Ruling: No, the land does not go on the stack, and your opponent cannot respond with an instant.

Why: Playing a land is a special action that doesn't use the stack; the player simply puts the land onto the battlefield. [CR 305.1] Since the land never becomes a spell and the action doesn't use the stack, players can't respond to it with instants or activated abilities. [CR 305.1] [CR 505.6b]

Review: **correct**. Correctly identifies playing a land as a special action that does not use the stack; cited rules support the no-response result.
Reviewer: Codex

Missing reference groups: none

### m20-copy-not-cast / repetition 1

An effect copies a modal instant on the stack and says I may choose new targets for the copy. Does the copy count as being cast for “whenever you cast” abilities? Can I choose a different mode as well as new targets?

**Ruling:**

1. **Does the copy count as being cast?** The supplied reference excerpts do not contain the rule that addresses whether a copy of a spell is considered cast. I cannot confirm or deny this from the provided sources.

2. **Can you choose a different mode?** No. A copy of a modal spell copies the mode(s) chosen for the original, and the controller of the copy cannot choose a different mode.

**Why:**

Rule 700.2g explicitly states that a copy of a modal spell or ability copies the mode(s) chosen for it and the controller of the copy can't choose a different mode [CR 700.2g]. Additionally, rule 700.2f confirms that changing a spell's target can't change its mode [CR 700.2f]. For the first question, the rule governing whether a copied spell is considered "cast" (typically found in rule 707) is not present in the supplied excerpts, so I cannot provide a supported ruling on that point.

Review: **abstained**. Correctly says the copy keeps the original mode and new targets are limited by the copy effect. It abstains on whether the copy was cast, which is answerable from the rules and is required by criterion 1.
Reviewer: Codex

Missing reference groups: CR 707.10, CR 707.10c

