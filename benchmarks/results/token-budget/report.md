# token-budget

Status: **complete** · implementation commit `6cf5cc3f7153454a9d60510df64e49bc09bb6438`

Suite `gameplay-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 18/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 93.8% |
| Cases retrieving every expected evidence group | 17/20 |
| Answers with citations | 20/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Reviewed fully correct | 18/20 reviewed |
| Reviewed accuracy | 90.0% |
| Mean reviewed rubric score | 100.0% |
| Median successful response | 10.83 s |
| p95 successful response | 14.31 s |
| Median first visible answer token | 8.21 s |

These are development scenarios, not a held-out accuracy claim. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| 01-mana (r1) | 100.0% | correct | 7.85 |
| 02-hold-priority (r1) | 50.0% | correct | 10.29 |
| 03-illegal-target (r1) | 100.0% | correct | 10.26 |
| 04-partial-targets (r1) | 100.0% | correct | 14.07 |
| 05-trample-indestructible (r1) | 100.0% | correct | 14.06 |
| 06-deathtouch-trample (r1) | 100.0% | correct | 10.02 |
| 07-zero-toughness (r1) | 100.0% | correct | 14.31 |
| 08-commander-dies (r1) | 100.0% | partial | 12.52 |
| 09-commander-tax (r1) | 100.0% | correct | 8.43 |
| 10-rest-in-peace (r1) | 75.0% | correct | 8.79 |
| 11-token-doublers (r1) | 100.0% | correct | 14.40 |
| 12-replacement-choice (r1) | 100.0% | correct | 10.82 |
| 13-apnap (r1) | 100.0% | correct | 12.41 |
| 14-humility-anthem (r1) | 100.0% | correct | 11.25 |
| 15-own-hexproof (r1) | 100.0% | correct | 6.92 |
| 16-first-strike-blocker (r1) | 100.0% | correct | 12.90 |
| 17-token-blink (r1) | 100.0% | correct | 9.60 |
| 18-summoning-sacrifice (r1) | 100.0% | correct | 10.41 |
| 19-legend-response (r1) | 50.0% | correct | 12.48 |
| 20-clarify-interaction (r1) | 100.0% | partial | 10.84 |

## Answers and review notes

### 01-mana / repetition 1

Can I respond to my opponent tapping a basic Forest for mana?

**No, you cannot respond to your opponent tapping a basic Forest for mana.**

Basic lands have the intrinsic ability "{T}: Add {G}" (for Forests) [CR 305.6]. This is an activated mana ability, meeting all the criteria in rule 605.1a: it doesn't require a target, it adds mana to a player's mana pool, it's not a loyalty ability, and it doesn't move cards to or from a library [CR 605.1a].

The key rule here is that **an activated mana ability doesn't go on the stack**, so it can't be targeted, countered, or otherwise responded to. It resolves immediately after it is activated [CR 605.3b].

This means there is no window in which you could cast an instant, activate a response, or otherwise interact with the tap-for-mana action. It simply happens and is over.

Review: **correct**. Correct activated mana ability ruling, immediate resolution, and supporting rules.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 02-hold-priority / repetition 1

I have priority and cast an instant. Do I get priority again before my opponent, and does the instant resolve immediately?

## Ruling

**Yes, you get priority again after casting. No, the instant does not resolve immediately.**

### Explanation

When you cast a spell while you have priority, you receive priority again afterward (before your opponent does). This means you could, for example, cast another instant or activate an ability in response to your own first instant.

However, the instant does **not** resolve immediately. It is placed on the stack, and it only resolves once all players pass in succession. Your opponent will get the chance to respond before it resolves.

### Supporting Citations

- **[CR 117.3c]** — "If a player has priority when they cast a spell, activate an ability, or take a special action, that player receives priority afterward."
- **[CR 608.1]** — "Each time all players pass in succession, the spell or ability on top of the stack resolves."
- **[CR 405.6c]** — "Mana abilities resolve immediately." (This is the exception — only mana abilities resolve immediately, not instants.)

### Summary of the sequence

1. You have priority and cast the instant → it goes on the stack.
2. You receive priority again (117.3c).
3. You may act or pass.
4. Your opponent receives priority and may respond.
5. Once all players pass in succession, the instant resolves (608.1).

Review: **correct**. Correct caster priority and all-player passing. Canonical 117.4 was omitted by packing, but 608.1 directly supplies the passing condition.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 117.4

### 03-illegal-target / repetition 1

I cast Defiant Strike targeting my creature. My opponent destroys that creature in response. Do I still draw a card when Defiant Strike would resolve?

**No, you do not draw a card.**

Defiant Strike has a single target (the creature). When it resolves, the game checks whether that target is still legal. Since the creature was destroyed and is no longer on the battlefield, it is no longer in the zone it was in when targeted, making it an illegal target. [CR 608.2b]

Because **all** of Defiant Strike's targets are now illegal, the spell doesn't resolve at all — it's removed from the stack and put into its owner's graveyard. Neither the +1/+0 buff nor the "draw a card" effect happens. [CR 608.2b]

This is the same principle as the Sorin's Thirst example in the rules: if the target is illegal at resolution, the entire spell fails to resolve, including any non-targeted portions like "you gain 2 life." [CR 608.2b]

Review: **correct**. Correct no draw with sole target illegal and whole spell not resolving.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 04-partial-targets / repetition 1

An instant says "Deal 2 damage to each of up to two target creatures." I choose two targets. Before it resolves, one target leaves the battlefield; the other remains legal. Does the remaining creature take 2 damage?

**Yes, the remaining creature takes 2 damage.**

The spell "Deal 2 damage to each of up to two target creatures" contains a single instance of the word "target." You chose two different creatures for that one instance. When one of them leaves the battlefield, it becomes an illegal target, but the other remains legal.

Under [CR 608.2b], the spell fails to resolve only if **all** its targets, for **every** instance of the word "target," are now illegal. Since one target is still legal, the spell resolves normally. The rule then states:

> "Illegal targets, if any, won't be affected by parts of a resolving spell's effect for which they're illegal. Other parts of the effect for which those targets are not illegal may still affect them."

So the spell resolves, the creature that left the battlefield is simply not affected, and the remaining legal creature takes 2 damage.

This is analogous to the Plague Spores example in [CR 608.2b], where a spell with two target instances still resolves (and affects the legal target) even when one target becomes illegal.

Review: **correct**. Correct remaining legal target takes damage and partial illegality does not stop resolution.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 05-trample-indestructible / repetition 1

My attacking 6/6 with trample is blocked only by an undamaged 2/2 with indestructible. No other effects apply. May I assign 2 to the blocker and 4 to the defending player?

**Yes.** You may assign 2 damage to the indestructible blocker and 4 damage to the defending player.

**Why:** Trample's assignment rule requires you to assign at least *lethal damage* to the blocker before assigning excess to the player. Lethal damage for an undamaged 2/2 is 2 (equal to its toughness). Indestructible prevents the *result* of that damage (destruction) but does not change what counts as "lethal damage" for assignment purposes.

[CR 702.19b] states: "Once all those blocking creatures are assigned lethal damage, any excess damage is assigned as its controller chooses among those blocking creatures and the player, planeswalker, or battle the creature is attacking."

[CR 702.12b] clarifies that indestructible means the permanent "isn't destroyed by lethal damage" — it addresses the outcome, not the assignment threshold.

The supplied example in [CR 702.19b] is directly analogous: a 6/6 with trample blocked by a 2/2 with protection from green must still assign at least 2 to the blocker (even though that damage will be prevented), and the remaining 4 may go to the defending player. Indestructible functions the same way here — the damage is assigned normally; the creature simply survives it.

Review: **correct**. Correct 2/4 assignment and indestructibility distinction with both operative definitions.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 06-deathtouch-trample / repetition 1

My attacking 5/5 has deathtouch and trample. It is blocked only by an undamaged 8/8 with no abilities. No other effects apply. What is the maximum damage I can assign to the defending player?

## Ruling

**You can assign a maximum of 4 damage to the defending player.**

## Explanation

Trample requires you to assign **lethal damage** to the blocking creature before any excess can go to the player [CR 702.19b]. Normally, an 8/8 would need 8 damage assigned to satisfy that requirement.

However, deathtouch changes what counts as "lethal damage" for this purpose:

> "Any nonzero amount of combat damage assigned to a creature by a source with deathtouch is considered to be lethal damage for the purposes of determining if excess damage is being dealt." [CR 702.2c]

So you must assign at least **1** damage to the 8/8 blocker, and the remaining **4** damage may be assigned to the defending player.

**Summary:** 1 to the blocker + 4 to the player = 5 total (the creature's power).

Review: **correct**. Correct maximum 4 and explicit nonzero deathtouch assignment rule.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 07-zero-toughness / repetition 1

An indestructible 3/3 gets -3/-3 until end of turn. No other effects apply. Does it survive because it is indestructible?

**No — the indestructible creature does not survive.** It will be put into its owner's graveyard.

**Explanation:**

Indestructible prevents a permanent from being *destroyed* — that is, it protects against damage-based destruction and effects that use the verb "destroy." [CR 702.12b]

However, the state-based action that handles a creature with toughness 0 or less is not a destruction event. Rule 704.5f states: "If a creature has toughness 0 or less, it's put into its owner's graveyard." [CR 704.5f]

This is a state-based action that moves the creature to the graveyard; it does not "destroy" it. Since indestructible only prevents destruction, it offers no protection here. The 3/3 becomes a 0/0, and the next time state-based actions are checked, it is put into its owner's graveyard.

**Key distinction:** Indestructible ≠ "can't be put into the graveyard." It specifically blocks the *destroy* verb and lethal damage, not all paths to the graveyard.

Review: **correct**. Correct 0/0, graveyard, and distinction from destruction; both previously missing definitions are now present.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 08-commander-dies / repetition 1

My commander is destroyed and goes from the battlefield to the graveyard. No replacement effects apply. Can I move it to the command zone, and do abilities that trigger when it dies still trigger?

## Ruling

**Yes to both.** You may move your commander to the command zone, and "dies" triggers still fire.

## Explanation

**Moving to the command zone:**

When your commander is destroyed and put into the graveyard, its owner *may* put it into the command zone. This is a state-based action that occurs after the commander is already in the graveyard — it is not a replacement effect. [CR 903.9a]

**"Dies" triggers still fire:**

The term "dies" means "is put into a graveyard from the battlefield." [CR 700.4] Leaves-the-battlefield abilities trigger when a permanent moves from the battlefield to another zone. [CR 603.6c] The trigger event (being put into the graveyard from the battlefield) has already occurred before the state-based action to move the commander to the command zone is checked. So the trigger fires normally. [CR 603.10a]

**One caveat at resolution:**

If a triggered ability attempts to do something *to* the commander (e.g., "return it to its owner's hand" or "exile it"), and the commander has already been moved to the command zone before that ability resolves, the ability will fail to find it in the zone it went to and that portion will do nothing. [CR 603.6] The trigger still fires and resolves, but the part targeting the commander's card will fizzle.

Review: **partial**. Both requested conclusions and explanations are correct and complete. However, the unsolicited caveat says a triggered ability still resolves while the part targeting the moved commander fizzles. This is too broad: an ability with all targets illegal does not resolve (608.2b); some triggers cannot be put on the stack if required targets cannot be chosen (603.3d). The extra universal resolution assurance prevents full correctness.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 09-commander-tax / repetition 1

I have cast my commander twice from the command zone and once from my hand this game. It is now in the command zone again. With no cost modifiers, how much additional commander tax applies to my next cast from there?

**Ruling:** The additional commander tax is **{4}**.

**Explanation:** Commander tax is calculated based solely on the number of times you have previously cast that commander *from the command zone* during the game. Casting it from your hand does not count toward the tax.

You have previously cast it from the command zone **2 times**, so the additional cost is 2 × {2} = **{4}**.

**Supporting citation:**

> "A commander cast from the command zone costs an additional {2} for each previous time the player casting it has cast it from the command zone that game." [CR 903.8]

The rule explicitly limits the count to casts *from the command zone*, so your cast from hand is irrelevant to the calculation.

Review: **correct**. Correct additional 4 and excludes hand cast. Citation ID now correct.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 10-rest-in-peace / repetition 1

Rest in Peace and my Blood Artist are on the battlefield. Another creature would be destroyed. With no other relevant effects, does Blood Artist trigger for that creature?

**No, Blood Artist does not trigger.**

**Explanation:**

Blood Artist's ability triggers "whenever this creature or another creature **dies**." The term "dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4].

Rest in Peace has a replacement effect: "If a card or token would be put into a graveyard from anywhere, exile it instead" [C1]. When the creature is destroyed, it would be put into a graveyard from the battlefield, but Rest in Peace replaces that zone change with exile. Since the creature is exiled rather than put into a graveyard, it never satisfies the definition of "dies," and Blood Artist's trigger condition is never met [C5].

Review: **correct**. Correct no Blood Artist trigger, exile replaces graveyard entry, and no dies event. Now finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 614.6

### 11-token-doublers / repetition 1

I control Doubling Season and Anointed Procession. An effect would create one creature token under my control. No other effects apply. How many tokens do I create, and do the doublers loop forever?

## Ruling

You create **4 tokens**. The doublers do **not** loop forever.

## Explanation

Both Doubling Season and Anointed Procession are replacement effects that modify the same event (the creation of a token). When two or more replacement effects are attempting to modify the same event, the affected player chooses which one applies first [CR 616.1]. After one is applied, the process is repeated with any remaining applicable effects [CR 616.1f].

However, each replacement effect gets only **one** opportunity to affect the event [CR 614.5]. So the sequence is:

1. An effect would create **1** token.
2. You choose one doubler (say, Doubling Season). It doubles 1 → **2**.
3. The process repeats; Anointed Procession is still applicable and doubles 2 → **4**.
4. No further replacement effects are applicable (each has already been used once), so the process ends.

The result is 1 × 2 × 2 = **4 tokens**.

This is the same principle as the example in [CR 614.5], where two "double damage" effects turn 2 damage into 8 (not infinite), because each effect applies exactly once.

Review: **correct**. Correct four tokens and each replacement applies once to the event. Now finishes normally.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 12-replacement-choice / repetition 1

A source would deal 3 damage to me. Two ordinary replacement effects apply: one doubles that damage, and the other increases it by 1. Neither is a self-replacement or prevention effect and no other effects apply. Who chooses their order, and can the final damage be 7 or 8?

## Ruling

**You (the affected player) choose the order.** The final damage can be **7** or **8**, depending on which effect you apply first.

## Explanation

Since neither effect is a self-replacement effect, and neither modifies control, causes a copy, or causes a permanent to enter face-down, the choice falls to rule 616.1e: "Any of the applicable replacement and/or prevention effects may be chosen." [CR 616.1e]

The affected player makes this choice per rule 616.1, which states that "the affected object's controller (or its owner if it has no controller) or the affected player chooses one to apply." [CR 616.1]

Once the first effect is applied, the process repeats with the remaining effect [CR 616.1f], yielding:

| Order | Calculation | Result |
|-------|-------------|--------|
| Double first, then +1 | 3 → 6 → 7 | **7 damage** |
| +1 first, then double | 3 → 4 → 8 | **8 damage** |

Doubling damage is confirmed as a replacement effect by rule 701.10g. [CR 701.10g]

So you, as the player being dealt damage, pick whether the result is 7 or 8.

Review: **correct**. Correct affected-player choice, both arithmetic orders, and once-per-effect restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 13-apnap / repetition 1

In a two-player game it is Alice's turn. One ordinary triggered ability Alice controls and one Bob controls trigger simultaneously. Neither triggers from another ability triggering. With no further responses, whose trigger resolves first?

## Ruling

**Bob's triggered ability resolves first.**

## Explanation

When multiple triggered abilities are waiting to go on the stack, they are placed in **APNAP order** (Active Player, then Non-Active Player). Since it is Alice's turn, she is the active player and goes first.

1. **Alice** (active player) puts her triggered ability on the stack.
2. **Bob** (non-active player) puts his triggered ability on the stack.

Each object placed on the stack goes on **top** of everything already there [CR 405.2]. So Bob's ability ends up above Alice's.

When all players pass in succession, the topmost object on the stack resolves [CR 608.1] [CR 405.5]. That is Bob's ability.

## Key citations

- **[CR 603.3b]** – "First, each player, in APNAP order, puts each triggered ability they control with a trigger condition that isn't another ability triggering on the stack in any order they choose."
- **[CR 405.2]** – "Each time an object is put on the stack, it's put on top of all objects already there."
- **[CR 608.1]** – "Each time all players pass in succession, the spell or ability on top of the stack resolves."

This is the standard "non-active player's triggers resolve first" outcome that applies whenever both players have ordinary (non-"another ability triggered") triggers waiting simultaneously.

Review: **correct**. Correct APNAP order and last-in-first-out resolution with supporting sources.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 14-humility-anthem / repetition 1

I control a printed 4/4 creature, Humility, and Glorious Anthem. The creature has no counters or other effects. What is its power/toughness? Does it matter which enchantment entered first?

## Ruling

Your creature is a **2/2**. It does **not** matter which enchantment entered the battlefield first.

## Explanation

The two effects apply in different sublayers of layer 7, so timestamp order is irrelevant:

1. **Layer 7b** – Humility's "have base power and toughness 1/1" is a *setting* effect. It sets the creature's base P/T to 1/1. [CR 613.4b]

2. **Layer 7c** – Glorious Anthem's "get +1/+1" is a *modifying* effect (it adds to P/T without setting it to a specific value). It applies after the setting effect. [CR 613.4c]

The sublayers are applied in the fixed order 7a → 7b → 7c → 7d, regardless of timestamps. [CR 613.4]

So the calculation is: 1/1 (set by Humility) + 1/+1 (from Glorious Anthem) = **2/2**.

Even if Glorious Anthem entered the battlefield before Humility, the result is the same because the layer system always applies setting effects (7b) before modifying effects (7c).

Review: **correct**. Correct 2/2 and sublayer order regardless of timestamps.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 15-own-hexproof / repetition 1

I control a creature with hexproof. May I target it with my own Giant Growth, assuming I can pay for the spell and have priority?

**Yes, you may target your own hexproof creature with Giant Growth.**

Hexproof only restricts targeting by *opponents*. The rule states:

> "Hexproof" on a permanent means "This permanent can't be the target of spells or abilities **your opponents** control." [CR 702.11b]

Since you are the controller of both the creature and the Giant Growth, the hexproof ability imposes no restriction on you. You can freely target your own hexproof creature with your own spells or abilities.

Review: **correct**. Correct own-creature targeting and opponents-only hexproof restriction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 16-first-strike-blocker / repetition 1

My attacking 3/3 has double strike but not trample. Its only blocker is an undamaged 2/2 with no abilities. The blocker dies in the first combat damage step. Does my attacker then deal 3 damage to the player in the second combat damage step?

**No.** Your attacker deals no combat damage in the second combat damage step.

**Explanation:**

In the first combat damage step, your 3/3 with double strike assigns 3 damage to the 2/2 blocker (it's blocked, so it can't assign damage to the player without trample). The blocker dies.

In the second combat damage step, your attacker still has double strike and therefore still assigns damage. However, it is still a *blocked* creature (blocking status is determined when blockers are declared and doesn't change when the blocker dies). The key rule is:

> "A blocked creature assigns its combat damage to the creatures blocking it. If no creatures are currently blocking it (if, for example, they were destroyed or removed from combat), it assigns no combat damage." [CR 510.1c]

Since the blocker is dead and no other creatures are blocking, your attacker assigns **zero** combat damage.

**Why trample would change this:** If your attacker *did* have trample, rule 702.19d would apply:

> "If an attacking creature with trample… is blocked, but there are no creatures blocking it when damage is assigned, its damage is assigned to the defending player and/or planeswalker as though all blocking creatures have been assigned lethal damage." [CR 702.19d]

Without trample, a blocked attacker with no remaining blockers simply deals nothing.

Review: **correct**. Correct no second-step player damage and explicit continued blocked status without trample.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 17-token-blink / repetition 1

An effect exiles my creature token and then immediately tries to return it to the battlefield during the same resolution. No replacement effects apply. Does the token return?

**No, the token does not return to the battlefield.**

Once a token leaves the battlefield, it can't come back. Rule 111.8 states:

> "A token that has left the battlefield can't move to another zone or come back onto the battlefield. If such a token would change zones, it remains in its current zone instead." [CR 111.8]

So when the effect exiles the token, it has left the battlefield. The subsequent instruction to return it to the battlefield fails — the token simply remains in the exile zone. It will cease to exist the next time state-based actions are checked. [CR 111.7]

The fact that both actions occur during the same resolution doesn't change this. The token has already changed zones (battlefield → exile), so it has "left the battlefield" for the purposes of rule 111.8.

Review: **correct**. Correct immediate prohibition on changing zones again and later cessation at the next state-based check; no incorrect interruption of resolution.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 18-summoning-sacrifice / repetition 1

A creature I just cast has "Sacrifice this creature: Draw a card." There is no tap or untap symbol in that cost and no other restriction. When I have priority, can I activate it this turn despite summoning sickness?

**Yes, you can activate it this turn.**

Summoning sickness (rule 302.6) only restricts two things:

1. Activated abilities whose cost includes the **tap symbol** ({T}) or the **untap symbol** ({Q}).
2. Attacking.

Your ability's cost is "Sacrifice this creature," which contains neither the tap nor the untap symbol. Therefore, summoning sickness does not apply to it. As long as you have priority, you may activate it.

**Supporting citations:**

- [CR 302.6] — "A creature's activated ability **with the tap symbol or the untap symbol** in its activation cost can't be activated unless the creature has been under its controller's control continuously since their most recent turn began."
- [CR 117.1b] — "A player may activate an activated ability any time they have priority."

Since your ability's cost is a sacrifice (not a tap or untap), it is not subject to the summoning sickness restriction, and you may activate it on the turn you cast the creature.

Review: **correct**. Correct sacrifice activation and tap/untap-symbol distinction.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

### 19-legend-response / repetition 1

I control two legendary creatures with the same name after a spell resolves. No effect changes the legend rule. Can I respond to the legend rule by casting an instant before choosing one to keep?

**No — you cannot respond to the legend rule with an instant.**

The legend rule is a state-based action, and state-based actions are handled automatically before any player receives priority. The sequence after a spell resolves is:

1. The spell finishes resolving.
2. State-based actions are checked and applied (including the legend rule, if applicable). You choose which legendary permanent to keep; the rest go to their owners' graveyards.
3. Only *then* does the active player receive priority, at which point instants could be cast.

Because the state-based action occurs before priority is granted, there is no window in which a player could cast an instant "in response" to the legend rule.

**Supporting citations:**

- [CR 704.5j] — "If two or more legendary permanents with the same name are controlled by the same player, that player chooses one of them, and the rest are put into their owners' graveyards. This is called the 'legend rule.'"
- [CR 117.2d] — "State-based actions happen automatically when certain conditions are met. See rule 704. They're dealt with before a player would receive priority."
- [CR 117.3b] — "The active player receives priority after a spell or ability (other than a mana ability) resolves."

The practical upshot: if you need to protect one of the two permanents (e.g., with a "can't be put into a graveyard" effect), that protection must already be in place *before* the state-based action is checked. You cannot react to the legend rule itself.

Review: **correct**. Correct no response window, explicit state-based checks before priority, and choice of one legendary permanent. Uses alternative timing evidence 117.5 rather than canonical reference 704.3.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: 704.3

### 20-clarify-interaction / repetition 1

My creature has protection and my opponent used a removal spell. Is my creature safe?

## Ruling

**It depends on what the protection covers and what the removal spell is.**

Protection from a quality (e.g., "protection from red") prevents the following against that permanent:

- **Being targeted** by spells or abilities with that quality [CR 702.16b]
- **Being enchanted** by Auras with that quality [CR 702.16c]
- **Being equipped** by Equipment with that quality [CR 702.16d]
- **Taking damage** from sources with that quality [CR 702.16e]
- **Being blocked** by creatures with that quality [CR 702.16f]

### Key distinction

If the removal spell **targets** your creature and has the stated quality (e.g., a red spell targeting a creature with "protection from red"), it **can't legally target** your creature. The spell would need to choose a different target or fizzle.

If the removal spell is **untargeted** (e.g., "destroy all creatures" or "destroy all red creatures"), protection does **not** save your creature, because protection only prevents targeting, not untargeted effects.

### What I need to give you a definitive answer

1. **What is the exact protection quality?** (e.g., "protection from red," "protection from black," "protection from [player name]")
2. **What is the removal spell?** (name or text) — specifically, does it target, and what color/type is it?

If you can share the card name (use `[[Exact Card Name]]` or card search), I can give you a precise ruling.

Review: **partial**. Asks both clarifications but again asserts protection only prevents targeting, not untargeted effects, contradicting the damage-prevention bullet. Non-targeted damage can be prevented by protection; the unsupported generalization prevents full correctness.
Reviewer: Codex (AI-assisted review; not independently human-validated)

Missing reference groups: none

