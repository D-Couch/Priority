# medium-reasoning

Status: **complete** · implementation commit `9a9dafd5e7dfad2f442f0d2a6d893e86373bb95e`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 16/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 93.8% |
| Cases retrieving every expected evidence group | 17/20 |
| Answers with citations | 20/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Reviewed fully correct | 16/20 reviewed |
| Reviewed accuracy | 80.0% |
| Mean reviewed rubric score | 95.0% |
| Median successful response | 12.12 s |
| p95 successful response | 19.39 s |
| Median first visible answer token | 10.26 s |

These are development scenarios, not a held-out accuracy claim. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.90 |
| 02-hold-priority (r1) | 100.0% | correct | 11.85 |
| 03-illegal-target (r1) | 100.0% | correct | 10.29 |
| 04-partial-targets (r1) | 100.0% | correct | 12.66 |
| 05-trample-indestructible (r1) | 100.0% | correct | 12.68 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 10.96 |
| 07-zero-toughness (r1) | 100.0% | correct | 13.02 |
| 08-commander-dies (r1) | 100.0% | partial | 20.63 |
| 09-commander-tax (r1) | 100.0% | correct | 7.75 |
| 10-rest-in-peace (r1) | 75.0% | correct | 12.11 |
| 11-token-doublers (r1) | 100.0% | correct | 16.27 |
| 12-replacement-choice (r1) | 100.0% | correct | 14.16 |
| 13-apnap (r1) | 100.0% | correct | 11.92 |
| 14-humility-anthem (r1) | 100.0% | correct | 14.19 |
| 15-own-hexproof (r1) | 100.0% | correct | 8.37 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 15.36 |
| 17-token-blink (r1) | 50.0% | incorrect | 19.39 |
| 18-summoning-sacrifice (r1) | 100.0% | partial | 9.81 |
| 19-legend-response (r1) | 50.0% | correct | 12.13 |
| 20-clarify-interaction (r1) | 100.0% | partial | 11.92 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

**No.** You cannot respond to your opponent tapping a basic Forest for mana.

A basic Forest has the intrinsic ability "{T}: Add {G}" [CR 305.6]. That ability meets every criterion for an activated mana ability: it doesn't require a target, it adds mana to a player's mana pool, it isn't a loyalty ability, and it doesn't move cards to or from a library [CR 605.1a].

Because it is a mana ability, it doesn't go on the stack. It resolves immediately after it is activated, so it can't be targeted, countered, or otherwise responded to [CR 605.3b]. There is no window in which either player receives priority to cast an instant or activate an ability in response.

Review: **correct**. Correct activated mana ability ruling, immediate resolution, and supporting rules.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

**Ruling:** Yes, you receive priority back first, but no—the instant does not resolve immediately. It goes on the stack, and your opponent gets a chance to respond before it resolves.

**Explanation:**

When you cast the instant while you have priority, you are the one who receives priority again afterward [CR 117.3c]. You then pass (or take another action), and the next player in turn order—your opponent—receives priority [CR 117.3d]. Your opponent may cast instants, activate abilities, or pass. The instant only resolves once **all** players pass in succession [CR 405.5] [CR 608.1].

So the sequence is:

1. You cast the instant; it is put on the stack [CR 405.1].
2. You get priority back [CR 117.3c].
3. You pass; your opponent gets priority [CR 117.3d].
4. Your opponent may respond or pass.
5. When every player has passed in succession, the instant resolves [CR 405.5] [CR 608.1].

The instant is not a "free" action that bypasses your opponent's turn to act; it uses the stack just like any other spell [CR 304.1].

Review: **correct**. Correct priority returned to caster and all players passing. Both canonical references now fit; same mean recall conceals changing coverage between cases.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

**No, you do not draw a card.**

Defiant Strike has a single target: the creature. If that creature is destroyed before Defiant Strike resolves, it is no longer on the battlefield and is therefore an illegal target [CR 608.2b]. Because *all* of the spell's targets are now illegal, the spell doesn't resolve at all—it is removed from the stack and put into its owner's graveyard [CR 608.2b]. Neither the +1/+0 buff nor the "Draw a card" instruction occurs.

