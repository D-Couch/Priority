# focused-heldout-2026-10-26-2

Status: **complete** · implementation commit `31e05b08fe647d5cd8dbe29e6f3b7c64c109837d`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 28/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 79.6% |
| Cases retrieving every expected evidence group | 18/32 |
| Answers with citations | 32/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 28/32 reviewed |
| Reviewed accuracy | 87.5% |
| Mean reviewed rubric score | 89.1% |
| Median successful response | 7.48 s |
| p95 successful response | 11.81 s |
| Median first visible answer token | 5.87 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 10.94 |
| h02-intervening-if (r1) | 100.0% | correct | 6.00 |
| h03-independent-trigger (r1) | 100.0% | correct | 6.56 |
| h04-replacement-death (r1) | 100.0% | correct | 6.68 |
| h05-simultaneous-death (r1) | 100.0% | correct | 7.84 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 4.70 |
| h07-infect-lifelink (r1) | 100.0% | correct | 7.63 |
| h08-protection-wrath (r1) | 100.0% | correct | 8.55 |
| h09-protection-aura (r1) | 100.0% | correct | 5.06 |
| h10-own-hexproof (r1) | 100.0% | correct | 6.18 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 7.18 |
| h12-split-second (r1) | 100.0% | correct | 10.30 |
| h13-sacrifice-cost (r1) | 66.7% | correct | 11.19 |
| h14-flashback-countered (r1) | 66.7% | correct | 5.73 |
| h15-rebound-countered (r1) | 66.7% | correct | 6.22 |
| h16-persist-counter (r1) | 100.0% | correct | 6.69 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 16.82 |
| h18-blink-target (r1) | 50.0% | correct | 10.08 |
| h19-equip-timing (r1) | 75.0% | correct | 11.81 |
| h20-crew-new-creature (r1) | 66.7% | correct | 8.51 |
| h21-new-vehicle (r1) | 50.0% | correct | 7.12 |
| h22-tapped-blocker (r1) | 0.0% | correct | 9.12 |
| h23-fight-double-strike (r1) | 100.0% | correct | 7.68 |
| h24-leaving-controller (r1) | 100.0% | correct | 7.97 |
| h25-leaving-stack (r1) | 100.0% | correct | 6.99 |
| h26-commander-control (r1) | 100.0% | correct | 7.33 |
| h27-commander-hand (r1) | 0.0% | incorrect | 7.81 |
| h28-replacement-order (r1) | 80.0% | correct | 8.89 |
| h29-empty-library (r1) | 100.0% | correct | 6.15 |
| h30-ambiguous-combat (r1) | 100.0% | partial | 5.72 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 6.81 |
| h32-ambiguous-replacements (r1) | 100.0% | incorrect | 10.12 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** They go on the stack in turn order (Alice, then Bob, then Charlie), so they resolve in reverse: Charlie's ability first, then Bob's, then Alice's.

**Why:** In a multiplayer game, the active player puts their triggered abilities on the stack first, then each nonactive player in turn order does the same [CR 805.7]. Each new object is placed on top of all objects already there [CR 405.2], and the top of the stack resolves first when all players pass [CR 405.5]. So the stack (bottom to top) is Alice → Bob → Charlie, and resolution proceeds Charlie → Bob → Alice.

Review: **correct**. Correct stack placement and reverse resolution order; citations support the APNAP and stack rules.
Reviewer: Codex

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability triggers because you had 40 or more life when your upkeep began, but it checks the condition again as it resolves. Since you're at 39 life at that point, the ability is removed from the stack and does nothing.

**Why:** This is the "intervening 'if' clause" rule: the condition is checked both when the ability triggers and again when it resolves, and it must be true at both times for the effect to occur [CR 603.4]. The official ruling for Felidar Sovereign confirms this exact sequence [C2].

