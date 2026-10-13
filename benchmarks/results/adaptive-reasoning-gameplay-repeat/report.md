# adaptive-reasoning-gameplay-repeat

Status: **complete** · implementation commit `506a4b8dda275024b6e673519b5cbe392bad760a`

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
| Median successful response | 4.22 s |
| p95 successful response | 10.17 s |
| Median first visible answer token | 2.94 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 3.55 |
| 02-hold-priority (r1) | 100.0% | correct | 3.47 |
| 03-illegal-target (r1) | 100.0% | correct | 3.76 |
| 04-partial-targets (r1) | 100.0% | correct | 3.69 |
| 05-trample-indestructible (r1) | 100.0% | correct | 11.50 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 8.07 |
| 07-zero-toughness (r1) | 100.0% | correct | 3.74 |
| 08-commander-dies (r1) | 100.0% | correct | 7.88 |
| 09-commander-tax (r1) | 100.0% | correct | 4.19 |
| 10-rest-in-peace (r1) | 75.0% | correct | 6.63 |
| 11-token-doublers (r1) | 100.0% | correct | 4.25 |
| 12-replacement-choice (r1) | 100.0% | correct | 7.83 |
| 13-apnap (r1) | 100.0% | correct | 8.48 |
| 14-humility-anthem (r1) | 100.0% | correct | 5.06 |
| 15-own-hexproof (r1) | 100.0% | correct | 3.72 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 10.17 |
| 17-token-blink (r1) | 100.0% | correct | 7.14 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 4.00 |
| 19-legend-response (r1) | 50.0% | correct | 4.02 |
| 20-clarify-interaction (r1) | 100.0% | correct | 3.53 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No, you cannot respond to your opponent tapping a basic Forest for mana.

Why: Activated mana abilities do not go on the stack, so they cannot be targeted, countered, or otherwise responded to [CR 605.3b]. Instead, they resolve immediately after they are activated [CR 605.3b].

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you get priority again before your opponent, and no, the instant does not resolve immediately.

Why: When you cast a spell while you have priority, you receive priority again after it is cast [CR 117.3c]. The spell remains on the stack and only resolves when all players pass in succession [CR 405.5], [CR 117.4].

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No, you do not draw a card.
Why: If the target creature is destroyed before Defiant Strike resolves, it is no longer a legal target, causing the spell to fail to resolve entirely. Consequently, none of its effects, including the card draw, occur. [C2] [CR 608.2b]

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes, the remaining legal creature takes 2 damage.
Why: When a spell with multiple targets resolves, it checks if each target is still legal; if at least one target remains legal, the spell resolves normally [CR 608.2b]. The spell’s effect applies to the legal target, while the illegal target is not affected by the part of the effect for which it is illegal [CR 608.2b].

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Ruling:** Yes. You must assign at least 2 damage to the 2/2 blocker (enough to be lethal), and you may assign the remaining 4 to the defending player.

**Why:** Trample requires you to assign lethal damage to blocking creatures before assigning excess to the player, and the check for "lethal damage" considers only damage already marked and damage being assigned in the same step—not abilities that change what happens after damage is dealt [CR 702.19b]. Indestructible prevents destruction but does not alter the lethal-damage calculation or prevent damage from being assigned [CR 702.12b]. This is the same principle as the protection example in the trample rule, where the blocker's protection doesn't reduce the required assignment [CR 702.19b].

Review: **correct**. Answer satisfies the authored criteria for the stated scenario; cited rule/card identifiers support its material rules claims.
Reviewer: Codex

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

**Ruling:** You can assign a maximum of 4 damage to the defending player.

**Why:** Deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for the purpose of determining excess damage [CR 702.2c]. Trample requires you to assign lethal damage to the blocking creature before assigning excess to the player [CR 702.19b]. Since 1 damage is sufficient to be "lethal" against the 8/8 due to deathtouch, the remaining 4 damage (5 power − 1) may be assigned to the defending player.

Review: **correct**. Answer satisfies the authored criteria for the stated scenario; cited rule/card identifiers support its material rules claims.
Reviewer: Codex

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: No, it does not survive; it is put into its owner’s graveyard.
Why: Indestructible prevents a permanent from being destroyed, but it does not prevent it from being put into the graveyard due to having toughness 0 or less [CR 702.12b]. State-based actions require that a creature with toughness 0 or less be put into its owner’s graveyard, and this event cannot be replaced by regeneration or indestructible [CR 704.5f].

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

**Ruling:** Yes, you may put your commander into the command zone from the graveyard, and yes, abilities that trigger when it "dies" still trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Your commander was put into the graveyard, so the trigger event occurred. The owner's option to move it to the command zone is a state-based action that happens afterward [CR 903.9a]; it doesn't retroactively prevent the trigger from having fired. Zone-change triggers look back in time to the moment the permanent moved [CR 603.10a].

Review: **correct**. Answer satisfies the authored criteria for the stated scenario; cited rule/card identifiers support its material rules claims.
Reviewer: Codex

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax is {4}.
Why: The commander tax is an additional cost of {2} for each previous time the player has cast the commander from the command zone [CR 903.8]. Since you have cast it from the command zone twice previously, the total additional cost is 2 × {2} = {4} [CR 903.8]. Casting the commander from your hand does not count toward this tax, as the rule specifically references casts from the command zone [CR 903.8].

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

