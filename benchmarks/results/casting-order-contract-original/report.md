# casting-order-contract-original

Status: **complete** · implementation commit `f4b87111878e6e50b32076f548b1d9896a1fac8b`

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
| Answers with citations | 20/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 20/20 reviewed |
| Reviewed accuracy | 100.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 11.16 s |
| p95 successful response | 18.86 s |
| Median first visible answer token | 9.52 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.73 |
| 02-hold-priority (r1) | 100.0% | correct | 9.45 |
| 03-illegal-target (r1) | 100.0% | correct | 8.63 |
| 04-partial-targets (r1) | 100.0% | correct | 10.78 |
| 05-trample-indestructible (r1) | 100.0% | correct | 18.86 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 10.16 |
| 07-zero-toughness (r1) | 100.0% | correct | 20.18 |
| 08-commander-dies (r1) | 100.0% | correct | 16.36 |
| 09-commander-tax (r1) | 100.0% | correct | 7.71 |
| 10-rest-in-peace (r1) | 75.0% | correct | 7.85 |
| 11-token-doublers (r1) | 100.0% | correct | 12.38 |
| 12-replacement-choice (r1) | 100.0% | correct | 14.24 |
| 13-apnap (r1) | 100.0% | correct | 11.55 |
| 14-humility-anthem (r1) | 100.0% | correct | 14.55 |
| 15-own-hexproof (r1) | 100.0% | correct | 7.10 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 13.25 |
| 17-token-blink (r1) | 100.0% | correct | 17.77 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 10.05 |
| 19-legend-response (r1) | 50.0% | correct | 11.87 |
| 20-clarify-interaction (r1) | 100.0% | correct | 9.40 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No. Tapping a basic Forest for mana is an activated mana ability, which does not go on the stack and therefore cannot be targeted, countered, or otherwise responded to. It resolves immediately after it is activated.

Why: A basic Forest's "Tap: Add one green mana" ability meets every criterion for an activated mana ability (no target, adds mana, not a loyalty ability, no library interaction) [CR 605.1a]. Because it is a mana ability, it bypasses the stack entirely and resolves immediately, leaving no window for either player to take an action in response [CR 605.3b].

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you receive priority again after casting the instant. No, the instant does not resolve immediately; it waits on the stack until all players pass in succession.

Why: A player who has priority when they cast a spell receives priority again afterward [CR 117.3c]. The spell then sits on the stack, and it resolves only when all players pass in succession without taking actions [CR 405.5] [CR 117.4]. Your opponent will receive priority before the instant resolves, giving them the chance to respond.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No. If your creature is destroyed before Defiant Strike resolves, the creature is no longer in the zone it was in when targeted, making it an illegal target. Since that is the spell's only target, Defiant Strike doesn't resolve at all, and you do not draw a card.

Why: A target that has left the zone it was in when targeted is illegal [CR 608.2b]. When all of a spell's targets are illegal, the spell doesn't resolve and is put into its owner's graveyard [CR 608.2b]. The card-specific ruling confirms this directly: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes. The remaining legal creature takes 2 damage.

Why: Because not *all* targets are illegal, the spell resolves normally; only the illegal target is skipped. [CR 608.2b] states that if all targets are illegal the spell doesn't resolve, but "otherwise, the spell or ability will resolve normally," and "illegal targets, if any, won't be affected" while "other parts of the effect for which those targets are not illegal may still affect them." The Plague Spores example in the same rule illustrates this: a spell with one illegal and one legal target still resolves and affects the legal target.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Ruling: Yes. You may assign 2 damage to the indestructible 2/2 blocker and 4 damage to the defending player.

Why: Under [CR 702.19b], once the blocking creature is assigned lethal damage (2 damage for a 2-toughness creature), any excess may be assigned to the defending player. Indestructible prevents the creature from being destroyed [CR 702.12b] but does not raise the lethal-damage threshold used for trample assignment. The protection example in [CR 702.19b] confirms that even damage that will be prevented still satisfies the "assigned lethal damage" requirement, so an ability that merely prevents destruction (rather than changing the damage amount) likewise does not alter the threshold.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

Ruling: You can assign a maximum of 4 damage to the defending player (1 to the 8/8 blocker, 4 to the player).

Why: Deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for the purpose of determining excess damage [CR 702.2c]. Trample requires that all blocking creatures be assigned lethal damage before excess damage may be assigned to the defending player [CR 702.19b]. Since 1 damage satisfies the lethal-damage requirement against the 8/8, the remaining 4 of the 5/5's total combat damage [CR 510.1a] may be assigned to the defending player.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: No. The indestructible 3/3 does not survive. The −3/−3 makes it a 0/0, and the state-based action for toughness 0 or less puts it into its owner's graveyard.

Why: Indestructible means a permanent "can't be destroyed" and "isn't destroyed by lethal damage," and it ignores the state-based action that checks for lethal damage [CR 702.12b]. However, a creature with toughness 0 or less is put into its owner's graveyard by a separate state-based action [CR 704.5f], which is not a destruction event. Indestructible does not prevent that action, so the 0/0 creature is sent to the graveyard when state-based actions are checked [CR 704.1].

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

Ruling: Yes, you may put your commander into the command zone, and yes, "when it dies" / "when it leaves the battlefield" triggers still trigger.

Why: The commander is destroyed and moves to the graveyard; that zone change is the trigger event for leaves-the-battlefield abilities, which fire when a permanent moves from the battlefield to another zone [CR 603.6c] [CR 603.10a]. After it is in the graveyard, the state-based action in rule 903.9a lets its owner put it into the command zone [CR 903.9a]. Because the trigger already occurred at the moment the permanent left the battlefield, subsequently moving the card to the command zone does not cancel or prevent those triggers.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax is {4}.