Review: **correct**. Correctly applies the intervening-if check at resolution; CR 603.4 and card ruling support it.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. Once the triggered ability is on the stack, it exists independently of Solemn Simulacrum. Destroying the Simulacrum before the ability resolves does not remove or affect the ability, so it will still resolve and you may search for a basic land.

**Why:** A triggered ability, once on the stack, is independent of its source; destruction or removal of the source after that time won't affect the ability [CR 113.7a]. The ability's effect (searching for a basic land) does not reference the Simulacrum at resolution, so there is nothing to fail.

Review: **correct**. Correct and cites CR 113.7a directly; the optional search choice is correctly made on resolution.
Reviewer: Codex

Missing reference groups: none

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exiling the card, so the card is never put into a graveyard and the trigger condition is never met [C1]. This is explicitly confirmed by the card's ruling: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Review: **correct**. Correctly explains that Rest in Peace replaces the graveyard event, so the creature does not die.
Reviewer: Codex

Missing reference groups: none

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **3 times** — once for itself dying and once for each of the two other creatures dying.

**Why:** Blood Artist's trigger condition is "whenever this creature or another creature dies," so it triggers for each creature that dies in the event, including itself. The official ruling confirms that when Blood Artist and other creatures die simultaneously, its ability triggers for each of those creatures [C2]. Since three creatures die (Blood Artist + two tokens), the ability triggers three times.

Review: **correct**. Correctly counts three triggers; supplied Blood Artist ruling directly supports the count.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain when damage is *dealt* by a source with lifelink [CR 702.15b]. Prevented damage is not dealt, so the condition for lifelink's effect is never met.

Review: **correct**. Correct; prevented damage is not dealt and causes no lifelink gain.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged. Your opponent gets 3 poison counters. You gain 3 life.

**Why:** Infect replaces the "lose life" result with "get that many poison counters" [CR 702.90b]. Lifelink causes the source's controller to gain that much life "in addition to any other results that damage causes" [CR 702.15b]. Since infect changes what happens to the opponent (poison counters instead of life loss) and lifelink adds a separate life-gain result for you, both apply simultaneously.

Review: **correct**. Correctly states poison counters replace life loss while lifelink still grants life.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature. Protection from white does not prevent it.

**Why:** Protection from a quality prevents being targeted by spells of that quality, being enchanted by Auras of that quality, being equipped by Equipment of that quality, damage from sources of that quality, and being blocked by creatures of that quality [CR 702.16b]–[CR 702.16f]. Wrath of God is a global "destroy all creatures" effect that doesn't target anything [C1], so none of the protections granted by the protection ability apply. The creature is destroyed by the spell's effect.

Review: **correct**. Correct; protection does not prevent a nontargeting destroy effect.
Reviewer: Codex

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from white means the permanent can't be enchanted by Auras that are white. Any such Auras already attached to it are put into their owners' graveyards as a state-based action [CR 702.16c]. This happens automatically the next time state-based actions are checked; no player needs to do anything.

Review: **correct**. Correctly identifies state-based removal of the Aura to its owner’s graveyard.
Reviewer: Codex

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes. Hexproof only prevents a permanent from being targeted by spells or abilities your *opponents* control. Since you control both the Slippery Bogle and the Giant Growth, hexproof does not block the targeting.

**Why:** Hexproof on a permanent means "This permanent can't be the target of spells or abilities your opponents control" [CR 702.11b]. Your own spell is not controlled by an opponent, so the restriction does not apply. Giant Growth simply requires a legal creature target [CR 115.2], and your own creature is a legal target for your own spell.

Review: **correct**. Correct; the player is not their own opponent for hexproof.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost. Abrupt Decay still resolves and destroys the target.

**Why:** Ward's ability says "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but Abrupt Decay's text states "This spell can't be countered" [C1]. The official ruling confirms this interaction directly: "Abrupt Decay won't be countered even if you don't" [C2]. The ward ability triggers and resolves, but its countering effect fails because Abrupt Decay is immune to being countered.

