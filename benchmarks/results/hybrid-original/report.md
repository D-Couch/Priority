# hybrid-original

Status: **complete** · implementation commit `2df6e9b3a650df2d3ac378ca0d7ad3bee538bf5e`

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
| Median successful response | 10.62 s |
| p95 successful response | 18.95 s |
| Median first visible answer token | 9.29 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.80 |
| 02-hold-priority (r1) | 100.0% | correct | 9.57 |
| 03-illegal-target (r1) | 100.0% | correct | 9.44 |
| 04-partial-targets (r1) | 100.0% | correct | 11.01 |
| 05-trample-indestructible (r1) | 100.0% | correct | 18.95 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 10.35 |
| 07-zero-toughness (r1) | 50.0% | incorrect | 18.29 |
| 08-commander-dies (r1) | 100.0% | correct | 20.51 |
| 09-commander-tax (r1) | 100.0% | correct | 7.48 |
| 10-rest-in-peace (r1) | 75.0% | correct | 9.29 |
| 11-token-doublers (r1) | 100.0% | correct | 14.19 |
| 12-replacement-choice (r1) | 100.0% | correct | 12.57 |
| 13-apnap (r1) | 100.0% | correct | 12.26 |
| 14-humility-anthem (r1) | 100.0% | correct | 13.85 |
| 15-own-hexproof (r1) | 100.0% | correct | 6.83 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 10.90 |
| 17-token-blink (r1) | 100.0% | correct | 9.86 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 9.32 |
| 19-legend-response (r1) | 50.0% | correct | 12.92 |
| 20-clarify-interaction (r1) | 100.0% | correct | 9.94 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No. You cannot respond to your opponent tapping a basic Forest for mana.

Why: A basic Forest's "{T}: Add {G}" ability is an activated mana ability [CR 305.6] [CR 605.1a]. Activated mana abilities don't go on the stack, so they can't be targeted, countered, or otherwise responded to; they resolve immediately after activation [CR 605.3b] [CR 405.6c].

Review: **correct**. Correct activated mana ability cannot be responded to; 605.3b and 605.1a directly support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you receive priority again before your opponent. No, the instant does not resolve immediately; it sits on the stack until all players pass in succession.

Why: A player who has priority when they cast a spell receives priority again afterward [CR 117.3c]. Casting an instant uses the stack [CR 304.1], and a spell on the stack resolves only when all players pass in succession [CR 405.5] [CR 117.4]. Immediate resolution applies to mana abilities [CR 405.6c], not to instants.

Review: **correct**. Correct caster retains priority and all-player-pass sequence; cited priority/stack rules support both.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No, you do not draw a card. If the creature you targeted is destroyed before Defiant Strike resolves, it is no longer a legal target, the spell fails to resolve entirely, and the "Draw a card" instruction never happens.

Why: A target that is no longer in the zone it was in when targeted (e.g., a creature that left the battlefield) is illegal, and if all of a spell's targets are illegal, the spell doesn't resolve and is put into its owner's graveyard [CR 608.2b]. The card-specific ruling confirms this directly: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Correct no card when all targets are illegal; 608.2b and Defiant Strike ruling support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes. The remaining legal creature takes 2 damage.

Why: The spell uses the word "target" once, so both creatures are targets for that single instance. Because one target is still legal, not *all* targets are illegal, so the spell resolves normally [CR 608.2b]. The illegal target simply isn't affected, while the legal target is dealt 2 damage as the effect instructs [CR 608.2b].

Review: **correct**. Correct remaining legal target takes 2 damage; 608.2b explains partial target legality.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Ruling: Yes. You must assign at least 2 damage to the 2/2 blocker (lethal damage for an undamaged 2/2), and you may assign the remaining 4 damage to the defending player.

Why: Trample requires you to assign lethal damage to the blocking creature before assigning excess to the player, and the rule explicitly says that when checking for assigned lethal damage you do **not** take into account "abilities or effects that might change the amount of damage that's actually dealt" [CR 702.19b]. Indestructible does not reduce or prevent the damage dealt; it only means the creature isn't destroyed by it [CR 702.12b]. The supplied example confirms the principle with a similar case: a 6/6 with trample blocked by a 2/2 with protection must still assign 2 to the blocker and may assign the rest to the player [CR 702.19b].

