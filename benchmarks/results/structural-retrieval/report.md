# structural-retrieval

Status: **complete** · implementation commit `43d9d2a2dc1c68f5f4eaf5ea440f0e418c5b8d52`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Mean expected-evidence recall | 96.2% |
| Cases retrieving every expected evidence group | 18/20 |
| Answers with citations | 19/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Reviewed fully correct | 18/20 reviewed |
| Reviewed accuracy | 90.0% |
| Mean reviewed rubric score | 97.5% |
| Median successful response | 11.22 s |
| p95 successful response | 16.16 s |
| Median first visible answer token | 8.88 s |

These are development scenarios, not a held-out accuracy claim. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.27 |
| 02-hold-priority (r1) | 100.0% | correct | 9.77 |
| 03-illegal-target (r1) | 100.0% | correct | 9.34 |
| 04-partial-targets (r1) | 100.0% | correct | 11.03 |
| 05-trample-indestructible (r1) | 100.0% | correct | 16.16 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 11.44 |
| 07-zero-toughness (r1) | 100.0% | correct | 9.98 |
| 08-commander-dies (r1) | 100.0% | partial | 17.85 |
| 09-commander-tax (r1) | 100.0% | correct | 8.17 |
| 10-rest-in-peace (r1) | 75.0% | correct | 8.74 |
| 11-token-doublers (r1) | 100.0% | correct | 15.85 |
| 12-replacement-choice (r1) | 100.0% | correct | 13.22 |
| 13-apnap (r1) | 100.0% | correct | 11.83 |
| 14-humility-anthem (r1) | 100.0% | correct | 14.07 |
| 15-own-hexproof (r1) | 100.0% | correct | 6.86 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 12.76 |
| 17-token-blink (r1) | 100.0% | correct | 11.41 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 9.97 |
| 19-legend-response (r1) | 50.0% | correct | 12.26 |
| 20-clarify-interaction (r1) | 100.0% | partial | 10.82 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

**No, you cannot respond to your opponent tapping a basic Forest for mana.**

A basic Forest's tap-for-mana ability is an activated mana ability. Mana abilities do not go on the stack, so they cannot be targeted, countered, or otherwise responded to. They resolve immediately after being activated. [CR 605.3b]

This applies to all basic lands, which have the intrinsic ability "{T}: Add [mana symbol]" (for Forests, {G}). [CR 305.6]

Since the ability never hits the stack, no player ever gets priority in response to it. [CR 605.3b]

Review: **correct**. Correct activated mana ability ruling, immediate resolution, and supporting rules.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

## Ruling

**Yes, you get priority first after casting the instant. No, the instant does not resolve immediately.**

## Explanation

When you cast a spell while you have priority, you are the first player to receive priority again afterward. Your opponent then gets the chance to respond (e.g., counter the spell) before it resolves.

The instant sits on the stack and only resolves once **all players pass in succession**. It does not resolve the moment it is cast.

### Supporting rules

- **You get priority first:** "If a player has priority when they cast a spell, activate an ability, or take a special action, that player receives priority afterward." [CR 117.3c]

- **The spell waits on the stack:** "When all players pass in succession, the top (last-added) spell or ability on the stack resolves." [CR 405.5]

- **Resolution happens after all players pass:** "Each time all players pass in succession, the spell or ability on top of the stack resolves." [CR 608.1]

### Summary of the sequence

1. You have priority and cast the instant (it goes on the stack).
2. You receive priority first and may choose to pass.
3. Your opponent receives priority and may respond (counter, etc.) or pass.
4. Once all players have passed in succession, the instant resolves.

Review: **correct**. Correct caster receives priority again and all players must pass; now cites 117.3c.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

**No, you do not draw a card.**

When Defiant Strike tries to resolve, it checks whether its target is still legal. Since your creature was destroyed and is no longer on the battlefield, it is an illegal target. Because Defiant Strike has only one target and that target is now illegal, the spell doesn't resolve at all — it's removed from the stack and put into your graveyard. Neither the +1/+0 buff nor the card draw happens.

