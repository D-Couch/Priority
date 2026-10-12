# hybrid-neighbors-original

Status: **complete** · implementation commit `8cd2f2fdefeaa477f6f6707ae9bc5e1222f826f2`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 19/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 93.8% |
| Cases retrieving every expected evidence group | 17/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 1 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 19/20 reviewed |
| Reviewed accuracy | 95.0% |
| Mean reviewed rubric score | 95.0% |
| Median successful response | 11.48 s |
| p95 successful response | 16.48 s |
| Median first visible answer token | 9.88 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 6.90 |
| 02-hold-priority (r1) | 100.0% | correct | 9.09 |
| 03-illegal-target (r1) | 100.0% | correct | 7.17 |
| 04-partial-targets (r1) | 100.0% | correct | 16.42 |
| 05-trample-indestructible (r1) | 100.0% | correct | 14.56 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 10.23 |
| 07-zero-toughness (r1) | 50.0% | incorrect | 16.54 |
| 08-commander-dies (r1) | 100.0% | correct | 12.88 |
| 09-commander-tax (r1) | 100.0% | correct | 7.50 |
| 10-rest-in-peace (r1) | 75.0% | correct | 8.56 |
| 11-token-doublers (r1) | 100.0% | correct | 13.33 |
| 12-replacement-choice (r1) | 100.0% | correct | 15.84 |
| 13-apnap (r1) | 100.0% | correct | 11.50 |
| 14-humility-anthem (r1) | 100.0% | correct | 14.48 |
| 15-own-hexproof (r1) | 100.0% | correct | 7.63 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 12.11 |
| 17-token-blink (r1) | 100.0% | correct | 10.54 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 11.46 |
| 19-legend-response (r1) | 50.0% | correct | 16.48 |
| 20-clarify-interaction (r1) | 100.0% | correct | 8.15 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No. You cannot respond to your opponent tapping a basic Forest for mana.

Why: A Forest's "{T}: Add {G}" is an activated mana ability [CR 305.6] [CR 605.1a]. Activated mana abilities don't go on the stack, so they can't be targeted, countered, or otherwise responded to; they resolve immediately after activation [CR 605.3b].

Review: **correct**. Correct activated mana ability cannot be responded to; 605.3b and 605.1a directly support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you receive priority again immediately after casting the instant, before your opponent. No, the instant does not resolve immediately; it resolves only after all players pass in succession.

Why: The player who had priority when casting a spell receives priority again afterward [CR 117.3c]. The spell on the stack resolves only when all players pass in succession [CR 405.5] [CR 117.4], so your opponent gets a window to respond before the instant resolves.

Review: **correct**. Correct caster retains priority and all-player-pass sequence; cited priority/stack rules support both.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No, you do not draw a card.

Why: When Defiant Strike tries to resolve, the destroyed creature is no longer on the battlefield, making it an illegal target [CR 608.2b]. Because that is the spell's only target, the entire spell fails to resolve and is put into your graveyard, so neither the +1/+0 nor the card draw occurs [C2].

Review: **correct**. Correct no card when all targets are illegal; 608.2b and Defiant Strike ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes. The remaining legal creature takes 2 damage.

Why: The spell has one instance of the word "target" with two creatures chosen for it. Because at least one target for that instance is still legal, the spell resolves normally rather than being removed from the stack [CR 608.2b]. At resolution, the illegal target simply isn't affected, while the legal target is dealt 2 damage as the effect instructs [CR 608.2b].

Review: **correct**. Correct remaining legal target takes 2 damage; 608.2b explains partial target legality.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Ruling: Yes. You may assign 2 damage to the indestructible 2/2 blocker and 4 damage to the defending player.

