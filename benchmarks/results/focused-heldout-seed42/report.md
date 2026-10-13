# focused-heldout-seed42

Status: **complete** · implementation commit `9bd6927e08e72f4dd5eee8de720e79ced44746bf`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 28/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 80.4% |
| Cases retrieving every expected evidence group | 17/32 |
| Answers with citations | 31/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 0 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 28/32 reviewed |
| Reviewed accuracy | 87.5% |
| Mean reviewed rubric score | 90.6% |
| Median successful response | 7.49 s |
| p95 successful response | 11.88 s |
| Median first visible answer token | 5.96 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 11.88 |
| h02-intervening-if (r1) | 100.0% | correct | 6.16 |
| h03-independent-trigger (r1) | 50.0% | correct | 11.26 |
| h04-replacement-death (r1) | 75.0% | correct | 6.31 |
| h05-simultaneous-death (r1) | 100.0% | correct | 9.26 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 5.53 |
| h07-infect-lifelink (r1) | 100.0% | correct | 8.95 |
| h08-protection-wrath (r1) | 100.0% | correct | 7.99 |
| h09-protection-aura (r1) | 100.0% | correct | 4.94 |
| h10-own-hexproof (r1) | 100.0% | correct | 5.46 |
| h11-ward-uncounterable (r1) | 66.7% | partial | 6.22 |
| h12-split-second (r1) | 100.0% | correct | 13.93 |
| h13-sacrifice-cost (r1) | 66.7% | correct | 10.35 |
| h14-flashback-countered (r1) | 66.7% | correct | 5.51 |
| h15-rebound-countered (r1) | 66.7% | correct | 6.40 |
| h16-persist-counter (r1) | 100.0% | correct | 6.66 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 10.67 |
| h18-blink-target (r1) | 50.0% | correct | 10.70 |
| h19-equip-timing (r1) | 75.0% | correct | 10.69 |
| h20-crew-new-creature (r1) | 66.7% | correct | 9.09 |
| h21-new-vehicle (r1) | 50.0% | correct | 8.31 |
| h22-tapped-blocker (r1) | 0.0% | correct | 7.36 |
| h23-fight-double-strike (r1) | 100.0% | correct | 6.82 |
| h24-leaving-controller (r1) | 100.0% | correct | 10.22 |
| h25-leaving-stack (r1) | 100.0% | correct | 6.66 |
| h26-commander-control (r1) | 100.0% | correct | 7.17 |
| h27-commander-hand (r1) | 100.0% | correct | 7.62 |
| h28-replacement-order (r1) | 80.0% | correct | 10.90 |
| h29-empty-library (r1) | 100.0% | correct | 7.33 |
| h30-ambiguous-combat (r1) | 100.0% | partial | 6.30 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 7.14 |
| h32-ambiguous-replacements (r1) | 100.0% | incorrect | 11.82 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** The abilities go on the stack in the order Alice, Bob, Charlie (bottom to top), so they resolve in the order Charlie, Bob, Alice.

**Why:** In a multiplayer game, when multiple triggered abilities are waiting to be put on the stack, the active player puts theirs on first, then each nonactive player in turn order does the same [CR 805.7]. Since each object is placed on top of all objects already on the stack [CR 405.2], the topmost (last-added) ability resolves first [CR 608.1]. All of this happens before the active player receives priority [CR 117.3a].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability checks your life total again as it resolves, and since you have 39 life at that point, it does nothing.

**Why:** Felidar Sovereign's ability uses an "intervening if clause," which means the condition is checked both when the ability triggers and again as it resolves. If the condition isn't met at resolution, the ability is removed from the stack with no effect [CR 603.4]. The card-specific ruling confirms this: "If you do, the ability will check again as it tries to resolve. If you don't have 40 or more life at that time, the ability won't do anything" [C2].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. Once the ability is on the stack, it is an independent object with its own text. Its effect—search your library, put a basic land onto the battlefield tapped, then shuffle—does not reference the Simulacrum, so the Simulacrum being destroyed before resolution has no effect on it.

