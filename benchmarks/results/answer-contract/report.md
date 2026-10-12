# answer-contract

Status: **complete** · implementation commit `1432d4563ff7bf68cd3eb6f58f4416ce23272ce7`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 1 |
| Correct and normally completed | 19/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 93.8% |
| Cases retrieving every expected evidence group | 17/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Reviewed fully correct | 19/20 reviewed |
| Reviewed accuracy | 95.0% |
| Mean reviewed rubric score | 95.0% |
| Median successful response | 12.11 s |
| p95 successful response | 17.99 s |
| Median first visible answer token | 10.55 s |

These are development scenarios, not a held-out accuracy claim. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.31 |
| 02-hold-priority (r1) | 100.0% | correct | 8.83 |
| 03-illegal-target (r1) | 100.0% | correct | 9.79 |
| 04-partial-targets (r1) | 100.0% | correct | 12.73 |
| 05-trample-indestructible (r1) | 100.0% | correct | 12.35 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 10.23 |
| 07-zero-toughness (r1) | 100.0% | correct | 17.03 |
| 08-commander-dies (r1) | 100.0% | correct | 17.99 |
| 09-commander-tax (r1) | 100.0% | correct | 7.59 |
| 10-rest-in-peace (r1) | 75.0% | correct | 9.26 |
| 11-token-doublers (r1) | 100.0% | correct | 12.06 |
| 12-replacement-choice (r1) | 100.0% | correct | 14.16 |
| 13-apnap (r1) | 100.0% | correct | 14.45 |
| 14-humility-anthem (r1) | 100.0% | correct | 12.95 |
| 15-own-hexproof (r1) | 100.0% | correct | 8.54 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 12.17 |
| 17-token-blink (r1) | 50.0% | incorrect | 39.84 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 9.25 |
| 19-legend-response (r1) | 50.0% | correct | 12.61 |
| 20-clarify-interaction (r1) | 100.0% | correct | 7.71 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

Ruling: No. Tapping a basic Forest for mana is an activated mana ability, and mana abilities don't go on the stack, so they can't be targeted, countered, or otherwise responded to.

Why: A basic Forest has the intrinsic ability "{T}: Add {G}" [CR 305.6], which meets all the criteria for an activated mana ability [CR 605.1a]. An activated mana ability doesn't go on the stack and resolves immediately after it is activated, so there is no window in which you could respond [CR 605.3b].

Review: **correct**. Correct activated mana ability ruling, immediate resolution, and supporting rules.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: Yes, you receive priority again before your opponent. No, the instant does not resolve immediately; it waits on the stack until all players pass in succession.

Why: Because you had priority when you cast the spell, you are the first to receive priority afterward [CR 117.3c]. The instant resolves only when every player passes in turn order without taking an action [CR 405.5] [CR 608.1], so your opponent gets a chance to respond before it resolves.

Review: **correct**. Correct priority returned to caster and all players passing. Both canonical references now fit; same mean recall conceals changing coverage between cases.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

Ruling: No, you do not draw a card. Defiant Strike does not resolve at all.

Why: Defiant Strike has a single target (the creature). If that creature has been destroyed and left the battlefield, it is no longer a legal target because it is no longer in the zone it was in when targeted [CR 608.2b]. Since all of the spell's targets are illegal, the spell doesn't resolve; it is removed from the stack and put into its owner's graveyard [CR 608.2b]. Because the spell never resolves, neither the +1/+0 nor the "Draw a card" instruction occurs. This is the same principle as the Sorin's Thirst example, where an illegal target means the controller doesn't gain life [CR 608.2b].

Review: **correct**. Correct no draw with sole target illegal and whole spell not resolving.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Ruling: Yes. The remaining legal creature takes 2 damage. The spell resolves normally because not all of its targets are illegal; the illegal target simply isn't affected.

Why: Under [CR 608.2b], a spell fails to resolve only if *all* its targets, for every instance of the word "target," are illegal. Here one target is still legal, so the spell resolves. The same rule then states that "illegal targets, if any, won't be affected by parts of a resolving spell's effect for which they're illegal," while the legal target is affected as normal. The Plague Spores example in [CR 608.2b] illustrates this exact pattern: the spell still resolves and affects the legal target even though the other target became illegal.

Review: **correct**. Correct remaining legal target takes damage and partial illegality does not stop resolution.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Ruling: Yes. You assign 2 damage (lethal damage) to the 2/2 blocker and 4 damage to the defending player.

Why: Trample requires you to assign "lethal damage" to each blocking creature before assigning excess to the player; lethal damage is simply damage equal to the creature's toughness (here, 2), regardless of whether the creature will actually be destroyed [CR 702.19b]. Indestructible prevents the permanent from being destroyed by lethal damage, but it does not change what counts as "lethal damage" for trample assignment purposes [CR 702.12b]. This is analogous to the protection example in the trample rule, where damage that will be prevented still satisfies the "lethal damage" threshold for the rest to go through [CR 702.19b].

