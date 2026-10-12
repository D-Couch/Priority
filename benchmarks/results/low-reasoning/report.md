# low-reasoning

Status: **complete** · implementation commit `6a176bd62b197dfc27ebe1eefa20c8adc2923674`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Mean expected-evidence recall | 63.3% |
| Cases retrieving every expected evidence group | 8/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 97.6% |
| Reviewed fully correct | 16/20 reviewed |
| Reviewed accuracy | 80.0% |
| Mean reviewed rubric score | 87.5% |
| Median successful response | 12.37 s |
| p95 successful response | 18.61 s |
| Median first visible answer token | 9.40 s |

These are development scenarios, not a held-out accuracy claim. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 5.36 |
| 02-hold-priority (r1) | 0.0% | abstained | 13.99 |
| 03-illegal-target (r1) | 100.0% | correct | 6.33 |
| 04-partial-targets (r1) | 100.0% | correct | 9.50 |
| 05-trample-indestructible (r1) | 50.0% | correct | 11.06 |
| 06-deathtouch-trample (r1) | 50.0% | correct | 16.77 |
| 07-zero-toughness (r1) | 0.0% | incorrect | 17.79 |
| 08-commander-dies (r1) | 100.0% | correct | 14.48 |
| 09-commander-tax (r1) | 100.0% | correct | 6.41 |
| 10-rest-in-peace (r1) | 75.0% | correct | 8.30 |
| 11-token-doublers (r1) | 66.7% | correct | 16.80 |
| 12-replacement-choice (r1) | 100.0% | correct | 12.01 |
| 13-apnap (r1) | 50.0% | correct | 10.65 |
| 14-humility-anthem (r1) | 75.0% | correct | 17.94 |
| 15-own-hexproof (r1) | 100.0% | correct | 6.87 |
| 16-first-strike-blocker (r1) | 50.0% | correct | 12.73 |
| 17-token-blink (r1) | 0.0% | partial | 18.61 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 8.09 |
| 19-legend-response (r1) | 50.0% | correct | 23.36 |
| 20-clarify-interaction (r1) | 0.0% | partial | 13.05 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

**No, you cannot respond to your opponent tapping a basic Forest for mana.**

A basic Forest has the intrinsic ability "{T}: Add {G}" [CR 305.6]. When your opponent activates that ability, it is an activated mana ability. Activated mana abilities don't go on the stack, so they can't be targeted, countered, or otherwise responded to. They resolve immediately after they are activated [CR 605.3b].

This means there is no window for either player to cast instants or activate abilities in response to the tap-for-mana action itself.

Review: **correct**. Correct mana-ability ruling and immediate resolution without the stack.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

## Ruling

**The instant does not resolve immediately.** It is placed on the stack and will resolve later, after priority has passed to your opponent (and they choose not to respond).

**Regarding priority after casting:** The provided reference excerpts do not include the specific rule that states the player who cast the spell receives priority again after casting. This is a standard part of the turn flow, but I can't cite a supporting excerpt from the supplied references for that particular claim.

## Explanation

Casting an instant spell uses the stack — it is not an immediate effect. The spell is put on the stack and will "eventually resolve and have its effect" [CR 701.5a]. Because it uses the stack, your opponent will have the opportunity to respond before it resolves [CR 304.1].

This is in contrast to mana abilities, which resolve immediately without waiting for priority [CR 405.6c], and triggered mana abilities, which also resolve immediately [CR 605.4a].

## What's Missing

The rule that explicitly grants priority back to the player who cast a spell (typically found in rule 117.3) is not included in the supplied excerpts. If you'd like, I can address that aspect if you can provide the relevant rule text, or I can note that this is a well-established part of the normal turn sequence.

Review: **abstained**. Declines to establish who receives priority without supporting excerpts. Does not explain all players passing in succession. Evidence-limited abstention.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 117.3c, 117.4

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

**No, you do not draw a card.**

Defiant Strike has a single target (the creature). If that creature is destroyed in response, it is no longer a legal target when the spell tries to resolve. Since all of its targets are illegal, the spell doesn't resolve at all—it's removed from the stack and put into its owner's graveyard. Neither the +1/+0 buff nor the card draw occurs. [CR 608.2b]