Why: Rule 903.8 states the commander "costs an additional {2} for each previous time the player casting it has cast it from the command zone that game." You have cast it from the command zone twice; the cast from your hand does not count toward this tally. Therefore the tax is 2 × {2} = {4}. [CR 903.8]

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No. Blood Artist does not trigger.

Why: "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's static ability replaces any event that would put a card or token into a graveyard from anywhere with exile instead [C1], so the destroyed creature is exiled and never enters a graveyard. Because the creature is never put into a graveyard, it never dies, and Blood Artist's trigger condition is never met [C2].

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create **4** tokens (1 × 2 × 2). The doublers do **not** loop forever.

Why: Each "twice as many" replacement effect multiplies the token count by 2, and they stack multiplicatively—two Doubling Seasons give 4×, three give 8×, and so on [C2][C11]. With one Doubling Season and one Anointed Procession, the single token is doubled twice, yielding 4. A replacement effect gets only one opportunity to affect an event and does not invoke itself repeatedly [CR 614.5], so the doubling is applied once per effect rather than recursively.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

Ruling: You (the affected player) choose which replacement effect to apply first. Yes, the final damage can be either 7 or 8.

Why: Under [CR 616.1], when two or more replacement effects modify the same event, the affected player chooses which to apply first; since neither is a self-replacement effect and none of the mandatory-choice steps in 616.1a–d apply, you may pick either one per [CR 616.1e]. After the first effect is applied, the second applies to the already-modified event per [CR 616.1f]. Doubling first gives 3 → 6 → 7; increasing first gives 3 → 4 → 8. Doubling damage is itself a replacement effect per [CR 701.10g].

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: When multiple triggered abilities go on the stack, each player in APNAP order puts their abilities on the stack; since Alice is the active player, she places hers first, then Bob places his on top [CR 603.3b]. Each new object is placed on top of all objects already on the stack [CR 405.2]. When all players pass in succession, the top (last-added) object resolves [CR 405.5], so Bob's ability, sitting above Alice's, resolves first.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is 2/2, and it does not matter which enchantment entered the battlefield first.

Why: Humility's "have base power and toughness 1/1" is a P/T-setting effect applied in sublayer 7b [CR 613.4b], while Glorious Anthem's "get +1/+1" is a P/T-modifying effect applied in sublayer 7c [CR 613.4c]. Because the two effects fall in different sublayers, the fixed sublayer order (7b before 7c) determines the result regardless of timestamp [CR 613.4]. The creature's base P/T is set to 1/1 in 7b, then +1/+1 is added in 7c, yielding 2/2.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own hexproof creature with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Because you control both the creature and the Giant Growth, the hexproof restriction does not apply to your own spell. Giant Growth simply requires "target creature" [C1], and you have priority and can pay the cost, so the targeting is legal.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

Ruling: No. In the second combat damage step your 3/3 assigns no combat damage at all, so the player takes 0.

Why: Your attacker is a blocked creature (it was declared as blocked by the 2/2). In the second combat damage step no creatures are currently blocking it, and because it lacks trample, rule 510.1c applies: "If no creatures are currently blocking it (if, for example, they were destroyed or removed from combat), it assigns no combat damage." [CR 510.1c] Double strike lets it assign damage in both steps [CR 702.4b], but the assignment in the second step is still governed by the blocked-creature rules, and without trample there is no mechanism to redirect that damage to the player.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

Ruling: No. Once the token is exiled, it has left the battlefield and can no longer be returned to it. The return effect does nothing to the token; it remains in exile and ceases to exist the next time state-based actions are checked.

Why: Rule 111.8 states that a token that has left the battlefield can't move to another zone or come back onto the battlefield, and if it would change zones it remains in its current zone instead. Rule 111.7 confirms that a token in a zone other than the battlefield ceases to exist as a state-based action. Because the token is in exile when the return effect attempts to move it, the return is simply prevented. [CR 111.8] [CR 111.7]

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You may activate "Sacrifice this creature: Draw a card" on the turn you cast it, even though the creature is still under your control for the first time.

Why: The summoning-sickness restriction applies only to a creature's activated ability whose activation cost includes the tap symbol ({T}) or the untap symbol ({Q}) [CR 302.6] [CR 602.5a]. Your ability's cost is "Sacrifice this creature," which contains neither symbol, so that restriction does not apply. As long as you have priority, you may activate the ability [CR 117.1b].

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. You cannot cast an instant in response to the legend rule. The legend rule is a state-based action that the game performs automatically before any player receives priority, so there is no window to respond.

Why: The legend rule (704.5j) is a state-based action, and state-based actions are dealt with automatically before a player would receive priority [CR 117.2d]. Specifically, each time a player would get priority, the game first performs all applicable state-based actions, including the legend rule, before that player actually receives priority [CR 117.5]. Because no player has priority during this process, no one can cast an instant or activate an ability in response [CR 117.1]. The choice of which legendary permanent to keep is made as part of the state-based action itself, not as a response to a spell or ability on the stack.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What is your creature's protection from? (e.g., "protection from red," "protection from black," "protection from a specific player," etc.)
2. What is the removal spell your opponent cast? (Card name, or at minimum: does it target a creature, and what color/quality does it have?)

Protection only prevents targeting by spells *with the stated quality* [CR 702.16b] and prevents damage *from sources with the stated quality* [CR 702.16e]. A removal spell that doesn't match the protection's quality, or that doesn't target (e.g., a board wipe), would not be blocked by the protection. I need the specific quality and the specific spell to give a ruling.

Review: **correct**. Reviewed against the frozen criteria; the current ruling matches the prior 20/20 review. Semantic citation support remains unavailable because that prior review did not record the field.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