This works the same way as the Sorin's Thirst example in the rules: if the target creature is no longer legal, the entire spell fails to resolve and its controller gains no life [CR 608.2b].

Review: **correct**. Correct no draw with sole target illegal and whole spell not resolving.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

**Yes, the remaining creature takes 2 damage.**

The spell still resolves because not *all* of its targets are illegal. Under [CR 608.2b], a spell or ability fails to resolve only if "all its targets, for every instance of the word 'target,' are now illegal." Here the text "Deal 2 damage to each of up to two target creatures" contains a single instance of the word "target" (per [CR 115.3], one instance of "target" can be applied to multiple objects). You chose two targets for that one instance; one is now illegal (left the battlefield) and one is still legal, so the spell does not fizzle.

Once it resolves, [CR 608.2b] continues: "Illegal targets, if any, won't be affected by parts of a resolving spell's effect for which they're illegal. Other parts of the effect for which those targets are not illegal may still affect them." The departed creature simply isn't dealt damage, but the creature still on the battlefield is a legal target and takes the full 2 damage.

Review: **correct**. Correct remaining legal target takes damage and partial illegality does not stop resolution.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Yes.** You may assign 2 damage to the indestructible blocker and 4 damage to the defending player.

**Explanation:** Trample's damage-assignment rule requires that *lethal damage* be assigned to each blocking creature before excess damage may be directed at the player. Lethal damage is simply damage equal to the creature's toughness (here, 2). [CR 702.19b]

Indestructible prevents the permanent from being *destroyed* by that damage and makes it ignore the state-based action that would destroy it. [CR 702.12b] It does not alter what counts as "lethal damage" for the purposes of the trample assignment check. The trample rule asks whether lethal damage has been *assigned*, not whether the creature will actually be destroyed.

So once 2 damage is assigned to the 2/2 blocker, the remaining 4 damage is excess and may be assigned to the defending player. [CR 702.19b]

Review: **correct**. Correct 2/4 assignment and indestructibility distinction with both operative definitions.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

**Ruling: You can assign a maximum of 4 damage to the defending player.**

**Explanation:**

Your 5/5 assigns 5 combat damage total [CR 510.1a]. Because it has trample, you must first assign at least lethal damage to the blocking creature before any excess can go to the defending player [CR 702.19b]. However, because your attacker also has deathtouch, *any nonzero amount* of damage assigned to the blocker counts as lethal damage for this purpose [CR 702.2c]. So the minimum you must assign to the 8/8 is just **1** damage.

That leaves 5 − 1 = **4** damage you may assign to the defending player.

**Citations:** [CR 510.1a], [CR 702.19b], [CR 702.2c]

Review: **correct**. Correct maximum 4 and explicit nonzero deathtouch assignment rule.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

**No, it does not survive.** The creature will be put into its owner's graveyard by the state-based action for having toughness 0 or less.

**Explanation:**

Indestructible prevents a permanent from being *destroyed*—that is, from being destroyed by lethal damage or by a "destroy" effect. Specifically, [CR 702.12b] states that an indestructible permanent "isn't destroyed by lethal damage, and they ignore the state-based action that checks for lethal damage (see rule 704.5g)."

However, the -3/-3 makes the creature a 0/0, and the applicable state-based action is [CR 704.5f]: "If a creature has toughness 0 or less, it's put into its owner's graveyard. Regeneration can't replace this event." This is not a destruction event; it is a separate state-based action that moves the permanent to the graveyard. Indestructible does not prevent this.

So the 0/0 indestructible creature is put into its owner's graveyard the next time state-based actions are checked.

Review: **correct**. Correct 0/0 goes to graveyard; explicitly distinguishes lethal-damage destruction from zero-toughness action.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

**Ruling: Yes to both.** You may put the commander into the command zone, and "dies" triggers still fire.

