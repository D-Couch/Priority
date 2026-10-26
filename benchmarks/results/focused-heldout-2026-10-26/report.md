# focused-heldout-2026-10-26

Status: **complete** · implementation commit `8b30a311015f6b7df72a8522ec3d89522ef45572`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 28/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 82.7% |
| Cases retrieving every expected evidence group | 19/32 |
| Answers with citations | 32/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 2 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 28/32 reviewed |
| Reviewed accuracy | 87.5% |
| Mean reviewed rubric score | 95.3% |
| Median successful response | 7.46 s |
| p95 successful response | 11.13 s |
| Median first visible answer token | 6.10 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 10.66 |
| h02-intervening-if (r1) | 100.0% | correct | 5.87 |
| h03-independent-trigger (r1) | 100.0% | correct | 9.37 |
| h04-replacement-death (r1) | 100.0% | correct | 7.04 |
| h05-simultaneous-death (r1) | 100.0% | correct | 7.36 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 5.08 |
| h07-infect-lifelink (r1) | 100.0% | correct | 7.60 |
| h08-protection-wrath (r1) | 100.0% | correct | 9.48 |
| h09-protection-aura (r1) | 100.0% | correct | 5.01 |
| h10-own-hexproof (r1) | 100.0% | correct | 5.88 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 7.09 |
| h12-split-second (r1) | 100.0% | correct | 11.13 |
| h13-sacrifice-cost (r1) | 66.7% | correct | 8.21 |
| h14-flashback-countered (r1) | 66.7% | correct | 5.10 |
| h15-rebound-countered (r1) | 66.7% | correct | 6.29 |
| h16-persist-counter (r1) | 100.0% | correct | 7.38 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 12.90 |
| h18-blink-target (r1) | 50.0% | correct | 8.04 |
| h19-equip-timing (r1) | 75.0% | correct | 9.99 |
| h20-crew-new-creature (r1) | 66.7% | correct | 8.82 |
| h21-new-vehicle (r1) | 50.0% | correct | 7.26 |
| h22-tapped-blocker (r1) | 0.0% | correct | 7.13 |
| h23-fight-double-strike (r1) | 100.0% | partial | 7.70 |
| h24-leaving-controller (r1) | 100.0% | correct | 7.75 |
| h25-leaving-stack (r1) | 100.0% | correct | 9.68 |
| h26-commander-control (r1) | 100.0% | correct | 7.35 |
| h27-commander-hand (r1) | 100.0% | correct | 7.46 |
| h28-replacement-order (r1) | 80.0% | partial | 9.72 |
| h29-empty-library (r1) | 100.0% | correct | 7.46 |
| h30-ambiguous-combat (r1) | 100.0% | partial | 6.33 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 6.75 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 8.11 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** The abilities go on the stack in the order Alice, Bob, Charlie (bottom to top), and resolve in the order Charlie, Bob, Alice (top to bottom).

**Why:** Before the active player receives priority at the beginning of upkeep, all triggered abilities are put on the stack [CR 117.3a], [CR 503.1a]. The active player's triggered abilities are placed first, then each nonactive player's in turn order [CR 805.7]. Since the top of the stack resolves first [CR 608.1], Charlie's ability resolves first, then Bob's, then Alice's.

Review: **correct**. Correct stack order and reverse resolution; cited rules establish APNAP placement and resolution order.
Reviewer: Codex

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability checks your life total again as it resolves, and if you have 39 or less life at that time, it is removed from the stack and has no effect.

**Why:** Felidar Sovereign's ability uses an "intervening 'if' clause," which means the condition is checked both when the ability triggers and again as it resolves. If the condition isn't true at resolution, the ability does nothing. [CR 603.4] [C2]

Review: **correct**. Correctly says the win does not occur after the life total falls below 40; CR 603.4 and the card ruling support the second check.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. Once the triggered ability is on the stack, it exists independently of the Simulacrum, so destroying the Simulacrum does not remove or affect the ability. You still get to choose whether to search for a basic land when it resolves.