This is confirmed by the card-specific ruling: "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

Review: **correct**. Correctly denies drawing because the only target is illegal and the entire spell does not resolve.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

**Yes, the remaining legal creature takes 2 damage.**

**Explanation:**

When the spell resolves, it checks whether its targets are still legal. Since one target left the battlefield, that target is now illegal. However, the other target is still legal, so **not all** targets are illegal. The spell therefore resolves normally.

Per the rules, illegal targets simply aren't affected by the spell's effect, while legal targets are affected as normal. So the spell deals 2 damage to the one creature that is still a legal target, and does nothing to the one that left the battlefield.

**Supporting citations:**

- [CR 608.2b]: "If all its targets, for every instance of the word 'target,' are now illegal, the spell or ability doesn't resolve… Otherwise, the spell or ability will resolve normally. Illegal targets, if any, won't be affected by parts of a resolving spell's effect for which they're illegal."

This is the same principle illustrated by the Plague Spores example in that rule: if one target becomes illegal but another remains legal, the spell still resolves and affects the legal target.

Review: **correct**. Correctly resolves against the remaining legal target for 2 damage.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Yes.** You must assign at least 2 damage to the blocker (lethal damage to a 2/2), and you may assign the remaining 4 to the defending player.

**Why indestructible doesn't matter here:** When checking for "assigned lethal damage" under trample, the rules explicitly say to ignore "any abilities or effects that might change the amount of damage that's actually dealt" [CR 702.19b]. Indestructible doesn't change how much damage is dealt—it only prevents the creature from being destroyed as a result. A 2/2 still requires 2 damage to be considered "lethally damaged" for trample purposes, regardless of indestructible.

This is directly analogous to the provided example: a 6/6 with trample blocked by a 2/2 with protection from green still requires 2 damage assigned to the blocker, with the rest going to the player [CR 702.19b].

Review: **correct**. Correct 2/4 assignment and distinction between lethal assignment and indestructibility.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 702.12b

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

## Ruling

**Maximum damage to the defending player: 4.**

## Explanation

Your 5/5 with trample must first assign **lethal damage** to the blocking creature before any excess can go to the player. [CR 702.19b]

Because your creature has **deathtouch**, any amount of damage it deals to a creature is considered lethal damage. Therefore, only **1 damage** needs to be assigned to the 8/8 blocker to satisfy the "lethal damage" requirement. The remaining **4 damage** may be assigned to the defending player.

The exclusion in [CR 702.19b] — "not any abilities or effects that might change the amount of damage that's actually dealt" — refers to things like damage prevention (e.g., protection) or damage increase effects. Deathtouch doesn't change the *amount* of damage dealt; it changes what threshold of damage counts as lethal, so it is properly taken into account when determining how much must be assigned to the blocker.

**Summary:** 1 to the blocker (lethal via deathtouch) + 4 to the player = 5 total.

Review: **correct**. Correct 1/4 assignment using deathtouch. The canonical deathtouch assignment rule is still absent from retrieval; correct conclusion does not establish complete citation support.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 702.2c

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

**Yes, the indestructible creature survives.**

A 3/3 that gets −3/−3 becomes a 0/3. Normally, a creature with toughness 0 or less is destroyed by a state-based action. However, **indestructible** means the permanent can't be destroyed, and this protection applies to *all* sources of destruction, including state-based actions. The creature remains on the battlefield as a 0/3 until the "until end of turn" effect expires during the cleanup step [CR 514.2].

**Important distinction:** Indestructible does *not* protect the creature from being dealt damage, exiled, or otherwise removed from the battlefield by means other than "destroy." It only prevents the specific action of destruction.

**Citation note:** The reference excerpts include only the heading for [CR 702.12] (Indestructible) without the full rule text, and do not include rule 704.5g (the state-based action for zero-toughness creatures). The answer above reflects the established interaction between these two rules, but I'm flagging that the specific rule text isn't fully present in the supplied references.

Review: **incorrect**. Incorrect survival ruling, arithmetic (3/3 minus 3/3 is 0/0, not 0/3), and zero-toughness action characterized as destruction. Confident misinformation replaces the previous empty response.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.5f, 702.12b

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