**Why:** A triggered ability on the stack has the text of the ability that created it and no other characteristics [CR 405.4], and it goes on the stack without any card associated with it [CR 405.1]. The zone-change trigger rule about looking for the object in the zone it moved to [CR 603.6] applies to abilities that attempt to do something *to* the object that changed zones; Solemn Simulacrum's ETB ability performs a player action (search, put onto battlefield, shuffle) that never references the Simulacrum itself, so it resolves normally regardless of the Simulacrum's current location.

Review: **correct**. The conclusion is correct. CR 405.1 and 405.4 describe stack objects but do not directly establish that removing a triggered ability source does not remove the ability; the direct source-removal rule is CR 113.7a.
Reviewer: Codex

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** Rest in Peace replaces the event of a card being put into a graveyard with exiling it, so the card is never actually put into a graveyard [C1]. Since the "dies" trigger condition requires the card to be put into a graveyard, and that event never happens, the ability does not trigger [C2]. This is consistent with the general principle that if an event is replaced, it never happens [CR 614.6].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 700.4

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **3 times** — once for itself dying and once for each of the two other creatures dying.

**Why:** Blood Artist's trigger condition is "Whenever this creature or another creature dies," so it triggers for each creature that dies, including itself. Leaves-the-battlefield triggers look back in time, so the ability triggers even though Blood Artist is no longer on the battlefield when the triggers go on the stack [CR 603.10a]. The card-specific ruling confirms this: "If Blood Artist and one or more other creatures die at the same time, its ability will trigger for each of those creatures" [C2].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain when damage is *dealt* by a source with lifelink [CR 702.15b]. Prevented damage is not dealt damage, so if all 3 damage is prevented, no damage is dealt and lifelink has no effect.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, they get 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result with poison counters, so the opponent does not lose life from that damage [CR 702.90b]. Lifelink causes the source's controller to gain that much life "in addition to any other results that damage causes," so you gain 3 life on top of the infect result [CR 702.15b]. The two abilities operate independently and do not conflict.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature.

**Why:** Protection from white prevents being targeted by white spells, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b]–[CR 702.16f]. None of these apply to a non-targeting "destroy all creatures" effect. Wrath of God simply says "Destroy all creatures" without targeting [C1], so protection offers no defense against it. Indestructible would have prevented the destruction [CR 702.12b], but your creature doesn't have it.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality means the protected permanent can't be enchanted by Auras that have that quality, and any such Auras already attached are removed to their owners' graveyards as a state-based action [CR 702.16c]. This happens automatically the next time state-based actions are checked; no player needs to do anything.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes, you can target your own Slippery Bogle with your own Giant Growth.

**Why:** Hexproof means "This permanent can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you are not an opponent of yourself, hexproof does not prevent you from targeting your own creature with your own spell. Giant Growth simply requires a target creature [C2], and your Slippery Bogle is a legal target for you.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

**Why:** Ward's ability says "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but Abrupt Decay's text states "This spell can't be countered" [C1]. The official ruling confirms this interaction directly: "you may still pay the ward cost, but Abrupt Decay won't be countered even if you don't" [C2]. The "can't be countered" clause overrides Ward's counter effect.

Review: **partial**. Correctly says Abrupt Decay is not countered even when ward is unpaid. The first frozen criterion specifically requires saying Ward triggers; the answer never states that explicitly.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will redirect Grip's target to your other artifact.

**Why:**

Turning a face-down permanent face up is a special action that doesn't use the stack [CR 702.37e], and players may take special actions while a spell with split second is on the stack [CR 702.61b]. Willbender's ability triggers when it is turned face up [C13], and triggered abilities are put on the stack as normal during split second [CR 702.61b]. Since Willbender's ability uses "change the target" language, the new target must be legal for Krosan Grip [CR 115.7a]–[CR 115.7b], and your other artifact qualifies. The triggered ability resolves before Grip (being on top of the stack [CR 405.2]), so Grip then destroys your other artifact instead of the first one.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice to prevent Fling from being cast.

