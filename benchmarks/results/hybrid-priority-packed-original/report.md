# hybrid-priority-packed-original

Status: **complete** · implementation commit `2c6a37b3714400d854708ceff1df9aa5eac3b583`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 20/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 96.2% |
| Cases retrieving every expected evidence group | 18/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 20/20 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 10.73 s |
| p95 successful response | 16.82 s |
| Median first visible answer token | 9.51 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.93 |
| 02-hold-priority (r1) | 100.0% | correct | 9.00 |
| 03-illegal-target (r1) | 100.0% | correct | 9.61 |
| 04-partial-targets (r1) | 100.0% | correct | 9.53 |
| 05-trample-indestructible (r1) | 100.0% | correct | 13.22 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 10.07 |
| 07-zero-toughness (r1) | 100.0% | correct | 15.98 |
| 08-commander-dies (r1) | 100.0% | correct | 22.21 |
| 09-commander-tax (r1) | 100.0% | correct | 9.15 |
| 10-rest-in-peace (r1) | 75.0% | correct | 9.46 |
| 11-token-doublers (r1) | 100.0% | correct | 16.82 |
| 12-replacement-choice (r1) | 100.0% | correct | 15.84 |
| 13-apnap (r1) | 100.0% | correct | 11.39 |
| 14-humility-anthem (r1) | 100.0% | correct | 12.78 |
| 15-own-hexproof (r1) | 100.0% | correct | 7.49 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 12.47 |
| 17-token-blink (r1) | 100.0% | correct | 13.67 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 8.84 |
| 19-legend-response (r1) | 50.0% | correct | 12.09 |
| 20-clarify-interaction (r1) | 100.0% | correct | 8.63 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No. You cannot respond to your opponent tapping a basic Forest for mana.

Why: A basic Forest's tap-for-mana ability is an activated mana ability, which doesn't go on the stack and therefore can't be targeted, countered, or otherwise responded to; it resolves immediately after activation [CR 605.3b]. The ability meets all criteria for a mana ability: it requires no target, adds mana to the player's mana pool, isn't a loyalty ability, and doesn't move cards to or from a library [CR 605.1a].

Review: **correct**. Correct activated mana ability resolves immediately without the stack; supported by 605.3b/605.1a.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you receive priority again before your opponent. No, the instant does not resolve immediately; it waits on the stack until both players pass in succession.

Why: When you have priority and cast a spell, you are the first to receive priority again afterward [CR 117.3c]. The spell sits on the stack and only resolves once all players pass in succession without taking any actions in between [CR 405.5] [CR 117.4] [CR 608.1]. Your opponent therefore gets a window to respond before the instant resolves.

Review: **correct**. Correct caster regains priority; all players must pass for resolution; cited priority and stack rules support both.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No. If your creature is destroyed (leaves the battlefield) before Defiant Strike resolves, the target is illegal, the spell doesn't resolve, and you do not draw a card.

Why: A target that is no longer in the zone it was in when targeted is illegal, and if all of a spell's targets are illegal, the spell doesn't resolve and is put into its owner's graveyard [CR 608.2b]. The card-specific ruling confirms this directly: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Correct no draw when only target becomes illegal; 608.2b and card ruling directly support result.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes. The remaining legal creature takes 2 damage.

Why: Because not *all* targets are illegal, the spell resolves normally; only the illegal target is skipped. [CR 608.2b] states that if all targets are illegal the spell doesn't resolve, but "otherwise, the spell or ability will resolve normally," and "illegal targets, if any, won't be affected" while "other parts of the effect for which those targets are not illegal may still affect them." The Plague Spores example in the same rule illustrates this exact partial-illegality outcome.

Review: **correct**. Correct legal remaining target takes damage; 608.2b supports partial legality.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Ruling: Yes. You must assign at least 2 damage to the 2/2 blocker, and you may assign the remaining 4 to the defending player.

Why: Trample requires you to assign "lethal damage" to the blocking creature before assigning excess to the player, and that threshold is based on the creature's toughness, not on whether it will actually be destroyed [CR 702.19b]. Indestructible prevents destruction and the lethal-damage state-based action, but it does not alter the amount of damage that must be assigned under trample [CR 702.12b]. The rule explicitly states that when checking for assigned lethal damage, you do not consider "abilities or effects that might change the amount of damage that's actually dealt," and indestructible is such an ability [CR 702.19b].