**Why:** A triggered ability on the stack is not affected by the destruction or removal of its source [CR 113.7a]. The "may" choice is made when the ability resolves, not when it triggers [CR 603.5]. Since the ability's effect (searching your library) does not require the Simulacrum to still be on the battlefield, it resolves normally.

Review: **correct**. Correct; now cites CR 113.7a directly for source independence and CR 603.5 for the optional search choice on resolution.
Reviewer: Codex

Missing reference groups: none

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No. Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** "Dies" is defined as "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exile, so the creature is never put into a graveyard and therefore never dies [C2]. Since the trigger condition is never met, the ability does not trigger at all.

Review: **correct**. Correct; CR 700.4 defines dies and the supplied Rest in Peace ruling supports replacement with exile.
Reviewer: Codex

Missing reference groups: none

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **three** times — once for itself dying and once for each of the two other creatures dying.

**Why:** Blood Artist's trigger condition is "whenever this creature or another creature dies," so it matches each individual creature death event. Zone-change triggers look back in time, meaning the ability triggers even though Blood Artist is no longer on the battlefield when the other creatures die [CR 603.10a]. The card-specific ruling confirms this: "If Blood Artist and one or more other creatures die at the same time, its ability will trigger for each of those creatures" [C2].

Review: **correct**. Correctly counts all three deaths, including Blood Artist itself; the supplied card ruling directly supports the count.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain when damage is *dealt* by a source with lifelink [CR 702.15b]. Prevented damage is not dealt, so the condition for lifelink's effect is never met.

Review: **correct**. Correct: prevented damage is not dealt, so lifelink causes no life gain.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, they get 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result of damage dealt to a player with gaining poison counters instead [CR 702.90b]. Lifelink causes the source's controller to gain life equal to the damage dealt, in addition to any other results [CR 702.15b]. Since infect already replaced the life-loss result, the opponent simply receives 3 poison counters while you gain 3 life.

Review: **correct**. Correctly distinguishes infect poison counters from life loss and applies lifelink independently.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature.

**Why:** Protection from white prevents being targeted by white spells/abilities, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b]–[CR 702.16f]. Wrath of God says "Destroy all creatures" without targeting, dealing damage, or otherwise interacting with the creature in any of those ways [C1]. Since none of protection's clauses apply to a non-targeting, non-damage destruction effect, the creature is destroyed.

Review: **correct**. Correct; protection does not prevent a nontargeting destroy effect, and the supplied card text says destroy all creatures.
Reviewer: Codex

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality prevents a permanent from being enchanted by Auras that have that quality, and any such Auras already attached are removed to their owners' graveyards as a state-based action [CR 702.16c]. This happens automatically when state-based actions are checked; no player needs to do anything.

Review: **correct**. Correctly states the Aura is put into its owner’s graveyard as a state-based action.
Reviewer: Codex

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes. Hexproof only prevents *opponents* from targeting the creature, so you can freely target your own Slippery Bogle with your own Giant Growth.

**Why:** Hexproof means "This permanent can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you are not your own opponent, the restriction doesn't apply to you. A creature is a legal target for a spell that targets a creature [CR 115.2], and Giant Growth's text simply requires "target creature" [C2].

Review: **correct**. Correct; hexproof restricts opponents, not the creature’s controller.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost. Abrupt Decay still resolves and destroys the target.

**Why:** Ward's ability attempts to counter the spell unless the player pays the cost [CR 702.21a], but Abrupt Decay's text states "This spell can't be countered" [C1]. The official ruling confirms this interaction directly: "Abrupt Decay won't be countered even if you don't" pay the ward cost [C2]. The ward ability triggers and resolves, but its effect fails because the spell is protected from being countered.