**Moving to the command zone.** When a commander is in the graveyard and was put there since the last time state-based actions were checked, its owner *may* put it into the command zone. This is a state-based action, not a replacement effect, so it works even when no replacement effects are present. [CR 903.9a]

**"Dies" triggers.** "Dies" means "is put into a graveyard from the battlefield." [CR 700.4] The trigger event occurs the moment the commander is put into the graveyard; the triggered ability goes on the stack at that point. [CR 603.2] The subsequent move to the command zone happens later, during the next state-based-action check. [CR 704.1]

Because "dies" triggers are a form of leaves-the-battlefield trigger, they "look back in time" rather than searching for the object in the zone it ended up in. [CR 603.10a] So even though the commander is in the command zone by the time the triggered ability resolves, the ability still resolves normally, referencing the commander as it was on the battlefield.

**Sequence in brief:**
1. Commander is destroyed → put into the graveyard from the battlefield (the event).
2. "Dies" triggers fire and go on the stack. [CR 603.2]
3. State-based actions are checked; you may put the commander into the command zone. [CR 903.9a]
4. The triggered ability resolves, looking back at the battlefield. [CR 603.10a]

Review: **partial**. Both requested conclusions are correct, but the sequence incorrectly puts triggered abilities on the stack before checking state-based actions. Triggering happens immediately; putting triggers on the stack waits until after state-based actions (117.5, 603.3). It also treats look-back determination of triggering as something performed on resolution. These false extra claims prevent full correctness.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

**Ruling:** The additional commander tax is **{4}**.

**Explanation:** Commander tax is calculated based solely on the number of times you have previously cast that commander *from the command zone* during the game. Casting it from your hand does not increase the count. You have cast it from the command zone twice, so the next cast from the command zone costs an additional 2 × {2} = {4}.

[CR 903.8] states: "A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game."

Review: **correct**. Correct additional 4 and excludes hand cast. Citation ID now correct.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

**No, Blood Artist does not trigger.**

Blood Artist's ability triggers "whenever this creature or another creature **dies**." The term *dies* is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace's replacement effect reads, "If a card or token would be put into a graveyard from anywhere, exile it instead" [C1]. When the creature is destroyed, Rest in Peace replaces the zone change: the creature is exiled rather than put into a graveyard. Because it is never actually put into a graveyard, it never "dies," and Blood Artist's trigger condition is never met.

Review: **correct**. Correct no Blood Artist trigger, exile replaces graveyard entry, and no dies event. Now finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

**Ruling: You create 4 tokens. The doublers do not loop forever.**

**Explanation:**

Both Doubling Season [C1] and Anointed Procession [C7] are replacement effects that modify the same event ("an effect would create one or more tokens under your control"). Because two replacement effects are competing, you choose the order in which they apply [CR 616.1e]. After the first is applied, the process repeats with the remaining applicable effect [CR 616.1f].

So the sequence is:

1. You choose one doubler (e.g., Doubling Season). It applies: 1 token → 2 tokens.
2. The process repeats. Anointed Procession is still applicable and hasn't been used. It applies to the modified event: 2 tokens → 4 tokens.
3. Both replacement effects have now been used. No further applicable replacement effects remain, so the process stops [CR 616.1f].

They do **not** loop infinitely. Each replacement effect gets only one opportunity to affect an event or any modified events that replace it [CR 614.5]. The rules explicitly illustrate this with two identical doubling effects: "A creature that normally deals 2 damage will deal 8 damage—not just 4, and not an infinite amount" [CR 614.5]. Your situation is the same structure: two doublers, each applied once, giving 1 × 2 × 2 = **4 tokens**.

Review: **correct**. Correct four tokens and each replacement applies once to the event. Now finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

**Ruling:** You (the affected player) choose the order, and the final damage can be either **7** or **8**.

**Explanation:**