Review: **correct**. Correct; Ward triggers, but its counter instruction cannot counter Abrupt Decay; the spell resolves.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up, its trigger goes on the stack, and you can use it to redirect Krosan Grip to your other artifact.

**Why:** Turning a face-down permanent face up is a special action, and special actions are permitted while a spell with split second is on the stack [CR 702.61b] [C5]. Triggered abilities trigger and are put on the stack as normal during split second [CR 702.61b] [C2]. Willbender's trigger fires when you turn it face up [C13], and since Krosan Grip has a single target, you can change that target to another legal target (your other artifact) [CR 115.7a].

Review: **correct**. Correct; turning face up is a special action and the supplied Willbender ruling supports redirection.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond by destroying the creature because the sacrifice is paid as part of the cost, which is completed before your opponent ever receives priority.

**Why:** When you cast Fling, the spell is put on the stack, then you pay all costs—including sacrificing the 4/4 creature—and only after those steps are complete does the spell become cast and your opponent get the chance to respond [CR 601.2a], [CR 601.2h], [CR 601.2i]. By the time your opponent has priority, the creature is already in your graveyard and is no longer a permanent they could target [CR 115.2]. The card's own ruling confirms this: "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell" [C3].

Review: **correct**. Correct; costs are paid as part of casting before the opponent receives priority.
Reviewer: Codex

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** Flashback includes a static ability that says "if the flashback cost was paid, exile this card instead of putting it anywhere else any time it would leave the stack" [CR 702.34a]. This applies whether the spell resolves, is countered, or leaves the stack in any other way [C2]. Since the spell was countered, it never resolved, so the "draw a card" instruction was never carried out.

Review: **correct**. Correct; flashback exiles the spell when it leaves the stack, including after it is countered.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not apply. The card goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never triggers. The card is put into its owner's graveyard as normal, and you lose the chance to cast it again [C5].

Review: **correct**. Correct; rebound applies only as the spell resolves, so a countered spell does not rebound.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it is put into the graveyard from the battlefield, persist does not return it.

**Why:** Persist's trigger condition requires that the permanent "had no -1/-1 counters on it" at the moment it is put into the graveyard [CR 702.79a]. If it has one or more -1/-1 counters, the condition is not met and the ability does not trigger. This is confirmed by the Kitchen Finks ruling, which explains that persist checks the creature's state just before it leaves the battlefield [C6].

Review: **correct**. Correct; an existing -1/-1 counter prevents persist from triggering.
Reviewer: Codex

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** Undying's condition is "if it had no +1/+1 counters on it" when it is put into a graveyard from the battlefield [CR 702.93a]. Because the creature dying and the opposite counters being removed are state-based actions performed simultaneously, the permanent's last known information is derived from the game state *before* any of those actions were performed [CR 704.8]. In that state, Young Wolf still had a +1/+1 counter on it, so the "no +1/+1 counters" condition is not met and undying does not trigger. This is the exact scenario illustrated in the example under [CR 704.8].

Review: **correct**. Correct; pre-SBA last known information includes the +1/+1 counter, so undying does not trigger.
Reviewer: Codex

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The Lightning Bolt will fizzle and deal no damage.

**Why:** Cloudshift's ruling explicitly states that the returned card won't be the target of any spells or abilities that targeted it before [C5]. Since the creature left the battlefield and came back as a new object, the original target no longer exists, so the Bolt has no legal target when it tries to resolve. (Note: if the creature were a token, it would cease to exist when exiled and not return at all [C6].)

Review: **correct**. Correct; Cloudshift creates a new object and the original Bolt target is illegal.
Reviewer: Codex

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. You cannot activate Colossus Hammer's equip ability in response to Lightning Bolt.

