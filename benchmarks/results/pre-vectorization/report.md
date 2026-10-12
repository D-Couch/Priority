# pre-vectorization

Status: **complete** · implementation commit `98cd7e431879a9817252d623a3ca5fe5373a06ea`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 14/20 |
| Request errors | 6 |
| Mean expected-evidence recall | 63.3% |
| Cases retrieving every expected evidence group | 8/20 |
| Answers with citations | 14/14 |
| Citation ID validity (not semantic support) | 100.0% |
| Reviewed fully correct | 12/20 reviewed |
| Reviewed accuracy | 60.0% |
| Mean reviewed rubric score | 65.0% |
| Median successful response | 20.02 s |
| p95 successful response | 41.05 s |
| Median first visible answer token | 18.29 s |

These are development scenarios, not a held-out accuracy claim. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 10.72 |
| 02-hold-priority (r1) | 0.0% | abstained | 41.05 |
| 03-illegal-target (r1) | 100.0% | correct | 21.57 |
| 04-partial-targets (r1) | 100.0% | correct | 13.06 |
| 05-trample-indestructible (r1) | 50.0% | correct | 16.32 |
| 06-deathtouch-trample (r1) | 50.0% | request error | 44.46 |
| 07-zero-toughness (r1) | 0.0% | request error | 43.81 |
| 08-commander-dies (r1) | 100.0% | request error | 43.84 |
| 09-commander-tax (r1) | 100.0% | correct | 10.11 |
| 10-rest-in-peace (r1) | 75.0% | correct | 10.15 |
| 11-token-doublers (r1) | 66.7% | request error | 44.22 |
| 12-replacement-choice (r1) | 100.0% | correct | 37.67 |
| 13-apnap (r1) | 50.0% | correct | 32.28 |
| 14-humility-anthem (r1) | 75.0% | correct | 38.68 |
| 15-own-hexproof (r1) | 100.0% | correct | 18.48 |
| 16-first-strike-blocker (r1) | 50.0% | request error | 45.71 |
| 17-token-blink (r1) | 0.0% | request error | 44.37 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 11.92 |
| 19-legend-response (r1) | 50.0% | correct | 36.12 |
| 20-clarify-interaction (r1) | 0.0% | partial | 29.69 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

No. A basic Forest has the intrinsic ability “{T}: Add {G}” [CR 305.6]. When your opponent activates that mana ability, it doesn’t go on the stack, so it can’t be targeted, countered, or otherwise responded to; it resolves immediately after it is activated [CR 605.3b].

So you don’t get a chance to respond to the tap itself. If the Forest is tapped as part of casting a spell, you can still respond to the spell on the stack, but not to the mana ability.

Review: **correct**. Correctly says the activated mana ability cannot be responded to and resolves without the stack, supported by CR 605.3b. The additional spell-response distinction is consistent with priority rules.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

Ruling: The instant does **not** resolve immediately. It goes on the stack and resolves later. The supplied excerpts do **not** establish whether you get priority again before your opponent after casting; that information is missing.

You may cast an instant when you have priority [CR 117.1a]. Casting an instant as a spell uses the stack [CR 304.1]. Casting a spell means putting it on the stack and paying its costs so that it will eventually resolve [CR 701.5a]. Therefore, the instant is not resolved immediately upon being cast. To answer the priority-after-casting part, we would need a supplied rule about who receives priority after a spell is cast.

Review: **abstained**. Correctly says the instant does not immediately resolve, but explicitly declines to answer who receives priority and never explains the all-players-pass condition. Both authored requirements remain unmet. Retrieval omitted CR 117.3c and 117.4; this is an evidence-limited abstention, not a false positive.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 117.3c, 117.4

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

No. If your creature is destroyed in response, **Defiant Strike** will not resolve and you will not draw a card.

**Defiant Strike** targets a creature and says “Draw a card” [C1]. If your opponent casts a spell or ability that destroys that creature in response, that response resolves first [CR 117.7]. By the time **Defiant Strike** tries to resolve, the creature is no longer in the battlefield, so it is an illegal target [CR 608.2b]. If all of a spell’s targets are illegal, the spell doesn’t resolve [CR 608.2b].

The dated card-specific ruling confirms this: if the target creature is illegal by the time **Defiant Strike** tries to resolve, the spell won’t resolve and you won’t draw a card [C2].

Review: **correct**. No card draw; the only target is illegal and the whole spell does not resolve. CR 608.2b and Defiant Strike Oracle text/card ruling support the result. The wording about casting an ability is imprecise, but does not change the adjudication.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

Yes. If one target is illegal but the other remains legal, the spell still resolves and deals 2 damage to the remaining legal creature.

The spell does not fizzle because not all of its targets are illegal. The illegal target simply isn’t affected by the part of the effect that would deal damage to it, while the legal target is still affected.

Supporting excerpt: [CR 608.2b]

Review: **correct**. Correctly deals 2 damage to the surviving legal target while ignoring the illegal target; CR 608.2b supports both requirements.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

Yes.