Review: **correct**. Correct; explicitly says Ward triggers and its counter effect fails against Abrupt Decay, which still resolves.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will go on the stack where you can use it to redirect Grip to your other artifact.

**Why:** Turning a face-down permanent face up is a special action that doesn't use the stack [CR 702.37e]. Players may take special actions while a spell with split second is on the stack [CR 702.61b], and the Krosan Grip ruling explicitly confirms this [C5]. Willbender's trigger fires when it is turned face up [C13], and triggered abilities are put on the stack as normal during split second [CR 702.61b]. Since Krosan Grip has a single target and your other artifact is a legal target for it, the redirect is valid.

Review: **correct**. Correct; turning face up is a special action and the supplied Willbender ruling supports the redirect.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice to stop Fling from being cast.

**Why:** The sacrifice is part of paying the spell's total cost, which happens during the casting process (the spell is already on the stack at 601.2a, costs are paid at 601.2h, and the spell becomes cast at 601.2i). Players only receive priority once the spell has been fully cast and all costs have been paid, so no one can interfere with the creature you sacrificed to prevent the casting [C3]. The sacrifice is not a separate action that can be responded to—it is an integral part of the casting process [CR 601.2h].

Review: **correct**. Correct; the sacrifice is paid during casting before an opponent receives priority.
Reviewer: Codex

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice goes to exile, and you do not draw a card.

**Why:** When a spell is cast using its flashback cost, it is exiled instead of going anywhere else any time it would leave the stack [CR 702.34a]. This applies whether it resolves, is countered, or leaves the stack for any other reason [C2]. Since it was countered, it never resolved, so its "Draw a card" instruction was never applied.

Review: **correct**. Correct; flashback exiles the spell when it leaves the stack even if countered, and the draw instruction does not resolve.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not apply. The card goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never triggers. The card is put into its owner's graveyard as normal, and you lose the chance to cast it again [C5].

Review: **correct**. Correct; rebound applies as the spell resolves, so a countered spell does not rebound.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. Persist only triggers if the creature had **no** -1/-1 counters on it when it was put into the graveyard from the battlefield. If it has one or more -1/-1 counters at that moment, the condition is not met and persist does not trigger.

**Why:** The ability's text is "When this permanent is put into a graveyard from the battlefield, **if it had no -1/-1 counters on it**, return it to the battlefield under its owner's control with a -1/-1 counter on it" [CR 702.79a]. This is an intervening "if" clause checked both when the ability triggers and again as it resolves [CR 603.4]. The ruling for Kitchen Finks confirms that if the creature has -1/-1 counters on it when it dies, persist won't trigger [C6].

Review: **correct**. Correct; the existing -1/-1 counter prevents persist from triggering.
Reviewer: Codex

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** When a state-based action causes a permanent to leave the battlefield at the same time other state-based actions are performed (such as removing opposite counters), the permanent's last known information is derived from the game state *before* any of those state-based actions were performed [CR 704.8]. In your scenario, before the check, Young Wolf had a +1/+1 counter on it, so the undying condition ("if it had no +1/+1 counters on it") is not met [CR 702.93a]. This is exactly the example given in [CR 704.8]: a Young Wolf with one +1/+1 counter and -1/-1 counters on it dies, and because it had a +1/+1 counter when it was last on the battlefield, undying does not trigger.

Review: **correct**. Correct; last known information before simultaneous state-based actions sees the +1/+1 counter, so undying does not trigger.
Reviewer: Codex

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The returned creature is no longer the target of the Lightning Bolt, so the Bolt will not damage it.

**Why:** Cloudshift's ruling explicitly states that "the returned card won't be the target of any spells or abilities that targeted it before" [C5]. The returned creature is considered a new object with no relation to the one that was exiled [C3]. When the original Bolt tries to resolve, it has no legal target (since the creature it targeted no longer exists as that object), so it won't resolve and no damage is dealt.