## Ruling

**Yes to both.** Your commander can be moved to the command zone, and "when it dies" abilities still trigger.

## Explanation

**Moving to the command zone:** The commander's return to the command zone is a **state-based action**, not a replacement effect. Per [CR 903.9a], if a commander is in a graveyard and was put there since the last time state-based actions were checked, its owner *may* put it into the command zone. This happens *after* the event of being put into the graveyard has already occurred.

**"Dies" triggers still fire:** The term "dies" means "is put into a graveyard from the battlefield" [CR 700.4]. That event did happen — your commander was put into the graveyard from the battlefield. Leaves-the-battlefield triggers (including "dies" triggers) look back in time to determine whether they trigger [CR 603.10a], and they trigger when a permanent moves from the battlefield to another zone [CR 603.6c]. The subsequent state-based action that moves the commander to the command zone does not retroactively undo the trigger condition that was already met.

**Key distinction:** If a *replacement effect* had said "instead, put it into the command zone," the card would never have entered the graveyard, and "dies" would not have triggered. But the commander's ability is a state-based action that applies *after* the zone change, so the trigger fires normally.

Review: **correct**. Correct graveyard entry, dies triggers, and subsequent optional command-zone move as a state-based action.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

**Ruling:** The additional commander tax is **{4}**.

**Explanation:** Commander tax is calculated based solely on the number of times you have previously cast that commander *from the command zone* that game. Casting it from your hand does not count toward the tax.

You have cast it from the command zone **twice** previously, so the next cast from the command zone costs an additional 2 × {2} = **{4}**.

[C1] (CR 903.8): "A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game."

Review: **correct**. Correct additional tax of 4 excluding the hand cast. Uses nonexistent [C1] for CR 903.8: substantive criteria pass, but citation-ID precision separately records this defect.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

**No, Blood Artist does not trigger.**

**Explanation:**

Blood Artist's ability triggers "whenever this creature or another creature **dies**." The term "dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4].

Rest in Peace's static ability replaces the event: "If a card or token would be put into a graveyard from anywhere, exile it instead" [C1]. So when the creature is destroyed, it is exiled rather than being put into a graveyard. Since it is never actually put into a graveyard, it does not "die," and Blood Artist's trigger condition is never met.

This is confirmed directly by the card-specific ruling:

> "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard." [C2]

Review: **correct**. Correct exile replacement and no dies trigger, supported by Oracle text and dies definition.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

## Ruling

You create **4 tokens**. The doublers do not loop.

## Explanation

Both Doubling Season and Anointed Procession are replacement effects that modify the same event: "an effect would create one or more tokens under your control." [C1] [C7]

When multiple replacement effects of this type apply to the same event, they multiply the original number rather than iterating. The established pattern from the rulings is:

- Two doublers → **4×** the original number [C2] [C11]
- Three doublers → **8×** the original number [C2] [C11]

This is the same whether the doublers are all copies of the same card or a mix of Doubling Season and Anointed Procession. With one of each, you get 1 × 2 × 2 = **4 tokens**.

They do not loop because a replacement effect modifies the original "would create" event into a different outcome. The resulting event (creating 4 tokens) is not itself a new "would create" event that re-triggers the replacement effects. The multiplication is applied once to the original event, not recursively.

Review: **correct**. Correct four tokens and no recursion. Describes multiplication once rather than the precise sequential replacement process; in this two-doubler context it conveys each effect applies once.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.5

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

## Ruling

**You (the affected player) choose the order, and the final damage can be either 7 or 8.**

## Explanation

When two or more replacement effects are attempting to modify the same damage event, the affected player chooses which one applies first [CR 616.1]. Each effect gets exactly one opportunity to affect the event or the modified event [CR 614.5].

The two possible orderings:

| Order applied | Calculation | Result |
|---|---|---|
| Increase by 1, then double | (3 + 1) × 2 | **8** |
| Double, then increase by 1 | (3 × 2) + 1 | **7** |

Doubling damage is explicitly a replacement effect [CR 701.10g], and the user has stated the "+1" effect is also a replacement effect (not a prevention effect and not a self-replacement effect), so both are eligible for the choice under rule 616.1.