Trample changes how an attacking creature assigns combat damage: you must first assign lethal damage to the creature(s) blocking it, and only then may you assign excess damage to the defending player [CR 702.19a] [CR 702.19b]. An undamaged 2/2 blocker needs 2 assigned damage to be assigned lethal damage, so assigning 2 to the indestructible blocker and the remaining 4 to the defending player is legal [CR 702.19b]. Indestructible does not reduce the amount of damage that must be assigned to the blocker; it only affects what happens after damage is dealt [CR 702.19b].

Review: **correct**. Correctly allows 2 damage to the undamaged blocker and 4 to the player. The explanation distinguishes assignment from indestructibility in this combat. CR 702.19b supports the assignment; the reference group for the explicit indestructible definition (702.12b) was missed, so retrieval recall is only 50% despite a correct ruling.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 702.12b

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

(No answer.)

Request error: No final answer returned

Review: **error**. No visible final answer was returned. The model exhausted its output limit; the app emitted length/empty-answer warnings. Retrieval also missed CR 702.2c. This is a failed request for evaluation purposes, not a correct abstention.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 702.2c

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

(No answer.)

Request error: No final answer returned

Review: **error**. No visible final answer; output-limit and empty-answer warnings. Retrieval omitted both required rule groups, 704.5f and 702.12b. Neither answer criterion can receive credit.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.5f, 702.12b

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

(No answer.)

Request error: No final answer returned

Review: **error**. No visible final answer; output-limit and empty-answer warnings. All expected evidence was retrieved, including the graveyard-to-command-zone rule and dies definition, so the generation failure cannot be explained solely by a retrieval miss.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

Ruling: **{4} additional commander tax** applies to your next cast from the command zone.

Commander tax is an additional **{2} for each previous time you have cast that commander from the command zone that game** [CR 903.8]. You have cast it from the command zone twice, so the next cast from the command zone costs an extra **{4}**. Casting it from your hand does not increase the commander tax.

Review: **correct**. Gives {4} additional tax and explicitly excludes the cast from hand; CR 903.8 supports both.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

No. Blood Artist does not trigger.

Blood Artist triggers when a creature **dies**, and “dies” means a creature is put into a graveyard from the battlefield [CR 700.4]. Rest in Peace replaces that event: if a card or token would be put into a graveyard from anywhere, it is exiled instead [C1]. Because the creature is exiled rather than put into a graveyard, it does not die, so Blood Artist’s trigger condition is not met [C2].

Review: **correct**. Correctly says Blood Artist does not trigger because Rest in Peace replaces the graveyard move with exile. The card text and CR 700.4 establish the result even though canonical replacement rule 614.6 was not retrieved.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

(No answer.)

Request error: No final answer returned

Review: **error**. No visible final answer; the output limit was reached. Both card texts were retrieved but CR 614.5, which explains each replacement effect applies only once, was missed. Record the generation failure without inferring that retrieval alone caused it.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.5

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

Ruling: **You choose which replacement effect applies first**, and the final damage **can be either 7 or 8**.

Explanation:

- Both effects are replacement effects modifying damage from a source [CR 614.2].
- The double effect makes the source deal twice that much damage [CR 701.10g].
- When multiple replacement and/or prevention effects modify the same event, the affected player chooses one to apply [CR 616.1]. Since the damage is being dealt to you, you make the choice.
- Because neither effect is a self-replacement effect, no self-replacement effect has to be applied first [CR 616.1a].
- The effect you choose modifies the damage event, and the other replacement effect then applies to the modified event [CR 614.5].

So, assuming the second effect simply increases the damage amount by 1:

- If you choose **double first**: 3 → 6, then +1 → **7**.
- If you choose **+1 first**: 3 → 4, then double → **8**.

Review: **correct**. Correctly assigns the choice to the affected player under CR 616.1 and calculates both 3×2+1=7 and (3+1)×2=8. The ordinary-replacement assumptions remove the special-order exceptions.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

Bob’s trigger resolves first.

Assuming both are ordinary triggered abilities that have already triggered and are waiting to be put on the stack, they are placed on the stack in APNAP order. Since it is Alice’s turn, Alice is the active player, so Alice puts her ability on the stack first and Bob puts his second [CR 603.3b]. Each triggered ability becomes the topmost object on the stack when it is put there [CR 603.3]. Therefore Bob’s ability is on top and, with no responses, resolves before Alice’s.

Review: **correct**. Correctly puts Alice’s trigger on first and Bob’s on top, resolving Bob’s first. CR 603.3b and the retrieved 603.3 support the stacking explanation. The authored generic stack-resolution group was missed, illustrating that canonical evidence recall is not equivalent to answer accuracy.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 405.2|608.1

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

Ruling: The creature is **2/2**. It does **not** matter whether **Humility** or **Glorious Anthem** entered the battlefield first.

Explanation:

- **Humility**’s Oracle text says all creatures “have base power and toughness 1/1” [C1].
- **Glorious Anthem**’s Oracle text says creatures you control “get +1/+1” [C5].
- Base power and toughness is determined after effects that set power/toughness or base power/toughness, ignoring effects that merely modify power/toughness [CR 208.4b]. Other continuous effects may further modify it [CR 208.4a].
- Continuous effects are applied in layers. Within layer 7, effects that modify power/toughness but do not set it to a specific value are applied in sublayer 7c [CR 613.1], [CR 613.4], [CR 613.4c].
- Dated Humility rulings show Humility’s power/toughness-setting effect is treated in layer 7b [C2].

So the order is:

1. Humility makes the creature’s base power/toughness **1/1** [C1], [C2].
2. Glorious Anthem’s **+1/+1** modifier applies [C5], [CR 613.4c].

Result: **1/1 + 1/+1 = 2/2**.

Timestamp order only matters within the same sublayer [CR 613.4]. Since Humility’s base-setting effect and Glorious Anthem’s modifier are in different sublayers, their entry order does not change the result.

Review: **correct**. Correctly gives 2/2 independent of entry order. The answer explains base-setting in 7b before Anthem’s 7c modifier, using the Humility card ruling and CR 613.4c. It missed canonical 613.4b but obtained the relevant base-setting information from the card ruling.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 613.4b

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

Yes.

Giant Growth’s Oracle text says: “Target creature gets +3/+3 until end of turn.” [C1]

Hexproof on a permanent means: “This permanent can’t be the target of spells or abilities your opponents control.” [CR 702.11b]

Since you control the creature and you are casting Giant Growth, it is not an opponent’s spell, so hexproof does not prevent you from targeting it. If the creature instead has “hexproof from [quality],” it only blocks opponents’ spells or abilities from that quality. [CR 702.11d]

Assuming the creature is still a legal target when Giant Growth resolves, it will get +3/+3 until end of turn. [CR 608.2b]

Review: **correct**. Correctly allows the player’s own Giant Growth to target their hexproof creature. CR 702.11b restricts opponents only; the final legality caveat is appropriate.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

(No answer.)

Request error: No final answer returned

Review: **error**. No visible final answer; output-limit and empty-answer warnings. The reference that a blocked attacker without blockers assigns no damage (CR 510.1c) was not retrieved.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 510.1c

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

(No answer.)

Request error: No final answer returned

Review: **error**. No visible final answer; output-limit and empty-answer warnings. Retrieval missed both token rules, including the prohibition on a token changing zones again before state-based actions.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 111.8, 111.7

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

Yes. Summoning sickness only restricts a creature’s activated abilities that include the tap symbol `{T}` or untap symbol `{Q}` in their activation cost, and it restricts attacking [CR 302.6]. Since “Sacrifice this creature: Draw a card” has no tap or untap symbol in its cost, that restriction does not apply. If you have priority, you may activate the ability [CR 117.1].

Review: **correct**. Correctly allows the sacrifice ability and distinguishes tap/untap-symbol restrictions from other activation costs. CR 302.6 directly supports the explanation.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

No. The legend rule is a state-based action, not something you respond to. When you control two legendary permanents with the same name, the state-based action makes you choose one of them, and the rest are put into their owners’ graveyards [CR 704.5j]. It is listed among the state-based actions [CR 704.5], and legendary permanents are subject to it [CR 205.4d].

The supplied excerpts do not provide a response window for the legend rule. Casting an instant is an action taken by a player with priority [CR 117.1], but no priority is granted to respond to the legend rule before you choose which permanent to keep.

Review: **correct**. Correctly says there is no response window before choosing one legendary permanent to keep. It identifies the legend rule as a state-based action under CR 704.5j. The canonical timing rule 704.3 was missed by retrieval, but the timing conclusion is correct.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

Not necessarily. It depends on **what your creature is protected from** and **what the removal spell does**.

- If your creature has **protection from everything**, it can’t be targeted by spells or abilities, can’t be enchanted by Auras, and all damage that would be dealt to it is prevented. [CR 702.16j]
- If your creature has **protection from that opponent**, it can’t be targeted by spells or abilities that opponent controls, can’t be enchanted by Auras that opponent controls, and damage from sources controlled by that opponent is prevented. [CR 702.16k]
- If it has protection from multiple qualities, those work as separate protection abilities. [CR 702.16g]

So if the removal spell **targets** your creature or **deals damage** to it, and your creature has protection from everything or from that opponent, it is safe from that spell. But if the removal spell doesn’t target it, doesn’t deal damage, or doesn’t have the protected quality, the supplied references don’t establish that it’s safe.

Please attach the creature and the removal spell using card search or `[[Exact Card Name]]`, and tell me:
1. What the creature’s protection is from.  
2. Whether the removal spell targeted the creature.  
3. Whether the removal spell dealt damage.

Review: **partial**. Asks for the creature, removal spell, and protection quality, so both clarification criteria pass. However, the extra assurance that a damage spell is safe against protection from everything/the opponent is too broad without knowing the spell: protection prevents damage (702.16e), and unpreventable damage bypasses prevention (615.12 in the same frozen corpus). This unsupported blanket assurance prevents a fully-correct grade; citation-ID validity alone would miss it.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 702.16b|702.16e