This is confirmed directly by the card's own ruling:

> "If the target creature is an illegal target by the time Defiant Strike tries to resolve, the spell won't resolve. You won't draw a card." [C2]

The general rule supports this: if all targets of a spell are illegal at resolution, the spell doesn't resolve and is put into its owner's graveyard. [CR 608.2b]

Review: **correct**. Correct no draw with sole target illegal and whole spell not resolving.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

**Yes, the remaining creature takes 2 damage.**

When the spell resolves, it checks whether its targets are still legal. Since one target left the battlefield, that target is now illegal. However, because *not all* targets are illegal, the spell still resolves normally. The illegal target simply isn't affected, while the legal target is.

This is directly supported by the rule:

> "If all its targets, for every instance of the word 'target,' are now illegal, the spell or ability doesn't resolve… **Otherwise, the spell or ability will resolve normally. Illegal targets, if any, won't be affected by parts of a resolving spell's effect for which they're illegal. Other parts of the effect for which those targets are not illegal may still affect them.**" [CR 608.2b]

So the spell resolves, the departed creature is skipped, and the remaining creature takes 2 damage.

Review: **correct**. Correct remaining legal target takes damage and partial illegality does not stop resolution.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Yes.** You may assign 2 damage to the indestructible blocker and 4 damage to the defending player.

**Why:** Trample's assignment rule checks for *assigned lethal damage* — meaning damage equal to or greater than the blocker's toughness (accounting for damage already marked on it). It does not check whether the blocker will actually be destroyed.

- The blocker is a 2/2 with no damage on it, so "lethal damage" = 2. [CR 702.19b]
- Once 2 damage is assigned to the blocker, the remaining 4 may be assigned to the defending player. [CR 702.19b]
- Indestructible means the permanent "can't be destroyed" and "isn't destroyed by lethal damage," but it does not alter the trample assignment check. [CR 702.12b]

This is directly analogous to the supplied example: a 6/6 with trample blocked by a 2/2 with protection from green still requires 2 damage assigned to the blocker (even though that damage is prevented), with the remaining 4 free to go to the player. [CR 702.19b]

Indestructible is a "can't be destroyed" protection that applies at the destruction step, not at the damage-assignment step. It has no bearing on how trample damage is divided.

Review: **correct**. Correct 2/4 assignment and indestructibility distinction with both operative definitions.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

## Ruling

**You can assign a maximum of 4 damage to the defending player.**

## Explanation

The interaction between trample and deathtouch works as follows:

1. **Trample** requires you to assign lethal damage to the blocking creature before assigning excess damage to the player. [CR 702.19b]

2. **Deathtouch** changes what counts as "lethal damage" for this purpose: any nonzero amount of combat damage assigned to a creature by a source with deathtouch is considered lethal damage for the purposes of determining if excess damage is being dealt. [CR 702.2c]

So even though the blocker is an 8/8, you only need to assign **1 damage** to it to satisfy the trample requirement (because deathtouch makes that 1 damage "lethal" for trample purposes). The remaining **4 damage** is excess and may be assigned to the defending player.