**Why:** The equip ability states "Equip only as a sorcery" [C2], meaning it can only be activated during your main phase when the stack is empty. Once Lightning Bolt is on the stack, you no longer have sorcery-speed timing, so the equip ability is not legal to activate. Additionally, even if you could equip it, the +10/+10 would not prevent Lightning Bolt from dealing 3 damage to the target creature [C1]; it would only make the creature larger, which might help it survive the damage if its toughness is sufficient.

Review: **correct**. Correct; equip is sorcery-speed and cannot be activated while Bolt is on the stack.
Reviewer: Codex

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the Crew 1 cost even though it just came under your control and doesn't have haste.

**Why:** The "summoning sickness" restriction (needing haste) applies to a creature attacking or activating its own tap abilities, but tapping a creature to pay a cost for another object's ability is not restricted. The official ruling for Smuggler's Copter explicitly confirms this: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control." [C12] The Crew ability itself is an activated ability of the Vehicle, not the creature being tapped. [CR 702.122a]

Review: **correct**. Correct; a newly controlled creature can be tapped to pay another object’s crew cost.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No. Even after crewing it, it cannot attack this turn.

**Why:** Once a Vehicle becomes a creature, it can't attack unless you've controlled it continuously since your turn began [C10]. Since you cast it this turn, that condition isn't met, and without haste there's no exception [CR 702.10b].

Review: **correct**. Correct; the newly controlled Vehicle cannot attack without haste after becoming a creature.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping does not remove a creature from combat, so it still assigns combat damage equal to its power (3) to the creature it's blocking.

**Why:** A creature remains a blocking creature until it's removed from combat or the combat phase ends [CR 509.1g]. Tapping is merely a change in the tapped/untapped state, not removal from combat. At the combat damage step, each blocking creature assigns combat damage equal to its power to the creatures it's blocking [CR 510.1a], [CR 510.1d].

Review: **correct**. Correct; tapping does not remove a declared blocker or prevent combat damage assignment.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 3 damage marked on it.

**Why:** In a fight, each creature deals damage equal to its power to the other [CR 701.14a]. Double strike has no effect here because it modifies the combat damage step [CR 702.4a], and fight damage is explicitly not combat damage [CR 701.14d]. The 4 damage marked on the 3/3 is lethal (exceeds its toughness of 3), while the 3 damage marked on the 4/4 is not (less than its toughness of 4).

Review: **correct**. Correct and uses precise terminology: the 4/4 survives with 3 damage marked, and double strike does not affect fight damage.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature reverts to Alice's control.

**Why:** When a player leaves the game, all objects they own leave the game and any effects giving them control of objects end [CR 800.4a]. Since Bob owns the Control Magic, it leaves the game; since Alice owns the creature, it remains on the battlefield and reverts to her control once the control-changing effect ends. This is exactly the scenario illustrated in the example: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control" [CR 800.4a].

Review: **correct**. Correct; the Aura leaves with Bob and its control effect ends, returning the creature to Alice.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, the Lightning Bolt does not resolve. It leaves the game.

**Why:** When a player leaves the game, all objects owned by that player leave the game [CR 800.4a]. Since Bob owns the Lightning Bolt card, it leaves the game as part of this process and never gets the chance to resolve. The fact that it was targeting Alice is irrelevant at this point—the object simply ceases to be in the game.

Review: **correct**. Correct; Bob’s owned spell leaves the game when he leaves and cannot resolve.
Reviewer: Codex

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. Those 12 + 9 = 21 combat damage points add together, and you lose the game.

**Why:** Commander damage is tracked per commander (the card), not per controller. The rule states that a player who has been dealt 21 or more combat damage "by the same commander over the course of the game" loses [CR 903.10a]. The commander designation is an attribute of the card itself and persists regardless of who controls it or what zone it's in [CR 903.3]. So all combat damage that particular commander has dealt to you across the entire game counts toward the threshold, no matter who was controlling it when each instance was dealt.