Review: **correct**. Correct 2 to indestructible blocker and 4 to player; lethal assignment differs from destruction under trample/indestructible clauses.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

Ruling: You can assign a maximum of 4 damage to the defending player.

Why: Deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for trample purposes [CR 702.2c]. Trample requires you to assign lethal damage to the blocking creature before assigning excess to the player [CR 702.19b]. Since 1 damage is sufficient to satisfy the lethal-damage requirement, the remaining 4 of your 5 total damage can be assigned to the defending player.

Review: **correct**. Correct assign 1 deathtouch damage and 4 trample damage; 702.2c and 702.19b support calculation.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: No. The indestructible 3/3 does not survive. The −3/−3 reduces its toughness to 0, and the state-based action in [CR 704.5f] puts it into its owner's graveyard.

Why: Indestructible means a permanent "can't be destroyed" and specifically ignores the state-based action for lethal damage (rule 704.5g) [CR 702.12b]. However, a creature with toughness 0 or less is *put into its owner's graveyard* by a separate state-based action [CR 704.5f]; that is not "destroying" the creature, so indestructible does not prevent it.

Review: **correct**. Correct: CR 704.5f sends a creature with toughness zero to its owner’s graveyard as a state-based action; indestructible does not prevent this because it is not destruction. The exact exception and indestructible rule are both packed and cited.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

Ruling: Yes to both. You may put your commander into the command zone, and "dies" (leaves-the-battlefield) triggers still fire.

Why: Rule 903.9a makes moving a commander from the graveyard to the command zone a state-based action the owner may take, not a replacement effect, so it applies even when no replacement effect is present [CR 903.9a]. The "dies" trigger condition is met the moment the permanent moves from the battlefield to the graveyard; that zone-change event is not undone by the subsequent state-based action moving it to the command zone [CR 603.6c]. Leaves-the-battlefield triggers "look back in time" to confirm the permanent left the battlefield, so they trigger regardless of where the card ends up afterward [CR 603.10a].

Review: **correct**. Correct commander enters graveyard and dies triggers occur before optional command-zone SBA; 903.9a and leaves-battlefield rules support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax on your next cast from the command zone is {4}.

Why: The tax is "{2} for each previous time the player casting it has cast it from the command zone that game" [CR 903.8]. You have cast it from the command zone twice previously, so the additional cost is 2 × {2} = {4}. The cast from your hand does not count toward the tax, since the rule specifically tracks casts *from the command zone* [CR 903.8].

Review: **correct**. Correct additional tax of four from two prior command-zone casts; hand cast excluded under 903.8.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No. Blood Artist does not trigger.

Why: "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's static replacement effect exiles the creature instead of putting it into a graveyard [C1], so the creature is never put into a graveyard and therefore never "dies." Because the trigger condition ("whenever… another creature dies") is never met, Blood Artist's ability does not trigger [C5].

Review: **correct**. Correct no Blood Artist dies trigger under Rest in Peace; Oracle/ruling and dies definition support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create **4** tokens (1 × 2 × 2). The doublers do **not** loop forever.

Why: Each replacement effect gets only one opportunity to affect the event and does not invoke itself repeatedly [CR 614.5]. The two separate doubling effects stack multiplicatively—just as two copies of Anointed Procession produce 4× the original number [C11]—so 1 token × 2 (Doubling Season) × 2 (Anointed Procession) = 4 tokens. The [CR 614.5] example (two "double damage" sources yielding 8, not infinite) confirms that multiple distinct sources of the same replacement type apply once each and multiply together rather than recursing.

Review: **correct**. Correct four tokens and no loop, with one application of each replacement under 614.5.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

Ruling: The affected player (the one being dealt damage) chooses the order. Yes, the final damage can be either 7 or 8.

Why: Because neither effect is a self-replacement effect, the choice proceeds to rule 616.1e, where "any of the applicable replacement and/or prevention effects may be chosen" by the affected player [CR 616.1] [CR 616.1a] [CR 616.1e]. Applying double first then +1 gives 3 × 2 + 1 = 7; applying +1 first then double gives (3 + 1) × 2 = 8. After the first effect is applied, the process repeats for the remaining effect [CR 616.1f].