Review: **correct**. Correct trample assignment to indestructible blocker and player; cited example supports distinction between lethal assignment and damage dealt.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

Ruling: The maximum damage you can assign to the defending player is **4**.

Why: Trample requires you to assign lethal damage to the blocking creature before assigning excess to the player [CR 702.19b]. Because your attacker has deathtouch, any nonzero amount of damage assigned to the 8/8 counts as lethal damage for this purpose [CR 702.2c]. So you assign the minimum 1 damage to the blocker, and the remaining 4 damage goes to the defending player.

Review: **correct**. Correct one deathtouch damage satisfies trample assignment and leaves four for player.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: Yes, it survives, but not because of indestructible. The −3/−3 makes it a 0/0, and since no damage is marked on it, the lethal-damage state-based action never triggers. A 0/0 creature with no damage simply remains on the battlefield.

Why: The only state-based action that destroys a creature based on toughness is 704.5g, which requires the creature to have toughness **greater than 0**, damage marked on it, and that damage to be ≥ its toughness. Here the toughness is 0 and no damage is marked, so that action doesn't apply at all. Indestructible (which prevents destruction and makes the permanent ignore 704.5g) is therefore irrelevant to this specific outcome; the creature would survive the same way even without it. [CR 704.5g] [CR 702.12b]

Review: **incorrect**. Incorrect and unsafe: claims 0/0 creature survives because only lethal-damage SBA applies. CR 704.5f sends a creature with toughness 0 or less to graveyard regardless of damage and indestructible. New unsupported claim caused by semantic retrieval returning 704.5g while omitting adjacent 704.5f.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 704.5f

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

Ruling: Yes, you may put your commander into the command zone, and yes, "dies" triggers still trigger.

Why: The commander being put into a graveyard from the battlefield is the event that satisfies the "dies" trigger condition [CR 700.4], and that event occurs before any state-based actions are checked. The option to move the commander to the command zone is a state-based action that happens when a player would next get priority [CR 903.9a] [CR 704.6d]; it is not a replacement effect, so it does not prevent the zone-change event from having already occurred. The triggered ability is registered at the moment of the event and is placed on the stack after state-based actions are resolved [CR 704.3], so the "dies" trigger fires regardless of the commander subsequently moving to the command zone.

Review: **correct**. Correct commander dies trigger occurs on battlefield-to-graveyard move before command-zone SBA; cited rules support timing.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax is {4}.

Why: Rule 903.8 states the commander "costs an additional {2} for each previous time the player casting it has cast it from the command zone that game." You have cast it from the command zone twice previously, so 2 × {2} = {4}. The cast from your hand does not count because the rule specifically tracks casts *from the command zone* [CR 903.8].

Review: **correct**. Correct commander tax is four; counts only prior command-zone casts.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No. Blood Artist does not trigger.

Why: "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that zone change, exiling the creature instead of putting it into a graveyard [C1]. Because the creature is never put into a graveyard, it does not die, so Blood Artist's trigger condition ("whenever another creature dies") is never met [C5].

Review: **correct**. Correct Rest in Peace replaces graveyard event and prevents dies trigger.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create **4 tokens**. The two doublers do not loop forever; each applies exactly once.

Why: Both Doubling Season and Anointed Procession are replacement effects modifying the same token-creation event. You choose the order in which they apply [CR 616.1], and after the first is applied, the second is then applied to the already-modified event [CR 616.1f] [CR 614.16]. A replacement effect gets only one opportunity to affect an event and does not invoke itself repeatedly [CR 614.5], so the calculation is 1 × 2 × 2 = 4. This matches the published ruling that two Anointed Processions yield four times the original token count [C11].

Review: **correct**. Correct two token doublers yield four once each with no loop.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

Ruling: The affected player (you, the one being dealt damage) chooses which replacement effect applies first. Yes, the final damage can be either 7 or 8.

Why: Under [CR 616.1], when two or more replacement effects modify the same event, the affected player chooses which to apply first; [CR 616.1e] confirms any applicable effect may be chosen, and [CR 616.1f] states the process repeats with the remaining effect. Doubling first gives 3→6→7; increasing by 1 first gives 3→4→8. The doubling effect is itself a replacement effect per [CR 701.10g], so both effects are eligible for the 616.1 ordering choice.