Because both effects are ordinary (non-self-replacement) replacement effects modifying the same damage event, the affected player chooses which applies first [CR 616.1]. Since neither is a self-replacement effect [CR 616.1a], nor does it modify control, copying, or face-up entry [CR 616.1b–d], the choice falls to the general rule: "Any of the applicable replacement and/or prevention effects may be chosen" [CR 616.1e]. After the first is applied, the process repeats with the remaining effect [CR 616.1f], and the second effect applies to the already-modified event [CR 616.2].

- **Double first, then +1:** 3 → 6 → **7**
- **+1 first, then double:** 3 → 4 → **8**

Doubling is explicitly a replacement effect [CR 701.10g], and each effect gets exactly one opportunity to modify the event [CR 614.5], so no further stacking occurs.

Review: **correct**. Correct affected-player choice, both arithmetic orders, and once-per-effect restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

**Ruling:** Bob's triggered ability resolves first.

**Explanation:** When multiple triggered abilities are waiting to go on the stack, they are placed in APNAP (active-player, non-active-player) order. Because it is Alice's turn, Alice is the active player and acts first in that ordering. She puts her triggered ability on the stack, then Bob puts his on the stack [CR 603.3b]. Each object placed on the stack goes on top of everything already there [CR 405.2], so Bob's ability ends up above Alice's. When all players pass in succession, the topmost object on the stack resolves [CR 608.1], which is Bob's ability.

Review: **correct**. Correct APNAP order and last-in-first-out resolution with supporting sources.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

**Ruling: The creature is 2/2, and it does not matter which enchantment entered first.**

**Explanation:**

The two effects land in different sublayers of layer 7, so the layer system—not timestamp order—determines the result.

1. **Layer 7b** – Humility's "have base power and toughness 1/1" is an effect that *sets* power and toughness to a specific value, so it applies in layer 7b [CR 613.4b]. The creature's P/T is now 1/1.

2. **Layer 7c** – Glorious Anthem's "get +1/+1" is an effect that *modifies* power and toughness without setting it to a specific number, so it applies in layer 7c [CR 613.4c]. The +1/+1 is added on top of the 1/1, giving **2/2**.

Because the two effects occupy different sublayers (7b before 7c), the order in which the enchantments entered the battlefield is irrelevant [CR 613.4]. Timestamp order only matters *within* a single sublayer [CR 613.7], and here the effects never compete in the same sublayer.