**Summary:** 1 damage to the 8/8 blocker + 4 damage to the defending player = 5 total (the creature's power).

Review: **correct**. Correct maximum 4 and explicit nonzero deathtouch assignment rule.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

**No, it does not survive.** The creature will be put into its owner's graveyard.

**Explanation:**

Indestructible prevents a permanent from being *destroyed*—it protects against lethal damage and "destroy" effects [CR 702.12b]. However, a creature with toughness 0 or less is put into its owner's graveyard as a state-based action [CR 704.5f]. This is not destruction; it's a separate game action that indestructible does not prevent.

So the 3/3 with indestructible that receives -3/-3 becomes a 0/0, and the next time state-based actions are checked, it goes to the graveyard. Indestructible offers no protection here.

Review: **correct**. Correct 0/0, graveyard, and distinction from destruction; both previously missing definitions are now present.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

## Ruling

**Yes to both.** You may move your commander to the command zone, and "dies" triggers still fire.

### Moving to the command zone

When your commander is put into the graveyard from the battlefield, the owner **may** put it into the command zone. This is a **state-based action**, not a replacement effect:

> "If a commander is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked, its owner may put it into the command zone. This is a state-based action." [CR 9

Review: **partial**. Correct yes-to-both opening and identifies the command-zone move as a state-based action, but the answer is cut off before explaining dies triggers through graveyard entry. Missing second explanation criterion. Context exhausted at 8190 total tokens.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

**Ruling: The additional commander tax is {4}.**

**Explanation:**

Rule 903.8 states that a commander cast from the command zone costs an additional {2} *for each previous time the player casting it has cast it from the command zone that game* [CR 903.8].

The tax is based solely on prior casts **from the command zone**. Your cast from your hand does not count toward the tax. Since you have previously cast your commander from the command zone **twice**, the additional cost is:

> 2 × {2} = **{4}**

So your next cast from the command zone will cost its normal mana cost plus an additional {4}.

Review: **correct**. Correct additional 4 and excludes hand cast. Citation ID now correct.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

**No, Blood Artist does not trigger.**

**Explanation:**

Blood Artist's ability triggers "whenever this creature or another creature **dies**." The term "dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4].

Rest in Peace has a static replacement effect: "If a card or token would be put into a graveyard from anywhere, exile it instead" [C1]. When the creature is destroyed, this replacement effect applies, so the creature is exiled rather than put into a graveyard. Since it is never put into a graveyard from the battlefield

Review: **correct**. Correct no trigger and exile instead of graveyard. Both substantive criteria are met, but response is cut off mid-sentence at 8189 total tokens. This is a delivery failure despite rubric correctness.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

## Ruling

You create **4 tokens**. The doublers do **not** loop forever.

## Explanation

Both Doubling Season and Anointed Procession are replacement effects that modify the same event ("an effect would create one or more tokens under your control"). When multiple replacement effects are applicable, the affected player chooses the order in which they apply, and the process repeats until no more applicable effects remain [CR 616.1] [CR 616.1f].

The sequence works like this:

1. An effect would create **1** token.
2. You choose one doubler to apply first (e.g., Doubling Season). It replaces "create 1" with "create **2**."
3. The process repeats with the modified event. Anointed Procession is still applicable (it's a *different* effect, not the same one re-triggering). It replaces "create 2" with "create **4**."
4. No further replacement effects are applicable. Done.

The reason this terminates is that each replacement effect gets only **one** opportunity to affect an event or any modified events that replace it [CR 614.5]. Once a doubler has been applied, it cannot apply again to its own output.

This is confirmed by the card-specific rulings: two doublers produce 4× the original number, three produce 8×, and so on [C2] [C11]. The multiplication is finite and deterministic, not an infinite

Review: **correct**. Correct four tokens, sequential replacement, and each effect only once. Both substantive criteria are met, but the final sentence is cut off at 8189 total tokens. Delivery regression is recorded separately.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

## Ruling

**You (the affected player) choose the order, and the final damage can be either 7 or 8.**

## Explanation

Since both effects are ordinary replacement effects (neither is a self-replacement effect, and neither modifies control or causes a copy to enter), the choice falls to the affected player under the general rule:

> "the affected object's controller (or its owner if it has no controller) or the affected player chooses one to apply" — [CR 616.1]

> "Any of the applicable replacement and/or prevention effects may be chosen." — [CR 616.1e]

> "Once the chosen effect has been applied, this process is repeated (taking into account only replacement or prevention effects that would now be applicable) until there are no more left to apply." — [CR 616.1f]

Doubling damage is confirmed as a replacement effect: [CR 701.10g].

### Two possible orders

| Order | Step 1 | Step 2 | Final |
|-------|--------|--------|-------|
| Double → +1 | 3 × 2 = 6 | 6 + 1 = **7** | 7 |
| +1 → Double | 3 + 1 = 4 | 4 × 2 = **8** | 8 |

Each effect gets only one opportunity to affect the event, even the modified one [CR 614.5], so there's no risk of the doubling effect re-triggering on its own output.

**Bottom line:** You pick the order, and you can get either 7 or 8.

Review: **correct**. Correct affected-player choice, both arithmetic orders, and once-per-effect restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

## Ruling

**Bob's triggered ability resolves first.**

## Explanation

When multiple triggered abilities are waiting to go on the stack, they are placed in APNAP (Active Player, then Non-Active Player) order. Since Alice is the active player, she puts her triggered ability on the stack first, and then Bob puts his on the stack. [CR 603.3b]

Each object placed on the stack goes on top of everything already there. [CR 405.2] So Bob's ability ends up on top of Alice's.

When all players pass in succession, the topmost object on the stack resolves. [CR 608.1] Since Bob's ability is on top, it resolves first.

This is the standard "non-active player's triggers go on the stack last, so they resolve first" pattern that applies whenever both players have triggered abilities waiting at the same time.

Review: **correct**. Correct APNAP order and last-in-first-out resolution with supporting sources.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

## Ruling

The creature is **2/2**. It does **not** matter which enchantment entered the battlefield first.

## Explanation

The two effects operate in different sublayers of layer 7, so timestamp order is irrelevant:

1. **Layer 7b** – Humility's "have base power and toughness 1/1" is a *setting* effect. It applies here. [CR 613.4b]
2. **Layer 7c** – Glorious Anthem's "get +1/+1" is a *modifying* effect. It applies here, after 7b. [CR 613.4c]

Because sublayers are applied in a fixed order (7a → 7b → 7c → 7d) regardless of timestamps, the setting effect always lands first and the +1/+1 is then added on top. [CR 613.4]

This is consistent with the general principle that "effects that set a creature's power and/or toughness to specific values may refer to base power and/or toughness. Other continuous effects may further modify the creature's power and toughness." [CR 208.4a]

**Result:** 1/1 (Humility) + 1/+1 (Glorious Anthem) = **2/2**.

Review: **correct**. Correct 2/2 and sublayer order regardless of timestamps.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

**Yes, you may target your own hexproof creature with your own Giant Growth.**

Hexproof only restricts *opponents* from targeting the permanent. The rule states:

> "Hexproof" on a permanent means "This permanent can't be the target of spells or abilities **your opponents** control." [CR 702.11b]

Since you are the controller of both the hexproof creature and the Giant Growth, the hexproof ability does not apply to you. You can freely target your own creature with your own spells, including Giant Growth.

Review: **correct**. Correct own-creature targeting and opponents-only hexproof restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**No.** Your attacker deals 0 damage in the second combat damage step.

**Explanation:**

In the first combat damage step, your 3/3 with double strike assigns 3 damage to the 2/2 blocker, which dies. In the second combat damage step, your creature still has double strike and therefore still assigns combat damage. However, it is still a *blocked* creature (blocking status persists even after the blocker dies), and a blocked creature can only assign damage to the creatures blocking it. Since no creatures are currently blocking it, it assigns no combat damage at all.

Trample is the ability that would allow a blocked attacker to assign excess damage to the player after lethal damage is assigned to blockers. Without trample, a blocked creature simply has no legal target for its damage once its blockers are gone.

**Citations:**

- [CR 510.1c] — "A blocked creature assigns its combat damage to the creatures blocking it. If no creatures are currently blocking it (if, for example, they were destroyed or removed from combat), it assigns no combat damage."
- [CR 702.19b] — Trample is what permits assigning excess damage to the player after lethal damage is assigned to blockers. Your attacker lacks this ability.

Review: **correct**. Correct no second-step player damage and explicit continued blocked status without trample.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**No, the token does not return to the battlefield.**

Once a token leaves the battlefield, it is permanently barred from returning. Rule 111.8 states:

> "A token that has left the battlefield can't move to another zone or come back onto the battlefield. If such a token would change zones, it remains in its current zone instead." [CR 111.8]

This is a "can't" restriction that applies immediately—the token doesn't need to wait for state-based actions to be checked before it becomes unreturnable. The "return to the battlefield" instruction simply fails; the token remains in exile.

(For completeness, the token will then cease to exist the next time state-based actions are checked, per [CR 111.7], but that's a separate cleanup step. The key point is that the return instruction is already blocked by rule 111.8.)

Review: **correct**. Correct no second zone change, followed by cessation at the next state-based check. Calls this a separate cleanup step colloquially, but explicitly states the correct timing rather than the cleanup phase.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

**Yes, you can activate it this turn.**

Summoning sickness only restricts two things:

1. Activated abilities whose activation cost includes the **tap symbol ({T})** or the **untap symbol ({Q})**. [CR 302.6] [CR 602.5a]
2. Attacking. [CR 302.6]

Your ability's cost is "Sacrifice this creature," which contains neither {T} nor {Q}. It is therefore **not** subject to the summoning sickness restriction. As long as you have priority, you may activate it. [CR 117.1b]

**In short:** Summoning sickness is specifically about tap/untap costs and attacking. A sacrifice cost (or any other cost like paying mana, discarding a card, etc.) is unaffected, so you can activate the ability the same turn the creature entered the battlefield.

Review: **correct**. Correct sacrifice activation and tap/untap-symbol distinction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

**No.** You cannot respond to the legend rule with an instant (or any other action). The legend rule is a state-based action, and state-based actions are handled automatically by the game before any player receives priority.

**How the sequence works:**

1. The spell resolves.
2. The active player *would* receive priority [CR 117.3b].
3. But before priority is actually given, the game checks for and performs all applicable state-based actions [CR 117.5].
4. The legend rule applies: the player who controls the duplicate legendary permanents chooses one to keep, and the rest are put into their owners' graveyards [CR 704.5j].
5. Only after state-based actions are resolved and any triggered abilities are put on the stack does a player actually receive priority [CR 117.5].

State-based actions happen automatically and do not use the stack [CR 117.2d]. No player gets a chance to cast a spell or activate an ability in response to them. The choice of which legendary permanent to keep is made as part of the state-based action itself, with no opportunity for interaction.

Review: **correct**. Correct no response window, explicit state-based checks before priority, and choice of one legendary permanent. Uses alternative timing evidence 117.5 rather than canonical reference 704.3.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

## Ruling

**Not necessarily.** Protection only shields your creature from specific things tied to the stated quality. Whether your creature is safe depends on two key details:

1. **What is your creature protected from?** (a color, a card type, a specific player, etc.)
2. **What is the removal spell?** (Does it target? Does it have the stated quality?)

## What Protection Actually Does

Protection from [quality] provides these specific protections:

- **Can't be targeted** by spells or abilities that have the stated quality. [CR 702.16b]
- **Can't be enchanted** by Auras with the stated quality. [CR 702.16c]
- **Can't be equipped** by Equipment with the stated quality. [CR 702.16d]
- **Damage is prevented** from sources with the stated quality. [CR 702.16e]
- **Can't be blocked** by creatures with the stated quality. [CR 702.16f]

## What Protection Does NOT Do

- It does **not** make the creature immune to all removal. A spell that doesn't have the stated quality can still target and destroy it.
- It does **not** protect against non-targeted effects (e.g., "destroy all creatures" or "destroy all creatures with power 4 or greater").
- It does **not** prevent the creature from being destroyed by effects that don't target it.

## What I Need From You

To give you a definitive answer, please tell me:

- The exact protection your creature has (e.g., "protection from red," "protection from black," "protection from [specific player]")
- The name of the removal spell your opponent cast

You can attach the card using `[[Exact Card Name]]` or describe its text.

Review: **partial**. Asks both required clarifications and correctly handles non-targeted destruction, but states protection does not protect against non-targeted effects in general. That blanket claim incorrectly encompasses damage effects, which protection may prevent. Its preceding damage-prevention bullet does not remove the contradiction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

