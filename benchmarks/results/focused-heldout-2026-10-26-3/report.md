# focused-heldout-2026-10-26-3

Status: **complete** · implementation commit `1ce5d2185b8bed03fdb7e154914bb2778fd96134`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 27/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 78.8% |
| Cases retrieving every expected evidence group | 17/32 |
| Answers with citations | 32/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 1 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 27/32 reviewed |
| Reviewed accuracy | 84.4% |
| Mean reviewed rubric score | 90.6% |
| Median successful response | 7.74 s |
| p95 successful response | 11.76 s |
| Median first visible answer token | 6.32 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 8.89 |
| h02-intervening-if (r1) | 100.0% | correct | 5.86 |
| h03-independent-trigger (r1) | 100.0% | correct | 9.63 |
| h04-replacement-death (r1) | 75.0% | correct | 6.49 |
| h05-simultaneous-death (r1) | 100.0% | correct | 7.18 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 5.66 |
| h07-infect-lifelink (r1) | 100.0% | correct | 6.47 |
| h08-protection-wrath (r1) | 100.0% | correct | 8.99 |
| h09-protection-aura (r1) | 100.0% | correct | 4.94 |
| h10-own-hexproof (r1) | 100.0% | correct | 6.51 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 7.24 |
| h12-split-second (r1) | 100.0% | correct | 11.27 |
| h13-sacrifice-cost (r1) | 66.7% | correct | 7.68 |
| h14-flashback-countered (r1) | 66.7% | correct | 6.42 |
| h15-rebound-countered (r1) | 66.7% | correct | 6.48 |
| h16-persist-counter (r1) | 100.0% | correct | 6.89 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 12.88 |
| h18-blink-target (r1) | 50.0% | correct | 11.33 |
| h19-equip-timing (r1) | 75.0% | correct | 11.76 |
| h20-crew-new-creature (r1) | 66.7% | correct | 9.61 |
| h21-new-vehicle (r1) | 50.0% | correct | 8.36 |
| h22-tapped-blocker (r1) | 0.0% | correct | 8.28 |
| h23-fight-double-strike (r1) | 100.0% | correct | 8.14 |
| h24-leaving-controller (r1) | 100.0% | correct | 8.46 |
| h25-leaving-stack (r1) | 100.0% | correct | 7.81 |
| h26-commander-control (r1) | 100.0% | correct | 7.04 |
| h27-commander-hand (r1) | 0.0% | incorrect | 8.01 |
| h28-replacement-order (r1) | 80.0% | partial | 11.08 |
| h29-empty-library (r1) | 100.0% | correct | 7.20 |
| h30-ambiguous-combat (r1) | 100.0% | partial | 6.41 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 5.83 |
| h32-ambiguous-replacements (r1) | 100.0% | partial | 11.18 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** The abilities go on the stack in the order Alice, Bob, Charlie (bottom to top), so they resolve in the order Charlie, Bob, Alice (top to bottom).

**Why:** When multiple triggered abilities are waiting to be put on the stack, the active player's abilities go on first, then each nonactive player's in turn order [CR 805.7]. Each new object is placed on top of all objects already on the stack [CR 405.2], so Charlie's ability ends up on top and resolves first when all players pass [CR 608.1].

Review: **correct**. Correct stack placement and reverse resolution order; citations support APNAP placement and resolution.
Reviewer: Codex

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability checks your life total again as it resolves, and if you have 39 or less life at that time, it does nothing.

**Why:** Felidar Sovereign's ability uses an "intervening 'if' clause," which means the condition is checked both when the ability triggers and again as it resolves. If the condition isn't met at resolution, the ability is removed from the stack and has no effect [CR 603.4]. The specific ruling confirms this: "If you don't have 40 or more life at that time, the ability won't do anything" [C2].

Review: **correct**. Correctly applies the intervening-if check at resolution; CR 603.4 and the card ruling support it.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. You may still search your library for a basic land card, put it onto the battlefield tapped, and shuffle.