Review: **correct**. Correct 2/4 assignment and indestructibility distinction with both operative definitions.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

Ruling: You can assign a maximum of 4 damage to the defending player (1 to the 8/8 blocker, 4 to the player).

Why: Deathtouch makes any nonzero amount of combat damage assigned to a creature count as lethal damage for the purpose of the trample check [CR 702.2c]. Trample requires that all blocking creatures be assigned lethal damage before excess damage may go to the defending player [CR 702.19b]. Since 1 damage satisfies the lethal-damage requirement, the remaining 4 of the 5 total combat damage [CR 510.1a] may be assigned to the defending player.

Review: **correct**. Correct maximum 4 and explicit nonzero deathtouch assignment rule.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

Ruling: No. The indestructible 3/3 that receives −3/−3 until end of turn becomes a 0/0 and is put into its owner's graveyard by the state-based action for a creature with toughness 0 or less. Indestructible does not prevent this.

Why: Indestructible specifically protects a permanent from being destroyed by lethal damage and lets it ignore the state-based action that checks for lethal damage [CR 702.12b]. A −3/−3 effect, however, reduces the creature's toughness to 0, which triggers the separate state-based action: "If a creature has toughness 0 or less, it's put into its owner's graveyard" [CR 704.5f]. Indestructible does not exempt a permanent from that action.

Review: **correct**. Correct 0/0 goes to graveyard; explicitly distinguishes lethal-damage destruction from zero-toughness action.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

Ruling: Yes, you may put your commander into the command zone, and yes, "dies" triggers still trigger.

Why: The commander is first put into the graveyard from the battlefield (the "dies" event occurs per [CR 700.4]), and then the state-based action in [CR 903.9a] lets its owner move it to the command zone. Because the zone-change event already happened, leaves-the-battlefield triggers (including "dies" triggers) fire normally [CR 603.6c] [CR 603.10a]. The state-based action that relocates the commander is a separate, subsequent action and does not prevent the trigger from having already been generated [CR 704.3].

Review: **correct**. Correct requested conclusions and repaired timing: explicitly puts state-based actions before waiting triggers are put on the stack, citing 704.3.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: The additional commander tax is {4}.

Why: Commander tax is calculated as an additional {2} for each previous time the player has cast that commander **from the command zone** that game [CR 903.8]. You have cast it from the command zone twice, so the tax is 2 × {2} = {4}. The cast from your hand does not count toward the tax because the rule specifically tracks casts "from the command zone" [CR 903.8].

Review: **correct**. Correct additional 4 and excludes hand cast. Citation ID now correct.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

Ruling: No. Blood Artist does not trigger.

Why: "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's replacement effect changes that event so the creature is exiled instead of being put into a graveyard [C1]. Because the creature is never actually put into a graveyard, the "dies" condition is never met, and Blood Artist's triggered ability ("Whenever this creature or another creature dies…") [C5] does not trigger.

Review: **correct**. Correct no Blood Artist trigger, exile replaces graveyard entry, and no dies event. Now finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

Ruling: You create **4** tokens. The doublers do **not** loop forever.

Why: Both Doubling Season [C1] and Anointed Procession [C7] are replacement effects modifying the same "create a token" event, so you choose the order in which they apply [CR 616.1e]. The first doubler doubles 1 → 2, then the process repeats with the remaining applicable effect [CR 616.1f], and the second doubler doubles 2 → 4. A replacement effect doesn't invoke itself repeatedly; it gets only one opportunity to affect an event [CR 614.5], so neither effect applies a second time and the loop terminates.

Review: **correct**. Correct four tokens and each replacement applies once to the event. Now finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

Ruling: You (the affected player, i.e., the one being dealt damage) choose which replacement effect applies first. The final damage can be either 7 or 8.

Why: Because neither effect is a self-replacement effect and none of the mandatory categories in 616.1a–d apply, the affected player simply picks any applicable replacement effect first [CR 616.1] [CR 616.1e]. The second effect then applies to the already-modified event [CR 616.1f]. Doubling is a replacement effect that makes the source deal twice the damage [CR 701.10g]. If you apply double first: 3 → 6, then +1 → 7. If you apply +1 first: 3 → 4, then double → 8. Both outcomes are legal depending on your choice.

Review: **correct**. Correct affected-player choice, both arithmetic orders, and once-per-effect restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Ruling: Bob's triggered ability resolves first.

Why: Under [CR 603.3b], when multiple triggered abilities are waiting and neither has a trigger condition of "another ability triggering," each player in APNAP order puts their qualifying abilities on the stack. Alice (the active player) acts first in APNAP order, placing her ability on the stack; Bob then places his on top of it, since each new object is put on top of all objects already there [CR 405.2]. The topmost object resolves first [CR 608.1], so Bob's ability resolves before Alice's.