Review: **correct**. Correct affected player chooses and arithmetic 7 or 8 is correct.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: Under [CR 603.3b], when triggered abilities are placed on the stack, each player in APNAP order puts their applicable abilities on the stack. Since Alice is the active player, she places her ability first; Bob then places his ability on top of it [CR 405.2]. When all players pass, the top (last-added) object on the stack resolves [CR 405.5], so Bob's ability resolves before Alice's.

Review: **correct**. Correct Bob APNAP trigger is on top and resolves first.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is 2/2, and it does not matter which enchantment entered the battlefield first.

Why: Humility's "have base power and toughness 1/1" is a setting effect applied in layer 7b [CR 613.4b], while Glorious Anthem's "get +1/+1" is a modifying effect applied in layer 7c [CR 613.4c]. Sublayers are applied in fixed order (7b before 7c) regardless of timestamp [CR 613.4], so the creature is set to 1/1 and then receives +1/+1, yielding 2/2.

Review: **correct**. Correct Humility/Anthem produces 2/2 independent of timestamp.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own hexproof creature with your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. The restriction applies only to opponents' spells and abilities; it does not prevent the controller from targeting the creature with their own spells. Giant Growth simply requires "target creature" [C1], and your own creature is a legal target for your own spell.

Review: **correct**. Correct own hexproof creature can be targeted by own Giant Growth.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

Ruling: No. In the second combat damage step your 3/3 assigns no combat damage at all.

Why: Your creature was blocked, so it is not an unblocked attacker and cannot assign damage to the player under [CR 510.1b]. Because the only blocker is dead, no creatures are currently blocking it, and a blocked creature with no current blockers assigns no combat damage [CR 510.1c]. Trample would let excess damage reach the player, but your attacker does not have that ability [CR 702.19a].

Review: **correct**. Correct blocked attacker without trample assigns no second-step damage to player.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

Ruling: No. Once the token is exiled (i.e., it has left the battlefield), the subsequent instruction to return it to the battlefield has no effect. The token remains in exile and ceases to exist the next time state-based actions are checked.

Why: Rule 111.8 states that a token that has left the battlefield can't move to another zone or come back onto the battlefield; if such a token would change zones, it remains in its current zone instead [CR 111.8]. This is a general restriction with no exception for the same resolution, so the return instruction simply does nothing. The token then ceases to exist as a state-based action [CR 111.7].

Review: **correct**. Correct token cannot return and only ceases as subsequent SBA.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You may activate "Sacrifice this creature: Draw a card" on the turn you cast the creature, as long as you have priority.

Why: Summoning sickness restricts only activated abilities whose cost includes the tap symbol ({T}) or the untap symbol ({Q}), and it restricts attacking [CR 302.6]. A sacrifice cost is neither a tap nor an untap symbol, so the restriction does not apply [CR 602.5a]. You may activate an activated ability any time you have priority [CR 117.1b].

Review: **correct**. Correct sacrifice ability without tap-symbol cost can be activated despite summoning sickness.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. The legend rule is a state-based action performed automatically by the game; it does not use the stack, does not generate priority, and cannot be responded to. You make your choice of which permanent to keep as part of the state-based action itself, with no opportunity for anyone to cast an instant in between.

Why: State-based actions are performed by the game rules without a player receiving priority [CR 117.2]. Each time a player would get priority, the game first performs all applicable state-based actions as a single event before that player actually receives priority [CR 117.5]. Because no priority is granted and nothing is placed on the stack, there is no window in which a player could cast an instant [CR 117.1a]. The "choice" in the legend rule [CR 704.5j] is made as part of that automatic process, not as a response to a stack event.

Review: **correct**. Correct legend-rule SBA occurs before priority; no response window.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What quality does your creature have protection from (e.g., protection from black, protection from red, protection from a specific player)?
2. What is the removal spell? (Please attach it using card search or [[Exact Card Name].) Specifically: does it target a creature, is it a mass effect (e.g., "destroy all creatures"), and what color(s) does it have?

Review: **correct**. Appropriate clarification asks protection quality and removal spell/characteristics. Minor UI defect: closing `[[Exact Card Name]]` markup is missing in question 2; no rules error.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