Review: **correct**. Correct affected player chooses, producing 7 or 8 depending on order, with replacement ordering citations.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: Because it is Alice's turn, she is the active player and goes first in APNAP order when placing triggered abilities on the stack [CR 603.3b]. Alice's ability is placed first, then Bob's is placed on top of it [CR 405.2]. When all players pass in succession, the top (last-added) object on the stack resolves [CR 405.5], so Bob's ability resolves before Alice's.

Review: **correct**. Correct Bob resolves first under APNAP stacking and last-in-first-out resolution.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is 2/2, and it does not matter which enchantment entered first.

Why: Humility's "have base power and toughness 1/1" is a set effect applied in layer 7b [CR 613.4b], while Glorious Anthem's "get +1/+1" is a modify effect applied in layer 7c [CR 613.4c]. Because the two effects fall in different sublayers, they are applied in fixed sublayer order (7b before 7c) regardless of timestamp [CR 613.4], so the creature is always 1/1 + 1/+1 = 2/2.

Review: **correct**. Correct 2/2 independent of timestamp; base-setting sublayer precedes modification.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own hexproof creature with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you control both the creature and the Giant Growth spell, the hexproof restriction does not apply to you. Giant Growth simply requires "target creature" [C1], and you have priority and can pay the cost, so the targeting is legal.

Review: **correct**. Correct own Giant Growth allowed; hexproof only restricts opponents.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

Ruling: No. In the second combat damage step your 3/3 assigns 0 damage. It is still a blocked creature (the block was declared and nothing unblocked it), but no creatures are currently blocking it because the 2/2 is dead. Without trample, a blocked creature can only assign damage to the creatures blocking it, and with none present it assigns no combat damage at all.

Why: A creature that was declared as blocked remains blocked for the rest of combat even after its blockers die [CR 510.1c]. Rule 510.1c explicitly states that if no creatures are currently blocking it (e.g., they were destroyed), it assigns no combat damage. Trample is the ability that would let excess damage go to the player [CR 702.19b], but your attacker does not have it, so it has no legal target for its damage in the second combat damage step.

Review: **correct**. Correct no second-step damage to player; remains blocked without trample. Bare rule references are supplied and now link in UI.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

Ruling: No, the token does not return to the battlefield. Once it has been exiled (i.e., left the battlefield), it cannot come back.

Why: [CR 111.8] states that a token that has left the battlefield can't move to another zone or come back onto the battlefield; if such a token would change zones, it remains in its current zone instead. So when the second part of the effect tries to return the token, that action simply doesn't occur—the token stays in exile and ceases to exist the next time state-based actions are checked per [CR 111.7].

Review: **correct**. Correct token cannot change zones again during resolution and only later ceases to exist; 111.8/111.7 distinguish mechanisms.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You may activate "Sacrifice this creature: Draw a card" on the turn you cast the creature, as long as you have priority.

Why: Summoning sickness (rule 302.6) restricts only activated abilities whose activation cost includes the tap symbol ({T}) or the untap symbol ({Q}), and it restricts attacking. A sacrifice cost contains neither symbol, so the restriction does not apply. You may activate the ability any time you have priority [CR 117.1b].

Review: **correct**. Correct sacrifice ability usable without tap/untap symbols; rule 302.6 accurately paraphrased and 117.1b supports activation timing.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. You cannot cast an instant in response to the legend rule. The legend rule is a state-based action that is performed automatically before any player receives priority, so there is no window to respond.

Why: State-based actions are dealt with before a player would receive priority [CR 117.2d], and the game performs all applicable state-based actions as a single event each time a player would get priority [CR 117.5]. The legend rule (choosing one legendary permanent and putting the rest into their owners' graveyards) is one such state-based action [CR 704.5j]. Because no player has priority at the moment the SBA is resolved, no one can cast a spell or activate an ability in response [CR 117.1].

Review: **correct**. Correct no response before legend-rule SBA; chooses one before priority under 117.2d/117.5 and 704.5j.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What is the exact protection quality on your creature (e.g., "protection from red," "protection from black," "protection from a specific player," "protection from everything")?
2. What is the removal spell (or ability) your opponent used? Specifically: does it target your creature, and what color/quality does it have?

Review: **correct**. Correct clarification asks protection quality and removal spell details without unconditional answer.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