Review: **correct**. Correct APNAP order and last-in-first-out resolution with supporting sources.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is 2/2. It does not matter which enchantment entered the battlefield first.

Why: Humility's "have base power and toughness 1/1" is a setting effect applied in Layer 7b [CR 613.4b], while Glorious Anthem's "get +1/+1" is a modifying effect applied in Layer 7c [CR 613.4c]. Because the two effects occupy different sublayers, the layer system fixes their order (7b before 7c) regardless of timestamp [CR 613.1], so the base is set to 1/1 and then +1/+1 is added, yielding 2/2. This mirrors the worked example in [CR 613.5] where a 7b setting effect establishes the value and 7c modifiers are then applied on top.

Review: **correct**. Correct 2/2 and sublayer order regardless of timestamps.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Ruling: Yes. You may target your own creature with hexproof using your own Giant Growth.

Why: Hexproof on a permanent means it "can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. The restriction applies only to opponents' spells and abilities, not to your own. Since Giant Growth is an instant, you may cast it any time you have priority [CR 117.1a], and its "target creature" requirement is satisfied by any creature, including one you control [CR 115.1a].

Review: **correct**. Correct own-creature targeting and opponents-only hexproof restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

Ruling: No. In the second combat damage step your 3/3 assigns no combat damage at all, so the player takes 0 damage.

Why: Because the attacker lacks trample, it can only assign combat damage to creatures blocking it. In the second combat damage step the 2/2 blocker is already in the graveyard, so no creatures are currently blocking the attacker, and a blocked creature with no blockers assigns no combat damage [CR 510.1c]. Trample is the ability that would let excess damage bypass blockers to the player [CR 702.19b], but your attacker does not have it.

Review: **correct**. Correct no second-step damage and continued blocked status without trample. The false first-strike damage sequence is gone.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

Ruling: It depends on the exact wording of the return instruction. If the effect says "return **that card** to the battlefield," the token does **not** return, because a token is not a card and the effect cannot find it. If the effect says "return **it** to the battlefield" or "return **that creature** to the battlefield," the token **does** return, because it still exists in the exile zone at that moment.

Why: A token is explicitly not a card, so any instruction that refers to "that card" cannot locate it [CR 111.6]. However, a token ceasing to exist in a zone other than the battlefield is a state-based action, not an immediate effect [CR 111.7]. State-based actions are only checked when a player would receive priority, which does not occur between the individual steps of a single resolution. The note in [CR 111.7] confirms a window exists where the token is in

Review: **incorrect**. Incorrect conditional return for tokens under return-it wording; 111.8 was again dropped by packing when the response contract consumed additional prompt space. Confuses existence before state-based checks with permission to change zones. The response also exhausts the 3500-token output budget and is cut off.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 111.8

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Ruling: Yes. You can activate "Sacrifice this creature: Draw a card" on the turn you cast the creature, as long as you have priority.

Why: Summoning sickness restricts only a creature's activated abilities that include the tap symbol ({T}) or untap symbol ({Q}) in their activation cost, and the creature's ability to attack [CR 302.6] [CR 602.5a]. A sacrifice cost contains neither symbol, so the restriction does not apply. You may activate the ability any time you have priority [CR 117.1b].

Review: **correct**. Correct activation when priority is available and absence of tap/untap symbols. No unsupported active-player assumption or immediate-draw claim.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

Ruling: No. You cannot cast an instant in response to the legend rule. The legend rule is a state-based action that is handled automatically before any player receives priority, so there is no window in which a player has priority and could cast an instant.

Why: The legend rule is a state-based action [CR 704.5j], and state-based actions are dealt with before a player would receive priority [CR 117.2d]. Each time a player would get priority, the game first performs all applicable state-based actions, then puts triggered abilities on the stack, and only then does the player actually receive priority [CR 117.5]. Because no player has priority at the moment the legend rule is applied, no player may cast a spell [CR 117.1]. The active player receives priority only after the state-based actions (including the legend rule) have been fully resolved [CR 117.3b].

Review: **correct**. Correct no response window, explicit state-based checks before priority, and choice of one legendary permanent. Uses alternative timing evidence 117.5 rather than canonical reference 704.3.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Need details:

1. What is the exact quality of your creature's protection (e.g., "protection from red," "protection from black," "protection from a specific card name," "protection from a player," "protection from everything")?
2. What is the removal spell (its name, color, and whether it targets the creature or affects it without targeting)?

Review: **correct**. Correctly asks only for protection quality and the removal spell’s identity/details. No hypothetical ruling or overbroad claim. This expected clarification is successful, not an abstention failure.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