Review: **correct**. Correct; the threshold tracks damage by the same commander across control changes.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** No. If an effect returns your commander from the battlefield to your hand, it goes to your hand. You cannot choose the command zone instead. The command zone option is a state-based action that applies only when your commander is in a graveyard or in exile, not when it is being returned to your hand.

**Why:** The Commander state-based action specifically triggers when a commander "is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked" [CR 704.6d]. A "return to hand" event does not place the commander in either of those zones, so that state-based action never applies. This is not a replacement effect you can elect; it is a separate, automatic game action that only fires under the specific conditions listed [CR 704.1].

Review: **incorrect**. Incorrect: CR 903.9b, the replacement rule that permits moving a commander to the command zone from hand-bound events, was not packed. The answer invents an incorrect state-based-action-only explanation.
Reviewer: Codex

Missing reference groups: CR 903.9b

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The possible totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran).

**Why:** When multiple replacement effects modify how much damage a source would deal, the player being dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace doubles it to 10. Applying Furnace first gives 3 × 2 = 6, then Torbran adds 2 for 8. Your opponent picks whichever order they prefer.

Review: **correct**. Correct chooser and both possible totals; it no longer predicts which order the opponent chooses.
Reviewer: Codex

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library is not itself a losing condition. You only lose if you *attempt to draw* a card from a library that has no cards in it.

**Why:** The state-based action that causes a loss specifically requires that a player "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked" [CR 704.5b]. Similarly, [CR 121.4] frames the loss as applying to "a player who attempts to draw a card from a library with no cards in it." Simply having zero cards in your library, without a draw attempt, does not trigger this loss.

Review: **correct**. Correct; an empty library alone is not a loss absent an attempted draw.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** If your attacking creature has trample, you must first assign lethal damage to the blocking creature(s). Any damage beyond that can be assigned to your opponent. If your creature does *not* have trample, none of its damage can get through to your opponent when it's blocked.

**Why:** Trample modifies damage assignment so that excess damage beyond what's needed to kill the blocker(s) may be assigned to the defending player [CR 702.19b]. Without trample, a blocked creature assigns all its combat damage to the creatures blocking it [CR 510.1c]. "Lethal damage" means damage equal to the blocker's toughness (accounting for damage already marked on it and damage from other creatures assigned in the same combat damage step) [CR 702.19b].

Review: **partial**. Both branches are useful and correct, but frozen criterion 1 asks for missing stats/abilities, so it remains false under the unchanged strict rubric; product-aligned.
Reviewer: Codex

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No to both. Your copy does not get the counters on the original creature, and it does not get the bonus from an enchantment attached to it.

**Why:** When copying an object, the copy acquires only the copiable values of the original's characteristics (name, mana cost, color, types, rules text, power, toughness, loyalty, etc.). "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." [CR 707.2] An enchantment's bonus is a continuous effect from a separate source, so it falls under "other effects" and is not part of the copiable values.

Review: **incorrect**. The general rule answer is correct and product-aligned, but both strict frozen criteria ask for specifics rather than a definitive general answer.
Reviewer: Codex

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** You don't automatically get a fixed number — the affected player chooses which replacement effect applies first, then the process is repeated to see if the other effect still applies to the modified event.

**Why:** When two or more replacement effects are attempting to modify the same event, the affected player chooses one to apply [CR 616.1]. Once that effect has been applied, the process is repeated, taking into account only replacement effects that would now be applicable to the modified event [CR 616.1f]. Whether the second effect still applies depends on what it does and what the modified event now looks like. For example, if both effects say "create twice as many tokens instead," the player chooses one, applies it (doubling the count), then the other is still applicable to the modified event and doubles it again. If the second effect modifies a different aspect (e.g., how the token enters), it may apply independently. The exact outcome depends on the specific wording of both effects.

Review: **incorrect**. The general ordering rule is correct, but the answer adds hypothetical examples despite the unspecified effects and does not ask for details required by the frozen rubric; strict criteria fail.
Reviewer: Codex

Missing reference groups: none