Review: **correct**. Correct; Cloudshift returns a new object, so the original Bolt target is illegal and Bolt does not damage it.
Reviewer: Codex

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. Colossus Hammer's equip ability can only be activated as a sorcery, meaning during your main phase when the stack is empty. Since Lightning Bolt is on the stack, you cannot activate the equip ability in response to it.

**Why:** The equip ability's text explicitly states "Equip only as a sorcery" [C2], and the rule defining equip confirms this restriction: "Activate only as a sorcery" [CR 702.6a]. A sorcery-speed activation requires the stack to be empty, which it is not while Lightning Bolt is waiting to resolve.

Review: **correct**. Correct; equip is restricted to sorcery timing and cannot be activated while the Bolt is on the stack.
Reviewer: Codex

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the Crew 1 cost even though it just came under your control and has no haste.

**Why:** The Crew ability's cost is "tap any number of other untapped creatures you control with total power N or greater" [CR 702.122a]. The official ruling for Smuggler's Copter explicitly confirms that "any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12]. This is distinct from attacking or using the creature's own tap abilities, which would be restricted by summoning sickness.

Review: **correct**. Correct; another creature may be tapped to pay crew even if it just came under control.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No, it cannot attack this turn.

**Why:** A creature can't attack unless its controller has controlled it continuously since their most recent turn began, and haste is the ability that overrides this restriction [CR 702.10b]. Since you cast the Copter this turn, you haven't controlled it continuously since your turn began, and it has no haste. Once crewed, it behaves exactly like any other artifact creature for these purposes [C10].

Review: **correct**. Correct; the newly controlled Vehicle cannot attack without haste after becoming a creature.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from assigning combat damage.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends, whichever comes first [CR 509.1g]. Tapping is not a removal-from-combat event, so the creature is still blocking and will assign combat damage to the creature it's blocking in the combat damage step [CR 510.1d].

Review: **correct**. Correct; tapping does not remove a declared blocker or stop it assigning combat damage.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 1 toughness remaining. Double strike has no effect.

**Why:** Fight is a specific action in which each creature deals damage equal to its power to the other [CR 701.14a]. The damage dealt when a creature fights isn't combat damage [CR 701.14d]. Double strike is a static ability that modifies the rules for the combat damage step [CR 702.4a], so it has no bearing on a fight.

Review: **partial**. The substantive outcome is correct, but “1 toughness remaining” is inaccurate terminology: the 4/4 has 3 damage marked and still has toughness 4. Count as an unsupported imprecision.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature reverts to Alice's control.

**Why:** When a player leaves the game, all objects they own leave the game and any effects giving them control of objects end [CR 800.4a]. Since Bob owns Control Magic, it leaves the game along with him, and the creature returns to its owner, Alice. This is exactly the scenario illustrated in the example for that rule: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control" [CR 800.4a].

Review: **correct**. Correct; Bob’s owned Aura leaves with him and the control-changing effect ends, returning control to Alice.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, the Lightning Bolt does not resolve. When Bob leaves the game, the Lightning Bolt card leaves the game entirely and is removed from the stack.

**Why:** Rule 800.4a states that when a player leaves the game, "all objects owned by that player leave the game." Since Bob owns the Lightning Bolt card, it leaves the game and is no longer on the stack, so it cannot resolve. The subsequent clauses about objects ceasing to exist or being exiled apply to objects not represented by cards (like copies or tokens) or objects controlled but not owned by the player who left, neither of which applies here. [CR 800.4a]

Review: **correct**. Correct; Bob’s owned spell leaves the game and cannot resolve.
Reviewer: Codex

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 and 9 add together to 21, and you lose the game.

**Why:** The rule tracks combat damage dealt "by the same commander" over the course of the game — it does not condition the tracking on who controls the commander at the time of each hit [CR 903.10a]. The commander designation is an attribute of the card itself and persists regardless of zone or controller changes [CR 903.3]. So once the total reaches 21, the state-based action causes you to lose [CR 704.6c].