**Why:** Once a triggered ability is on the stack, it exists independently of its source, and destruction or removal of the source doesn't affect it [CR 113.7a]. Solemn Simulacrum's ability effect ("search your library for a basic land card, put that card onto the battlefield tapped, then shuffle") doesn't reference the Simulacrum itself, so nothing about the effect requires the Simulacrum to still be on the battlefield [C1].

Review: **correct**. Correct and cites CR 113.7a directly; the optional search choice is correctly made on resolution.
Reviewer: Codex

Missing reference groups: none

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** Rest in Peace replaces the event of the card being put into a graveyard with exiling it, so the card is never actually put into a graveyard [C1]. Since the "dies" trigger condition requires the card to be put into a graveyard, and that event never happens, the ability does not trigger [C2]. This is consistent with the general principle that a replaced event never occurs [CR 614.6].

Review: **correct**. Correctly explains Rest in Peace replaces the graveyard event, so the creature does not die.
Reviewer: Codex

Missing reference groups: CR 700.4

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **three** times — once for each creature that dies (itself and the two tokens).

**Why:** Blood Artist's trigger condition is "Whenever this creature or another creature dies," and each creature dying is a separate matching event. The card-specific ruling confirms that when Blood Artist and other creatures die simultaneously, its ability triggers for each of those creatures [C2]. This is consistent with the general rule that leaves-the-battlefield abilities look back in time and trigger for each matching event [CR 603.10a].

Review: **correct**. Correctly counts three triggers; the supplied Blood Artist ruling directly supports the count.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain only when damage is *dealt* by the source [CR 702.15b]. If all 3 damage is prevented, no damage is dealt, so the condition for lifelink's effect is never met.

Review: **correct**. Correct; prevented damage is not dealt and causes no lifelink gain.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, they get 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result of damage dealt to a player with giving that player poison counters instead [CR 702.90b]. Lifelink causes the source's controller to gain life equal to the damage dealt, in addition to any other results [CR 702.15b]. Since infect already replaced the life-loss result, the opponent simply receives 3 poison counters while you gain 3 life.

Review: **correct**. Correctly states infect gives poison counters while lifelink grants life.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature. Protection from white does not protect against non-targeting effects that destroy creatures.

**Why:** Protection from white only prevents being targeted by white spells/abilities, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b]–[CR 702.16f]. Wrath of God says "Destroy all creatures" without targeting anything [C1], so none of the protections granted by the protection ability apply. Protection is not a general immunity; it only blocks the specific interactions listed in the rules.

Review: **correct**. Correct; protection does not prevent a nontargeting destroy effect.
Reviewer: Codex

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality means the protected permanent can't be enchanted by Auras that have that quality, and any such Auras already attached are put into their owners' graveyards as a state-based action [CR 702.16c]. Since the Aura is white and the creature now has protection from white, this condition is met.

Review: **correct**. Correctly identifies state-based removal of the Aura to its owner’s graveyard.
Reviewer: Codex

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes. Hexproof only prevents a permanent from being targeted by spells or abilities your *opponents* control. Since you control both Slippery Bogle and the Giant Growth, hexproof does not block the targeting.

**Why:** Hexproof on a permanent means "This permanent can't be the target of spells or abilities your opponents control" [CR 702.11b]. You are not your own opponent, so the restriction does not apply to your own spell. Giant Growth simply requires a target creature, and Slippery Bogle is a legal target for you [CR 115.2].

Review: **correct**. Correct; the player is not their own opponent for hexproof.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Even if you decline to pay the ward cost, Abrupt Decay is not countered.

**Why:** Ward's ability says "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but Abrupt Decay's text states "This spell can't be countered" [C1]. The official ruling confirms this interaction directly: "you may still pay the ward cost, but Abrupt Decay won't be countered even if you don't" [C2]. The "can't be countered" protection overrides Ward's countering effect.