**Why:** The sacrifice is part of paying the total cost, which happens while the spell is already on the stack but before it becomes "cast" [CR 601.2h], [CR 601.2i]. Players only receive priority to respond after the spell has been fully cast and all costs have been paid [C3]. By the time your opponent could act, the creature is already in your graveyard and the spell is already cast. The damage Fling will deal (4, equal to the sacrificed creature's power) is locked in at that point.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** Flashback creates a static ability that says "exile this card instead of putting it anywhere else any time it would leave the stack" [CR 702.34a]. This applies whether the spell resolves, is countered, or leaves the stack for any other reason [C2]. Since the spell was countered, it never resolved, so the "Draw a card" instruction was never applied.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not apply. The card goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never triggers. The official ruling confirms this explicitly: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn." [C5]

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it dies, persist does not trigger and it stays in the graveyard.

**Why:** Persist's trigger condition is "if it had no -1/-1 counters on it" [CR 702.79a]. The game checks the creature's state just before it leaves the battlefield, and if it has any -1/-1 counters at that moment, the condition fails and the ability doesn't trigger [C6].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** When a state-based action causes a permanent to leave the battlefield at the same time other state-based actions are performed (such as removing opposing +1/+1 and −1/−1 counters), the permanent's last known information is derived from the game state *before* any of those state-based actions were performed [CR 704.8]. In your scenario, before state-based actions were checked, Young Wolf had a +1/+1 counter on it, so the condition "if it had no +1/+1 counters on it" is not met and undying does not trigger. This is the exact example given in the rule: a Young Wolf with one +1/+1 counter and additional −1/−1 counters dies, and because it had a +1/+1 counter when last on the battlefield, undying does not trigger [CR 704.8].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The Lightning Bolt will fizzle and deal no damage.

**Why:** Cloudshift exiles the creature and returns it to the battlefield as a new object. The returned card is no longer the target of the Lightning Bolt, so when the Bolt tries to resolve it has no legal target and fizzes [C5]. This is consistent with the general rule that only permanents are legal targets for spells that target creatures [CR 115.2].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. Colossus Hammer's equip ability can only be activated as a sorcery, meaning it requires the stack to be empty during your main phase. Since Lightning Bolt is on the stack, you cannot activate the equip ability in response.

**Why:** The equip ability's text explicitly states "Equip only as a sorcery" [C2], which per the rules means it can only be activated when you could cast a sorcery — your main phase with an empty stack [CR 702.6a]. Additionally, even if you could activate it, the +10/+10 it grants would not prevent Lightning Bolt's 3 damage; damage is not reduced by toughness [C1].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost of Smuggler's Copter, even though it was just cast and has no haste.

**Why:** Crew is an activated ability of the Vehicle, not the creature. The creature is simply being tapped as part of the cost, so the "summoning sickness" restriction (which limits attacking and activating a creature's own tap abilities) doesn't apply here. The official ruling explicitly confirms this: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control." [C12]

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No, it cannot attack this turn.

**Why:** A creature can only attack if it has been under its controller's control continuously since the beginning of their most recent turn, unless it has haste [CR 702.10b]. Since you cast the Copter this turn, it hasn't met that requirement, and it has no haste to bypass it. The ruling for Vehicles confirms this: "It can't attack unless you've controlled it continuously since your turn began" [C10]. It will be able to attack starting next turn (assuming it's still a creature or you crew it again).

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from dealing combat damage. It remains a valid blocking creature and will still assign combat damage in the combat damage step.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends, whichever comes first [CR 509.1g]. Tapping is not a removal-from-combat event, so the creature is still blocking and still assigns combat damage to the creature it's blocking [CR 510.1d].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 3 damage marked on it.

**Why:** In a fight, each creature deals damage equal to its power to the other [CR 701.14a]. Double strike is a static ability that modifies the combat damage step [CR 702.4a], but fight damage is not combat damage [CR 701.14d], so double strike has no effect here. The 3/3 has 4 damage marked on it (exceeding its toughness of 3), so it dies; the 4/4 has 3 damage marked on it (below its toughness of 4), so it survives.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature reverts to Alice's control.

**Why:** When Bob leaves the game, all objects he owns leave the game, and any effects giving him control of objects end [CR 800.4a]. Since Bob owns Control Magic (he cast it), it leaves the game. The creature is owned by Alice, who is still in the game, so it remains on the battlefield and reverts to her control once the control-changing effect ends. This is directly illustrated by the example in [CR 800.4a]: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control." Additionally, gaining control of a creature does not cause you to gain control of Auras attached to it [C2], so the Aura's ownership was never transferred to Bob in the first place.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, the Lightning Bolt does not resolve. It leaves the game entirely.

**Why:** When a player leaves the game, all objects owned by that player leave the game [CR 800.4a]. Since Bob owns the Lightning Bolt card on the stack, it leaves the game as part of this process and is removed from the stack before it can resolve. Neither Alice nor Charlie will take damage from it.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 and 9 add together to 21, and you lose the game.

**Why:** Commander damage is tracked per commander, not per controller. The rule states that a player who has been dealt 21 or more combat damage "by the same commander over the course of the game" loses [CR 903.10a]. The commander designation is an attribute of the card itself and persists regardless of who controls it or what zone it's in [CR 903.3]. So all combat damage that particular commander has dealt to you across the entire game counts toward the threshold, no matter who was controlling it when each instance was dealt.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may put your commander into the command zone instead of your hand. This is a replacement effect, not a state-based action.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead, and identifies this as a replacement effect [CR 903.9b]. The state-based action in rule 903.9a covers a different situation — when the commander is already in a graveyard or in exile and was put there since the last state-based action check [CR 903.9a]. Since your commander is being returned to your hand (not to a graveyard or exile), the replacement effect in 903.9b is what applies.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The possible totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran). Your opponent will choose 10.

**Why:** When multiple replacement effects modify how much damage a source would deal, the player being dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace doubles it to 10. Applying Furnace first gives 3 × 2 = 6, then Torbran adds 2 for 8. Each replacement effect applies only once and does not invoke itself repeatedly [CR 614.5].

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library by itself does not cause you to lose the game. You only lose if you *attempt to draw* a card from a library that has no cards in it.

**Why:** The state-based action that causes a loss is specifically tied to the act of attempting a draw from an empty library, not to the library being empty in general. [CR 704.5b] states the loss occurs "if a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] confirms this is the triggering condition. So if your library is empty but no effect has caused you to draw, you are not in a losing state.

Review: **correct**. The answer addresses the scenario accurately and cites the supplied supporting rules.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** If your attacker has trample, you must assign lethal damage to the blocking creature(s) first, and any remaining damage can be assigned to the defending player. If your attacker does *not* have trample, all of its damage is assigned to the blocker(s) and none gets through.

**Why:** Trample modifies damage assignment so that excess beyond lethal damage to blockers may be assigned to the player being attacked [CR 702.19b]. Without trample, a blocked creature assigns all its combat damage to the creatures blocking it [CR 510.1c]. "Lethal damage" means damage equal to the blocker's toughness (accounting for damage already marked on it and other damage being assigned in the same step) [CR 702.19b].

Review: **partial**. Gives correct conditional outcomes for both trample and no-trample cases. Frozen criterion 1 requires asking for stats/abilities, which conflicts with the updated product preference for a useful conditional answer; counted as product-aligned in the addendum.
Reviewer: Codex

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No to both. Your copy does not get the counters on the original creature, and it does not get the bonus from an enchantment attached to it.

**Why:** When copying an object, the copy acquires only the copiable values derived from the text printed on the object (as modified by other copy effects and certain "as it enters" abilities). Other effects—including type-changing and text-changing effects—along with status, counters, and stickers are explicitly not copied [CR 707.2]. An enchantment's bonus is an "other effect" applied to the original, so it does not transfer to the copy.

Review: **incorrect**. Gives the general copy rule directly and correctly, matching the updated product preference. Both frozen criteria require asking for specifics and reject a definitive general answer; counted as product-aligned in the addendum.
Reviewer: Codex

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** Both replacement effects apply, but you choose the order. The first effect modifies the event, then the second effect is checked against that modified event and applied if still applicable. The exact number of tokens depends on what each effect does.

**Why:** When two or more replacement effects attempt to modify the same event, the affected player chooses one to apply first, then the process repeats with any remaining applicable effects [CR 616.1, CR 616.1f]. For example, if both effects double the number of tokens, you'd get four times the original count (2 × 2). If one doubles and the other adds a counter, you'd get double the tokens with that counter. The specific result depends on the exact wording of each effect.

Review: **incorrect**. States the general rule but adds hypothetical examples despite the exact effects being unspecified. It does not request the starting event details and does not follow the concise answer contract; the frozen criteria are not met.
Reviewer: Codex

Missing reference groups: none