Review: **correct**. Correct; commander damage is tracked by the same commander, not by who controlled it for each hit.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may choose to put your commander into the command zone instead of your hand. This is a replacement effect, not a state-based action.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, the owner may put it into the command zone instead, and identifies this as a replacement effect [CR 903.9b]. The state-based action in rule 903.9a applies only when the commander is already in a graveyard or in exile [CR 903.9a]. Since your scenario involves the commander being returned to your hand (not dying or being exiled), the replacement effect is what applies.

Review: **correct**. Correct; the hand/library option is a replacement effect, distinct from the graveyard/exile state-based action.
Reviewer: Codex

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The two possible totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran). Your opponent will choose 10.

**Why:** When multiple replacement effects modify how much damage a source would deal, the player being dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace doubles that to 10. Applying Furnace first gives 3 × 2 = 6, then Torbran adds 2 for 8. Each replacement effect gets only one opportunity to affect the event [CR 614.5], so there is no further stacking.

Review: **partial**. The chooser and both possible totals are correct, but “Your opponent will choose 10” predicts the opponent’s choice without support. Count as an unsupported claim.
Reviewer: Codex

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library by itself does not cause you to lose the game. You only lose if you *attempt to draw* a card from that empty library.

**Why:** The state-based action that causes a loss specifically requires that a player "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked" [CR 704.5b]. Simply having zero cards in your library is not listed among the state-based actions that cause a player to lose [CR 704.5]. The loss is triggered by the act of attempting the draw, not by the library's state alone [CR 121.4].

Review: **correct**. Correct; merely having an empty library is not a loss condition absent an attempted draw.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** If your attacking creature has trample, you must assign enough damage to the blocking creature(s) to be lethal (taking into account damage already marked on them and damage from other creatures assigned in the same combat damage step). Any damage beyond that can be assigned to your opponent. If your creature does **not** have trample, all of its combat damage must be assigned to the blocking creature(s), and none can be assigned to your opponent.

**Why:** Trample modifies damage assignment so that excess beyond lethal damage to blockers may go through to the defending player [CR 702.19b]. Without trample, a blocked creature assigns all its combat damage to the creatures blocking it [CR 510.1c]. The amount of "lethal damage" depends on the blocker's toughness and any damage already marked on it, so the exact number that gets through varies with those facts.

Review: **partial**. Both conditional outcomes are correct and product-aligned. Strict frozen criterion 1 asks for missing stats/abilities, so it is false under the unchanged rubric.
Reviewer: Codex

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No to both. Your copy does not get the counters on the original creature, and it does not get the bonus from an enchantment attached to it.

**Why:** When copying an object, the copy acquires only the copiable values of the original's characteristics (name, mana cost, color, types, rules text, power, toughness, loyalty, etc.). "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied" [CR 707.2]. An enchantment's bonus is a continuous effect from a separate source, so it falls under "other effects" and is not part of the copiable values.

Review: **incorrect**. The general answer is correct and product-aligned. Both strict frozen criteria ask for specifics rather than a definitive general answer, so they are false under the unchanged rubric.
Reviewer: Codex

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** You (the affected player) choose which replacement effect to apply first. After that effect is applied, the process is repeated with any remaining applicable effects. The final number of tokens depends on what the specific effects do.

**Why:** When two or more replacement effects attempt to modify the same event, the affected player chooses one to apply, following a priority order (self-replacement effects first, then control-modifying, then copy, then back-face, then any remaining) [CR 616.1], [CR 616.1a]–[CR 616.1e]. Once the chosen effect is applied, the process is repeated with any effects that are still applicable to the modified event [CR 616.1f]. If you share the specific card texts, I can walk through the exact outcome.

Review: **correct**. Correctly gives order and re-evaluation, does not invent outcomes, and invites exact card text; citations support the rules.
Reviewer: Codex

Missing reference groups: none