Review: **correct**. Correct; Ward triggers, but its counter instruction cannot counter Abrupt Decay; the spell resolves.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up as a special action while Krosan Grip is on the stack, its triggered ability goes on the stack above Grip, and you can legally redirect Grip to your other artifact.

**Why:** Split second permits special actions and triggered abilities to be put on the stack normally [CR 702.61b], and turning a face-down permanent face up is a special action [CR 702.37e]. Willbender's ability triggers when it is turned face up [C13], and since it has a single target, it is a valid object for Willbender's "change the target" effect [CR 115.7a]. Because the ability is placed on top of the stack, it resolves before Grip, changing Grip's target to your other artifact, which Grip then destroys.

Review: **correct**. Correct; turning face up is a special action and the Willbender ruling supports redirection.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice to prevent you from paying the cost.

**Why:** The creature is put on the stack first, then costs are paid, and only after all steps are complete does the spell become cast and the controller receive priority [CR 601.2a], [CR 601.2h], [CR 601.2i]. Players can only respond once the spell has been cast and all its costs have been paid; no one can interfere with the creature you sacrificed to prevent you from casting the spell [C3].

Review: **correct**. Correct; the sacrifice is paid during casting before an opponent receives priority.
Reviewer: Codex

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** Because the flashback cost was paid, the card is exiled instead of going to the graveyard any time it would leave the stack, including when it's countered [CR 702.34a]. A countered spell never resolves, so its "Draw a card" instruction is never applied [C2].

Review: **correct**. Correct; flashback exiles the spell when it leaves the stack, including if countered.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not function. The card goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never triggers. The official ruling confirms this explicitly: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn." [C5]

Review: **correct**. Correct; rebound applies only as the spell resolves, so a countered spell does not rebound.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it is put into a graveyard from the battlefield, persist does not return it.

**Why:** Persist's condition is "if it had no -1/-1 counters on it" [CR 702.79a]. The game checks the creature's state just before it leaves the battlefield, and if it has any -1/-1 counters at that moment, the condition isn't met and the ability doesn't return it [C6].

Review: **correct**. Correct; an existing -1/-1 counter prevents persist from triggering.
Reviewer: Codex

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** Per [CR 704.8], when a state-based action results in a permanent leaving the battlefield at the same time other state-based actions are performed, that permanent's last known information is derived from the game state *before* any of those state-based actions were performed. In your scenario, before state-based actions are checked, Young Wolf has a +1/+1 counter on it (alongside the -1/-1 counter). Since it had a +1/+1 counter at that moment, the condition for undying ("if it had no +1/+1 counters on it" per [CR 702.93a]) is not met. The supplied example in [CR 704.8] uses Young Wolf in nearly this exact situation and concludes undying will not trigger.

Review: **correct**. Correct; pre-SBA last known information sees the +1/+1 counter, so undying does not trigger.
Reviewer: Codex

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The Lightning Bolt will fizzle and deal no damage.

**Why:** When Cloudshift resolves, it exiles the creature and returns it to the battlefield as a new object. The returned card is not the target of any spell that targeted the original creature [C5]. Since the original creature is no longer on the battlefield, it is no longer a legal target [CR 115.2], so the Lightning Bolt has no legal target when it tries to resolve and will fizzle.

Review: **correct**. Correct; Cloudshift creates a new object and the original Bolt target is illegal.
Reviewer: Codex

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. Colossus Hammer's equip ability can only be activated as a sorcery, so you cannot activate it in response to Lightning Bolt while it is on the stack.

**Why:** The equip ability explicitly states "Equip only as a sorcery" [C2], and the equip keyword is defined with that same restriction [CR 702.6a]. A sorcery-speed ability can only be activated during your main phase when the stack is empty, so it is not a legal response to a spell your opponent has already cast. Since you stated no effect grants special activation permission, there is no way around this restriction.

Review: **correct**. Correct; equip is sorcery-speed and cannot be activated while Bolt is on the stack.
Reviewer: Codex

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost even though it just came under your control and has no haste.