(Humility's "lose all abilities" portion applies in layer 6 [CR 613.1f], but it has no bearing on the P/T calculation.)

Review: **correct**. Correct 2/2 and sublayer order regardless of timestamps.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

**Yes, you may target your own hexproof creature with your own Giant Growth.**

Hexproof on a permanent means "This permanent can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. The restriction is limited to opponents' spells and abilities. Since you control both the creature and the Giant Growth you're casting, hexproof does not block the targeting. Giant Growth simply reads "Target creature gets +3/+3 until end of turn" [C1], and nothing in its text or in the hexproof rule prevents the controller from choosing their own creature as the target.

As long as you have priority [CR 117.1a] and can pay the cost, you may cast Giant Growth and choose your hexproof creature as the target.

Review: **correct**. Correct own-creature targeting and opponents-only hexproof restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**No.** Your 3/3 deals no combat damage in the second combat damage step.

**Explanation:**

In the first combat damage step, your 3/3 with double strike assigns 3 damage to the 2/2 blocker, which is lethal. The blocker dies.

In the second combat damage step, your creature still assigns damage because it has double strike [CR 702.4b]. However, it is still a *blocked* creature (the blocking relationship was established during declare blockers). Rule 510.1c states:

> "A blocked creature assigns its combat damage to the creatures blocking it. **If no creatures are currently blocking it (if, for example, they were destroyed or removed from combat), it assigns no combat damage.**" [CR 510.1c]

Since the only blocker is gone, your attacker assigns **zero** damage in the second combat damage step. It does not redirect its damage to the player.

This is precisely the gap that trample fills: rule 702.19d explicitly allows a trample attacker whose blockers are all gone to assign damage to the defending player "as though all blocking creatures have been assigned lethal damage" [CR 702.19d]. Without trample, no such redirect exists, and 510.1c governs the result.

Review: **correct**. Correct no second-step player damage and explicit continued blocked status without trample.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**Yes, the token returns to the battlefield.**

Because the exile and the return are both part of the same resolution, the token is still in the exile zone (and still exists) when the "return" step is applied. The rule that makes a token cease to exist when it is in a zone other than the battlefield is explicitly a **state-based action** [CR 111.7]. State-based actions are checked only at specific times (e.g., when a player would receive priority, at the start of a step or phase), not between individual steps of a single spell or ability's resolution. So the game does not check whether the token should cease to exist between the exile and the return; the token is simply found in the exile zone and put back onto the battlefield as the effect instructs.

If, instead, the exile were one effect and the return were a *separate* effect (for example, a triggered ability that fires after the exile resolves), state-based actions would be checked in between, the token would cease to exist, and the return effect would have no valid object to act on. But in the single-resolution scenario you described, the token returns.

Review: **incorrect**. Incorrect return during resolution; still missing 111.8. Also overgeneralizes state-based checks to the start of every step/phase. More reasoning does not repair missing evidence.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 111.8

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

**Yes.** You can activate that ability on the same turn you cast the creature, as soon as you have priority after the spell resolves.

Summoning sickness restricts only two things: activating a creature's activated ability that includes the tap symbol ({T}) or the untap symbol ({Q}) in its activation cost, and attacking with that creature [CR 302.6]. Your ability's cost is "Sacrifice this creature," which contains neither symbol, so the restriction does not apply.

Once the creature spell resolves and the creature enters the battlefield, you (the active player) receive priority [CR 117.3b], and you may activate an activated ability any time you have priority [CR 117.1b]. You can therefore pay the sacrifice cost and draw a card immediately.

Review: **partial**. Correct activation permission and tap/untap distinction, but assumes the user is the active player without establishing that, and says the sacrifice activation draws immediately. This ordinary activated ability uses the stack and may be responded to. Extra timing claims prevent full correctness.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

**No.** You must choose which legendary permanent to keep as part of the state-based action; you do not get a window to cast an instant in response.

The legend rule is a state-based action: "If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners' graveyards" [CR 704.5j]. State-based actions "happen automatically when certain conditions are met" and "are dealt with before a player would receive priority" [CR 117.2d].

After the spell that created the duplicate resolves, the game checks state-based actions *before* the active player receives priority [CR 117.3b]. Because no one has priority at the moment the legend rule is applied, there is no opportunity to cast an instant or activate an ability in response. You make your choice, the other permanent(s) go to the graveyard, and only then does the active player get priority.

Review: **correct**. Correct no response window, explicit state-based checks before priority, and choice of one legendary permanent. Uses alternative timing evidence 117.5 rather than canonical reference 704.3.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

**It depends on two details you haven't provided.**

Protection from a quality (e.g., "protection from red") prevents a creature from being **targeted** by spells that have that quality [CR 702.16b]. It also prevents damage from sources with that quality [CR 702.16e]. However, protection does **not** make a creature immune to non-targeted effects (e.g., "destroy all creatures"), and it does **not** protect against spells of a different color or quality.

So the answer hinges on:

1. **What quality does your creature have protection from?** (red, blue, a specific card name, a player, etc.)
2. **What is the removal spell?** Specifically, what color is it, and does it say "target" in its text?

If the spell's color (or other quality) matches your creature's protection **and** the spell targets your creature, your creature is safe from being targeted [CR 702.16b]. If the spell is a different color, or if it's a non-targeted "board wipe" style effect, protection does not save it.

Could you tell me the exact protection text on your creature and the name (or text) of the removal spell your opponent cast?

Review: **partial**. Asks both clarifications, but still claims a non-targeted board-wipe-style effect cannot be stopped by protection. Non-targeted preventable damage of the protected quality is a counterexample. The prompt’s ask-and-stop instruction was not followed.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