**Ruling:** No, Blood Artist does not trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exiling the card, so the creature is never put into a graveyard and the trigger condition is never met [C2].

Review: **correct**. Answer satisfies the authored criteria for the stated scenario; cited rule/card identifiers support its material rules claims.
Reviewer: Codex

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create four tokens. The doublers do not loop forever.

Why: Doubling Season and Anointed Procession are both replacement effects that apply to the same event, doubling the number of tokens created. When multiple such effects apply, they are applied sequentially, resulting in a total multiplication of 2 x 2 = 4. A replacement effect does not invoke itself repeatedly; it gets only one opportunity to affect an event or any modified events that may replace that event. [C1] [C7] [CR 614.5]

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

**Ruling:** You (the affected player) choose the order. The final damage can be either 7 or 8.

**Why:** Under [CR 616.1], the affected player chooses which replacement effect to apply first, and [CR 616.1f] says the process is repeated with the remaining effects. If you apply the doubling effect first, 3 × 2 = 6, then +1 gives 7. If you apply the +1 effect first, 3 + 1 = 4, then doubling gives 8. Doubling damage is a replacement effect per [CR 701.10g].

Review: **correct**. Answer satisfies the authored criteria for the stated scenario; cited rule/card identifiers support its material rules claims.
Reviewer: Codex

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

**Ruling:** Bob's triggered ability resolves first.

**Why:** In APNAP order, Alice (the active player) puts her triggered ability on the stack first, then Bob puts his on top of it [CR 603.3b]. Each object placed on the stack goes on top of all objects already there [CR 405.2], so Bob's ability is the topmost object and resolves first when all players pass [CR 405.5].

Review: **correct**. Answer satisfies the authored criteria for the stated scenario; cited rule/card identifiers support its material rules claims.
Reviewer: Codex

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is a 2/2. It does not matter which enchantment entered first.

Why: Humility sets the creature's power and toughness to 1/1 in layer 7b [C1] [CR 613.4b]. Glorious Anthem adds +1/+1 in layer 7c [C5] [CR 613.4c]. Because layer 7b is applied before layer 7c, the +1/+1 is added to the set value of 1/1, resulting in 2/2 [CR 613.1g]. Timestamp order only determines the application order of effects within the same layer or sublayer, not across different layers [CR 613.7].

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes, you may target your own creature with hexproof using Giant Growth.

Why: Hexproof only prevents a permanent from being targeted by spells or abilities controlled by your opponents [CR 702.11b]. Since you control the spell, the hexproof ability does not restrict your choice of target. Giant Growth is a legal spell that targets a creature, and you have the priority and resources to cast it [C1] [CR 117.1a].

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**Ruling:** No. In the second combat damage step, your attacker assigns no combat damage at all.

**Why:** Your attacker is still a blocked creature (it was declared as blocked), and in the second combat damage step no creatures are currently blocking it. A blocked creature whose blockers are all gone assigns no combat damage, regardless of whether it has trample or double strike [CR 510.1c]. Double strike only determines *which* steps the creature assigns damage in [CR 702.4b]; it does not change *how* a blocked creature assigns its damage.

Review: **correct**. Answer satisfies the authored criteria for the stated scenario; cited rule/card identifiers support its material rules claims.
Reviewer: Codex

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**Ruling:** No, the token does not return to the battlefield. It remains in exile and ceases to exist the next time state-based actions are checked.

**Why:** A token that has left the battlefield can't move to another zone or come back onto the battlefield; if such a token would change zones, it remains in its current zone instead [CR 111.8]. It then ceases to exist the next time state-based actions are checked [CR 111.8].

Review: **correct**. Answer satisfies the authored criteria for the stated scenario; cited rule/card identifiers support its material rules claims.
Reviewer: Codex

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes, you can activate it this turn.

Why: The summoning sickness restriction only applies to activated abilities that include the tap or untap symbol in their activation cost [CR 302.6]. Since your ability’s cost is "Sacrifice this creature" and contains no tap or untap symbol, the restriction does not apply [CR 602.5a]. You may activate the ability any time you have priority [CR 117.1b].

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No, you cannot cast an instant in response to the legend rule.

Why: State-based actions, including the legend rule, happen automatically and are dealt with before a player would receive priority [CR 117.2d] [CR 117.5]. Since no player has priority during this process, no one can cast spells or activate abilities in response [CR 117.1] [CR 117.2e].

Review: **correct**. Answer satisfies the authored rubric for the stated scenario; cited rule/card identifiers support its material claims.
Reviewer: Codex

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:
1. What is the specific quality of the protection (e.g., "protection from black," "protection from red," "protection from [card name]")?
2. What is the name or color of the removal spell used?
3. Did the removal spell target your creature, or did it deal damage to it?

Review: **correct**. Appropriately requests missing protection and removal details; this satisfies the scenario rubric and is a clarification, not an incorrect abstention.
Reviewer: Codex

Missing reference groups: none