**Why:** The crew ability is an activated ability of the Vehicle, not of the creature being tapped. The creature is simply paying a cost (tapping itself) for another permanent's ability, which is not restricted by summoning sickness. The official ruling for Smuggler's Copter confirms this directly: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control." [C12] The crew cost requires only that the creature be untapped and have sufficient power [CR 702.122a].

Review: **correct**. Correct; a newly controlled creature may be tapped to pay another object’s crew cost.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No. Because you cast it this turn, it hasn't been under your control continuously since your turn began, and without haste it can't attack.

**Why:** A creature can't attack unless it has been controlled by its controller continuously since their most recent turn began, unless it has haste [CR 702.10b]. The Copter entered the battlefield this turn, so it fails that requirement. The ruling for Smuggler's Copter explicitly confirms this: "It can't attack unless you've controlled it continuously since your turn began" [C10].

Review: **correct**. Correct; the newly controlled Vehicle cannot attack without haste after becoming a creature.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from assigning combat damage.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends, whichever comes first [CR 509.1g]. Tapping is not "removing from combat," so the creature is still blocking. During the combat damage step, a blocking creature assigns combat damage to the creature it's blocking [CR 510.1d]. The only ways to stop it from dealing combat damage are to remove it from combat (e.g., destroy it, exile it, or an effect that specifically removes it from combat) or to change what it's blocking.

Review: **correct**. Correct; tapping does not remove a declared blocker or prevent combat-damage assignment.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 3 damage marked on it.

**Why:** In a fight, each creature deals damage equal to its power to the other [CR 701.14a]. Double strike only modifies the combat damage step [CR 702.4a], but fight damage is not combat damage [CR 701.14d], so double strike has no effect here. The 3/3 has 4 damage marked on it (exceeding its toughness of 3), so it will die; the 4/4 has 3 damage marked on it (less than its toughness of 4), so it survives.

Review: **correct**. Correct and precise: the 4/4 survives with 3 damage marked, and double strike does not affect fight damage.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature remains in the game under Alice's control.

**Why:** When a player leaves the game, all objects owned by that player leave the game, and any effects giving that player control of objects end [CR 800.4a]. Since Bob owns Control Magic, it leaves the game. The creature is owned by Alice, who remains in the game, so it stays and reverts to her control. This is exactly the scenario described in the example for [CR 800.4a]: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control."

Review: **correct**. Correct; Bob’s owned Aura leaves with him and its control effect ends, returning control to Alice.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No. The Lightning Bolt leaves the game and does not resolve.

**Why:** When a player leaves the game, all objects they own leave the game [CR 800.4a]. The Lightning Bolt card on the stack is owned by Bob, so it leaves the game as part of that process. Since it is no longer on the stack, it cannot resolve. (Objects on the stack *not* represented by cards would cease to exist instead, but a card simply leaves the game.)

Review: **correct**. Correct; Bob’s owned spell leaves the game when he leaves and cannot resolve.
Reviewer: Codex

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 and 9 add together to 21, and you lose the game.

**Why:** The rule tracks combat damage dealt "by the same commander" over the course of the game, not by a specific controller [CR 903.10a]. The commander designation is an attribute of the card itself and persists regardless of who controls it [CR 903.3]. So all combat damage that commander deals to you across the game is accumulated together, and reaching 21 is a state-based action that causes you to lose [CR 704.6c].

Review: **correct**. Correct; commander damage is tracked by the same commander across control changes.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** No. You may not choose the command zone instead of returning your commander to your hand. The state-based action that lets you put a commander into the command zone applies only when the commander is in a graveyard or in exile, not when it is being returned to hand.

**Why:** [CR 704.6d] states that the option to put a commander into the command zone arises when it "is in a graveyard or in exile and that object was put into that zone since the last time state-based actions were checked." A "return to hand" event does not place the commander in either of those zones, so this state-based action does not apply. There is no replacement effect in the supplied rules that would redirect a "return to hand" event to the command zone.