Since you are the affected player, you pick whichever order gives you the more favorable outcome (or the less favorable one, if that's strategically better).

Review: **correct**. Correct affected-player choice and both arithmetic orders yielding 7 or 8.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

**Bob's triggered ability resolves first.**

**Explanation:**

When multiple triggered abilities are waiting to be placed on the stack, they are put on in APNAP (Active Player, then Non-Active Player) order. Since it is Alice's turn, she is the active player and Bob is the non-active player.

The process works as follows:

1. Alice (AP) puts her triggered ability on the stack first — it becomes the bottom object.
2. Bob (NAP) puts his triggered ability on the stack second — it becomes the top object.

Since the top of the stack resolves first, Bob's ability resolves before Alice's.

This is the standard "APNAP" ordering rule for triggered abilities: the active player's triggers go on the stack first (and thus resolve last), giving the non-active player the opportunity to respond.

[CR 603.3b]

Review: **correct**. Correct APNAP stacking and Bob resolving first.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 405.2|608.1

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

## Ruling

Your creature is **2/2**, and it does **not** matter which enchantment entered the battlefield first.

## Explanation

The two effects operate in different sublayers of layer 7:

1. **Humility** ("have base power and toughness 1/1") is a *set* effect, applied in **layer 7b**.
2. **Glorious Anthem** ("get +1/+1") is a *modify* effect, applied in **layer 7c**.

Because sublayers are applied in a fixed order (7b before 7c), the result is always:

- 7b: Base P/T is set to 1/1 (Humility)
- 7c: +1/+1 is added (Glorious Anthem)
- **Final: 2/2**

Timestamp order only matters *within* the same sublayer [CR 613.4]. Since these effects are in different sublayers, their relative timestamps are irrelevant.

This is distinct from the Humility + Opalescence interaction, where both are "set" effects in the same sublayer (7b) and timestamp order *does* determine the outcome [C2].

## Citations

- [CR 613.4] – "Within layer 7, apply effects in a series of sublayers in the order described below. Within each sublayer, apply effects in timestamp order."
- [CR 613.4c] – "Layer 7c: Effects and counters that modify power and/or toughness (but don't set power and/or toughness to a specific number or value) are applied."
- [CR 208.4a] – "Effects that set a creature's power and/or toughness to specific values may refer to base power and/or toughness. Other continuous effects may further modify the creature's power and toughness."
- [C2] – Confirms that two "set" effects in the same sublayer (Humility vs. Opalescence) are resolved by timestamp, illustrating why the sublayer distinction is what matters here.

Review: **correct**. Correct 2/2 and base-setting before modification independently of timestamps.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 613.4b

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

**Yes, you may target your own hexproof creature with your own Giant Growth.**

Hexproof on a permanent means "This permanent can't be the target of spells or abilities **your opponents** control." [CR 702.11b]

Since you control both the creature and the Giant Growth spell, the hexproof restriction does not apply to you. You are free to target your own creature with your own spell.

Giant Growth simply reads "Target creature gets +3/+3 until end of turn." [C1] There is no additional restriction preventing you from choosing your own creature as the target.

Review: **correct**. Correct own-creature targeting because hexproof restricts opponents.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**No.** Without trample, your 3/3 deals no combat damage to the player in the second combat damage step.

**Explanation:**

In the first combat damage step, your 3/3 with double strike deals 3 damage to the 2/2 blocker, which is lethal and the blocker dies. In the second combat damage step, your creature still assigns combat damage (double strike creatures deal damage in both steps [CR 702.4b]), but it has no one to assign it to.

The critical rule is that **trample** is the ability that permits an attacking creature to assign excess combat damage to the player or planeswalker it's attacking [CR 702.19b]. Without trample, an attacking creature can only deal combat damage to creatures blocking it. Since the blocker is dead and no other creatures are blocking, your attacker simply deals no combat damage in the second step.

**Bottom line:** Double strike lets the creature deal damage in both steps, but it doesn't create a path for that damage to reach the player. You need trample for that.

Review: **correct**. Correct no player damage and no remaining blocker to assign to without trample. The explanation conveys continued blocked status implicitly. Read the attacking-creature restriction in the stated blocked-combat context, not as a rule for unblocked attackers.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 510.1c

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**Ruling: No, the token does not return to the battlefield.**

Once a token leaves the battlefield to any zone (including exile), it ceases to exist. There is no longer an object that can be the target or subject of a "return to the battlefield" effect. The second part of the resolution simply has nothing to act on.

**What's missing from the reference excerpts:** The specific rule that establishes this — that a token in a zone other than the battlefield ceases to exist (rule 704.5m) — is not included in the supplied excerpts. None of the provided rules directly address the fate of a token after it leaves the battlefield. The excerpts cover token creation, copying, and replacement effects involving tokens, but not the "dying" of tokens.

If you'd like, I can work with additional reference material that includes the token-existence rule to provide a fully cited explanation.

Review: **partial**. Correct no return, but incorrectly says the token immediately ceases to exist during resolution. Misses the prohibition on changing zones again before state-based actions. Cites the wrong unprovided rule number.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 111.8, 111.7

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

**Yes, you can activate it this turn.**

Summoning sickness only restricts two things:

1. Activated abilities with the **tap symbol ({T})** or **untap symbol ({Q})** in their activation cost.
2. Attacking.

[CR 302.6]

Your ability's cost is "Sacrifice this creature," which contains neither the tap nor the untap symbol. It is therefore not subject to the summoning sickness restriction. As long as you have priority, you may activate it on the same turn you cast the creature. [CR 117.1]

**In short:** Summoning sickness is not a blanket "can't activate abilities this turn" rule—it specifically targets tap/untap costs and attacking. A sacrifice cost is unaffected.

Review: **correct**. Correct sacrifice activation without tap/untap-symbol restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

**Ruling: No.** You cannot cast an instant "in response" to the legend rule. You must choose which legendary permanent to keep as part of the state-based action itself, with no opportunity to intervene.

**Explanation:**

The legend rule is a **state-based action** (it appears under rule 704.5, "The state-based actions are as follows" [CR 704.5], specifically at [CR 704.5j]). State-based actions do not use the stack and do not generate a priority window. They are checked and resolved immediately when the game state meets the condition.

The sequence after a spell resolves that causes you to control two legendary permanents with the same name is:

1. The spell resolves.
2. The game checks state-based actions **before** giving priority to any player.
3. The legend rule applies: you choose one to keep, and the rest are put into their owners' graveyards [CR 704.5j].
4. Only then is priority given, at which point instants could be cast.

Because there is no stack object and no priority window between the condition being met and the state-based action resolving, there is no moment at which you could cast an instant "in response" to the legend rule.

**Practical note:** If you want to cast an instant that would save one of the creatures (e.g., a spell that changes its name or grants it a different characteristic), you would need to do so *before* the spell that creates the duplicate resolves, or find a way to have priority at a point where the state-based action hasn't yet been checked.

Review: **correct**. Correct legend action before priority and no response window. General immediate-check phrasing is imprecise; the explicit sequence correctly specifies after resolution, before priority.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

**It depends on what your creature has protection *from* and what the removal spell is.**

Protection from a quality (e.g., "protection from red," "protection from artifacts") means the creature:

- Can't be **targeted** by spells or abilities with that quality
- Can't be **enchanted** by Auras with that quality
- Can't be **equipped** by Equipment with that quality
- Can't be **blocked** by creatures with that quality
- All **damage** from sources with that quality is prevented

This is illustrated by the "protection from everything" rule, which applies all of these protections without restriction: [CR 702.16j]

So the critical question is: **does the removal spell have the quality your creature has protection from?**

- If your creature has "protection from red" and the removal spell is red → the spell **can't target** your creature, so it's safe.
- If your creature has "protection from red" and the removal spell is blue → the spell **can** target and destroy your creature.

**To give you a definitive answer, I need to know:**
1. What exactly is your creature's protection text? (e.g., "protection from red," "protection from black," "protection from artifacts")
2. What is the removal spell? (You can attach it using [[Exact Card Name]] or card search.)

Review: **partial**. Asks for protection quality and spell, but asserts a red removal spell means the creature is safe. Non-targeted destruction can still remove it. This unsupported assurance fails full correctness despite satisfying both clarification criteria.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 702.16b|702.16e