Why: Trample requires you to assign lethal damage (damage equal to or greater than the blocker's toughness) to the blocking creature before assigning excess to the player. The 2/2's toughness is 2, so assigning 2 damage satisfies that requirement. The trample rule explicitly states that when checking for assigned lethal damage, you do not take into account "any abilities or effects that might change the amount of damage that's actually dealt" [CR 702.19b]. Indestructible prevents destruction after damage is dealt [CR 702.12b] but does not alter the damage-assignment check, so the remaining 4 damage may go to the defending player.

Review: **correct**. Correct trample assignment to indestructible blocker and player; cited example supports distinction between lethal assignment and damage dealt.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

Ruling: The maximum damage you can assign to the defending player is **4**.

Why: Because your attacker has deathtouch, any nonzero amount of damage assigned to the 8/8 blocker counts as lethal damage for trample purposes [CR 702.2c]. Trample requires you to assign lethal damage to the blocker before excess damage may go to the player [CR 702.19b]. So you assign 1 damage to the 8/8 (satisfying the lethal-damage requirement) and the remaining 4 damage to the defending player.

Review: **correct**. Correct one deathtouch damage satisfies trample assignment and leaves four for player.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: Yes, the indestructible creature survives. It remains on the battlefield as a 0/0 until the −3/−3 effect expires at end of turn.

Why: A creature with 0 damage marked and 0 toughness meets the "lethal damage" condition (damage ≥ toughness) [CR 302.7], which would normally trigger the state-based action to destroy it. However, indestructible explicitly causes the permanent to ignore that state-based action: "Such permanents aren't destroyed by lethal damage, and they ignore the state-based action that checks for lethal damage" [CR 702.12b]. Since no other effect removes it, it simply stays as a 0/0 indestructible creature.

Review: **incorrect**. Incorrect and unsafe: claims 0/0 creature survives because only lethal-damage SBA applies. CR 704.5f sends a creature with toughness 0 or less to graveyard regardless of damage and indestructible. New unsupported claim caused by semantic retrieval returning 704.5g while omitting adjacent 704.5f.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 704.5f

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

Ruling: Yes to both. You may put your commander into the command zone from the graveyard, and any "dies" (or "leaves the battlefield") triggered abilities still trigger.

Why: "Dies" is defined as being put into a graveyard from the battlefield [CR 700.4], and that zone-change event occurs when the commander is destroyed, before any state-based actions are checked. The commander's owner may then put it into the command zone as a state-based action [CR 903.9a] [CR 704.6d], which is a separate, subsequent event. Because the "dies" trigger condition was already satisfied at the moment of the initial zone change, the triggered ability goes on the stack normally [CR 603.10a] [CR 603.6c].

Review: **correct**. Correct commander dies trigger occurs on battlefield-to-graveyard move before command-zone SBA; cited rules support timing.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax is {4}.

Why: Rule 903.8 states the tax is "an additional {2} for each previous time the player casting it has cast it from the command zone that game." You have cast it from the command zone twice, so 2 × {2} = {4}. The cast from your hand does not count because the rule specifically tracks casts *from the command zone* [CR 903.8].

Review: **correct**. Correct commander tax is four; counts only prior command-zone casts.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No. Blood Artist does not trigger.

Why: "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's replacement effect changes that zone change so the creature is exiled instead of being put into a graveyard [C1]. Because the creature is never put into a graveyard, it never dies, and Blood Artist's trigger condition is never met [C2].

Review: **correct**. Correct Rest in Peace replaces graveyard event and prevents dies trigger.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create **4** tokens. The doublers do **not** loop forever.

Why: Both Doubling Season and Anointed Procession are replacement effects modifying the same "create a token" event, so you choose which applies first [CR 616.1]. After the first doubler doubles 1 → 2, the process repeats and the second doubler doubles 2 → 4 [CR 616.1f]. Each replacement effect gets only one opportunity to affect the event and does not invoke itself repeatedly [CR 614.5], so the chain stops at 4. This matches the confirmed stacking example: two token-doubling permanents produce four times the original number [C11].

Review: **correct**. Correct two token doublers yield four once each with no loop.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

Ruling: You (the affected player, i.e., the one being dealt damage) choose which replacement effect applies first. If you apply "increase by 1" first, the damage becomes 4, then doubling makes it 8. If you apply "double" first, the damage becomes 6, then "increase by 1" makes it 7. Both 7 and 8 are possible outcomes.

Why: When two or more replacement effects attempt to modify the same event, the affected player chooses which one to apply, and after it is applied the process repeats with the remaining effect [CR 616.1][CR 616.1f]. Doubling damage is explicitly a replacement effect [CR 701.10g], and a second replacement effect can become applicable to the event as modified by the first [CR 616.2]. Because the order is chosen by the affected player, the arithmetic yields either (3+1)×2 = 8 or (3×2)+1 = 7.

Review: **correct**. Correct affected player chooses and arithmetic 7 or 8 is correct.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: When triggered abilities are put on the stack, each player acts in APNAP order—Alice (active player) places her ability first, then Bob (non-active player) places his on top [CR 603.3b]. Because each new object is placed on top of all objects already on the stack [CR 405.2], Bob's ability sits above Alice's and therefore resolves first in the usual last-in, first-out order.

Review: **correct**. Correct Bob APNAP trigger is on top and resolves first.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is 2/2. It does not matter which enchantment entered the battlefield first.

Why: Humility's "have base power and toughness 1/1" is a setting effect applied in layer 7b [CR 613.4b], while Glorious Anthem's "+1/+1" is a modifying effect applied in layer 7c [CR 613.4c]. Because they operate in different sublayers, the fixed 7b → 7c ordering always applies regardless of timestamp [CR 613.4], so the creature is always 1/1 (set) + 1/+1 (modified) = 2/2.

Review: **correct**. Correct Humility/Anthem produces 2/2 independent of timestamp.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own hexproof creature with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Because you control both the creature and the Giant Growth spell, the hexproof restriction does not apply to you. Giant Growth simply requires a legal creature target [C1], and your own creature is one.

Review: **correct**. Correct own hexproof creature can be targeted by own Giant Growth.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

Ruling: No. In the second combat damage step, your 3/3 assigns no combat damage at all.

Why: Because the 2/2 blocker was destroyed in the first combat damage step, no creatures are currently blocking your attacker when the second combat damage step begins. Under rule 510.1c, a blocked creature that has no creatures currently blocking it (for example, because they were destroyed) assigns no combat damage. Since your attacker lacks trample, it could not assign excess damage to the player even while blocked, and once the blocker is gone it simply deals nothing. [CR 510.1c]

Review: **correct**. Correct blocked attacker without trample assigns no second-step damage to player.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

Ruling: No. Once the token has left the battlefield to exile, it cannot be returned to the battlefield. The return effect does nothing to the token; it remains in exile and ceases to exist the next time state-based actions are checked.

Why: Rule 111.8 states that a token that has left the battlefield can't move to another zone or come back onto the battlefield, and if such a token would change zones, it remains in its current zone instead [CR 111.8]. Rule 111.7 confirms that a token in a zone other than the battlefield ceases to exist as a state-based action [CR 111.7]. Because the token is already in exile when the return effect would apply, the effect has no valid object to put onto the battlefield.

Review: **correct**. Correct token cannot return and only ceases as subsequent SBA.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You can activate "Sacrifice this creature: Draw a card" on the same turn you cast the creature, as long as you have priority and the stack is empty (or you're otherwise allowed to activate abilities).

Why: Summoning sickness (rule 302.6) restricts only two things: activating a creature's ability that includes the tap symbol ({T}) or untap symbol ({Q}) in its activation cost, and attacking [CR 302.6]. A "Sacrifice this creature" cost contains neither symbol, so the restriction does not apply [CR 602.5a]. After your creature spell resolves, you receive priority [CR 117.3b], and with priority you may activate abilities [CR 117.1].

Review: **correct**. Correct sacrifice ability without tap-symbol cost can be activated despite summoning sickness.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. You cannot cast an instant in response to the legend rule. The legend rule is a state-based action that is resolved immediately; it does not use the stack and does not generate a window for priority.

Why: The legend rule is listed among the state-based actions [CR 704.5j], and actions performed by the game rules are carried out without a player receiving priority [CR 117.2]. You may cast an instant only when you have priority [CR 117.1a], but priority is granted only *after* state-based actions have been checked and resolved. The choice of which legendary permanent to keep is made as part of resolving the state-based action itself, not as a response to a spell or ability on the stack.

Review: **correct**. Correct legend-rule SBA occurs before priority; no response window.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality is the protection from (e.g., "protection from red," "protection from black," "protection from a specific player," "protection from everything")?
2. What is the removal spell (exact card name), and does it target your creature or affect all creatures?
3. What color(s) is the spell, and who controls it?

Review: **correct**. Appropriate clarification asks protection quality and removal spell/characteristics. Minor UI defect: closing `[[Exact Card Name]]` markup is missing in question 2; no rules error.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