Review: **incorrect**. Incorrect. The answer says the command-zone option is only a state-based action; CR 903.9b, the applicable replacement effect for hand/library destinations, was omitted from packed evidence. Its categorical conclusion is wrong.
Reviewer: Codex

Missing reference groups: CR 903.9b

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The two possible totals are **8** (Furnace of Rath first, then Torbran) or **10** (Torbran first, then Furnace of Rath). Your opponent will choose the order that results in less damage to themselves, which is 8.

**Why:** When multiple replacement effects modify how much damage is dealt, the player being dealt damage chooses the order to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace doubles it to 10. Applying Furnace first gives 3 × 2 = 6, then Torbran adds 2 for 8. Each replacement effect gets only one opportunity to affect the event [CR 614.5].

Review: **partial**. The chooser and both possible totals are correct, but the claim that the opponent will choose 8 predicts a player choice without rules support; mark unsupported.
Reviewer: Codex

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library by itself does not cause you to lose the game. You lose only if you *attempt to draw* a card from a library that has no cards in it.

**Why:** The state-based action that causes a loss is specifically tied to the act of attempting a draw from an empty library [CR 704.5b], [CR 121.4]. The general list of ways to lose the game includes life total at 0 or less [CR 104.3b] and ten or more poison counters [CR 104.3d], but an empty library alone is not among them. So as long as no effect causes you to draw, your empty library is not a losing condition on its own.

Review: **correct**. Correct; an empty library alone is not a loss absent an attempted draw.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** If your attacking creature has trample, you must assign at least lethal damage to each blocking creature before assigning any excess to your opponent. The amount that "gets through" is your creature's power minus the total toughness of the blocking creatures (accounting for damage already marked on them and damage from other creatures assigned in the same combat damage step).

**Why:** Trample modifies how an attacking creature's combat damage is assigned: you first assign lethal damage to the blockers, then any remaining damage may be assigned to the player or planeswalker you're attacking [CR 702.19b]. If your creature does *not* have trample, all of its damage is assigned to the blocking creature(s) and none reaches your opponent [CR 510.1c]. If you share your creature's power and the blocker's toughness (and any damage already on it), I can give you the exact number.

Review: **partial**. Both conditional branches are correct and useful, but frozen criterion 1 asks for missing stats/abilities, so it is false under the unchanged strict rubric; product-aligned.
Reviewer: Codex

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No to both. A copy does not get the counters on the original creature, and it does not get the bonus from an enchantment attached to it.

**Why:** When copying an object, the copy acquires only the copiable values derived from the object's printed text (as modified by other copy effects and certain "as it enters" abilities). Counters, status, and other effects (including type-changing and text-changing effects from enchantments) are explicitly not copied [CR 707.2].

Review: **incorrect**. The general copy rule answer is correct and product-aligned, but both strict frozen criteria ask for specifics rather than a definitive general answer.
Reviewer: Codex

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** You choose which replacement effect to apply first (following the ordering in [CR 616.1a]–[CR 616.1e]), apply it, then check whether the other effect is still applicable to the modified event. If it is, you apply it as well. The exact number of tokens depends on what each effect does.

**Why:** When two or more replacement effects attempt to modify the same event, the affected player chooses one to apply, then the process repeats with any remaining applicable effects [CR 616.1], [CR 616.1f]. Replacement effects that apply "if an effect would create one or more tokens" apply even if another replacement effect is the one creating them [CR 614.16]. The specific outcome (e.g., double, triple, or some other number) depends on the exact wording of both effects.

Review: **partial**. Gives the general ordering and reevaluation rule, but does not ask for the exact effect text the frozen criterion requires. It mentions hypothetical outcome categories (double/triple) despite the request lacking effect text; criterion 1 fails, criterion 2 passes because it does not assert a user-specific total.
Reviewer: Codex

Missing reference groups: none

