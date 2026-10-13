# concise-heldout-seed42

Status: **complete** · implementation commit `b26e4ea449f405a8debb43b1d3992d5e34a11bdd`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | pending / n/a/0 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 80.4% |
| Cases retrieving every expected evidence group | 17/32 |
| Answers with citations | 32/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | pending / n/a |
| Reviewed citation-support failures | pending / n/a |
| Reviewed fully correct | 0/0 reviewed |
| Reviewed accuracy | pending / n/a |
| Mean reviewed rubric score | pending / n/a |
| Median successful response | 7.23 s |
| p95 successful response | 11.19 s |
| Median first visible answer token | 5.76 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | pending | 7.77 |
| h02-intervening-if (r1) | 100.0% | pending | 6.09 |
| h03-independent-trigger (r1) | 50.0% | pending | 10.38 |
| h04-replacement-death (r1) | 75.0% | pending | 6.41 |
| h05-simultaneous-death (r1) | 100.0% | pending | 9.81 |
| h06-lifelink-prevented (r1) | 50.0% | pending | 4.88 |
| h07-infect-lifelink (r1) | 100.0% | pending | 7.11 |
| h08-protection-wrath (r1) | 100.0% | pending | 7.42 |
| h09-protection-aura (r1) | 100.0% | pending | 4.43 |
| h10-own-hexproof (r1) | 100.0% | pending | 5.48 |
| h11-ward-uncounterable (r1) | 66.7% | pending | 6.89 |
| h12-split-second (r1) | 100.0% | pending | 11.86 |
| h13-sacrifice-cost (r1) | 66.7% | pending | 9.76 |
| h14-flashback-countered (r1) | 66.7% | pending | 6.07 |
| h15-rebound-countered (r1) | 66.7% | pending | 6.14 |
| h16-persist-counter (r1) | 100.0% | pending | 6.22 |
| h17-undying-simultaneous-sba (r1) | 75.0% | pending | 9.70 |
| h18-blink-target (r1) | 50.0% | pending | 10.05 |
| h19-equip-timing (r1) | 75.0% | pending | 10.38 |
| h20-crew-new-creature (r1) | 66.7% | pending | 7.49 |
| h21-new-vehicle (r1) | 50.0% | pending | 8.87 |
| h22-tapped-blocker (r1) | 0.0% | pending | 10.04 |
| h23-fight-double-strike (r1) | 100.0% | pending | 7.32 |
| h24-leaving-controller (r1) | 100.0% | pending | 9.66 |
| h25-leaving-stack (r1) | 100.0% | pending | 7.12 |
| h26-commander-control (r1) | 100.0% | pending | 6.62 |
| h27-commander-hand (r1) | 100.0% | pending | 7.09 |
| h28-replacement-order (r1) | 80.0% | pending | 10.13 |
| h29-empty-library (r1) | 100.0% | pending | 7.15 |
| h30-ambiguous-combat (r1) | 100.0% | pending | 6.01 |
| h31-ambiguous-copy (r1) | 100.0% | pending | 6.32 |
| h32-ambiguous-replacements (r1) | 100.0% | pending | 11.19 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** They go on the stack in the order Alice, Bob, Charlie (Alice's at the bottom, Charlie's on top), and resolve in the order Charlie, Bob, Alice.

**Why:** In a multiplayer game, the active player puts their triggered abilities on the stack first, then each nonactive player in turn order does the same [CR 805.7]. Since each new object is placed on top of all objects already there [CR 405.2], Charlie's ability ends up on top and resolves first when all players pass in succession [CR 405.5].

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability checks your life total again as it resolves, and if you have 39 or less life at that time, it is removed from the stack and has no effect.

**Why:** Felidar Sovereign's ability uses an "intervening 'if' clause," which means the condition is checked both when the ability triggers and again as it resolves. [CR 603.4] explicitly uses Felidar Sovereign as its example: if the player has 39 or less life when the ability resolves, it does nothing. The card-specific ruling confirms this: "If you don't have 40 or more life at that time, the ability won't do anything." [C2]

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. You may still search for a basic land. The ability resolves normally even though the Simulacrum is no longer on the battlefield.

**Why:** Once a triggered ability is on the stack, it is independent of its source. The "look for the object in the zone it moved to" rule only applies when the ability's effect *attempts to do something to that object* [CR 603.6]. Solemn Simulacrum's ETB ability instructs you to search your library and put a land onto the battlefield—it never references the Simulacrum itself, so the Simulacrum leaving the battlefield has no effect on resolution.

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No. Solemn Simulacrum's "when this creature dies" ability will not trigger.

**Why:** "Dies" is shorthand for "is put into a graveyard from the battlefield." Rest in Peace replaces that event with exile, so the creature is never put into a graveyard and the trigger condition is never met [C1][C2]. This is confirmed by the official ruling: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Missing reference groups: CR 700.4

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **3 times** — once for itself dying and once for each of the two other creatures dying.

**Why:** Blood Artist's trigger condition is "Whenever this creature or another creature dies," so each creature dying is a separate trigger event. Even though Blood Artist is no longer on the battlefield when the other creatures die, leaves-the-battlefield triggers look back in time and still trigger. [C2] explicitly confirms that if Blood Artist and other creatures die at the same time, its ability triggers for each of those creatures, and [CR 603.10a] establishes that such abilities trigger even when the source has already left the battlefield.

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain based on damage *dealt* by the source [CR 702.15b]. Prevented damage is not dealt damage, so if all 3 damage is prevented, no damage is dealt and lifelink triggers no life gain.

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, they gain 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the life-loss result on the damage recipient with poison counters instead [CR 702.90b]. Lifelink causes the source's controller to gain life equal to the damage dealt, in addition to any other results [CR 702.15b]. These two abilities affect different players and different aspects of the damage event, so they apply simultaneously without conflict.

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature. Protection from white does not protect against non-targeting effects.

**Why:** Protection prevents being *targeted* by spells or abilities with the stated quality, but Wrath of God says "Destroy all creatures" without targeting anything [C1]. The five things protection actually prevents are: being targeted, being enchanted by Auras, being equipped by Equipment, damage from sources with that quality, and being blocked by creatures with that quality [CR 702.16b]–[CR 702.16f]. A non-targeting "destroy all" effect falls outside all of those protections, so your creature is destroyed.

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality means the protected permanent can't be enchanted by Auras that have that quality, and any such Auras already attached are removed to their owners' graveyards as a state-based action. [CR 702.16c]

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes. Hexproof only prevents *opponents* from targeting the creature, so you can freely target your own Slippery Bogle with your own Giant Growth.

**Why:** Hexproof on a permanent means "This permanent can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you are not an opponent of yourself, the restriction doesn't apply to your own spells. Giant Growth simply requires "target creature" [C2], and your own creature is a legal target for your own spell.

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No, Ward does not counter Abrupt Decay. Even if you decline to pay the ward cost, Abrupt Decay resolves and destroys the target.

**Why:** Ward's ability says "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but Abrupt Decay's text states "This spell can't be countered" [C1]. The official ruling confirms this interaction directly: "you may still pay the ward cost, but Abrupt Decay won't be countered even if you don't" [C2]. The "can't be countered" clause makes the spell immune to Ward's countering effect regardless of whether you pay.

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will resolve before Grip to redirect it to your other artifact.

**Why:** Turning a face-down permanent face up is a special action that doesn't use the stack, and special actions are explicitly allowed while a split-second spell is on the stack [CR 702.37e] [CR 702.61b]. Willbender's trigger fires on that event [CR 603.2] and is put on the stack above Grip [CR 405.2] [CR 702.61b]. When it resolves, it changes Grip's single target to your other artifact, which is a legal target [CR 115.7b]. This is confirmed by the card-specific ruling that players may turn face-down creatures face up while a split-second spell is on the stack [C5].

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to destroy the creature, because the sacrifice is part of paying costs, which happens before the spell is considered cast and before anyone receives priority to respond.

**Why:** When you cast Fling, the spell is put on the stack first [CR 601.2a], then you pay all costs including the sacrifice [CR 601.2h], and only after those steps are complete does the spell become cast [CR 601.2i]. Players receive priority only after the spell is fully cast, so there is no window in which your opponent can act on the creature you're sacrificing. The official ruling confirms this directly: "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell." [C3]

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice goes to exile, and you do not draw a card.

**Why:** A spell cast using flashback is exiled any time it would leave the stack, whether it resolves, is countered, or leaves the stack some other way [CR 702.34a] [C2]. Since the spell was countered, it never resolved, so its "Draw a card" instruction was never applied [CR 608.1].

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not exile it. The card goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's text says "instead of putting it into your graveyard **as it resolves**, exile it" [CR 702.88a]. If the spell is countered, it never resolves, so rebound never functions. The official ruling confirms: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn." [C5]

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it is put into the graveyard from the battlefield, persist does not trigger and it does not return to the battlefield.

**Why:** Persist's trigger condition is "if it had no -1/-1 counters on it" [CR 702.79a]. The game checks the creature's state just before it leaves the battlefield, and if it has any -1/-1 counters at that moment, the condition fails and the ability does not trigger [C6].

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** When a state-based action causes a permanent to leave the battlefield at the same time other state-based actions (like removing opposing counters) are performed, the permanent's last known information is derived from the game state *before* any of those state-based actions were performed. [CR 704.8] In that prior state, Young Wolf still had a +1/+1 counter on it, so the "if it had no +1/+1 counters on it" condition is not met and undying does not trigger. [CR 702.93a] This is the exact scenario illustrated in the example under [CR 704.8].

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The original Lightning Bolt will do nothing. When Cloudshift resolves, the creature is exiled and then returns as a new object. That new object is not the target of the Bolt, so the Bolt's target is illegal when it tries to resolve and it has no effect.

**Why:** Cloudshift's ruling explicitly states that "the returned card won't be the target of any spells or abilities that targeted it before" [C5]. Since Lightning Bolt's only effect is to deal damage to its target, and that target no longer exists as a legal permanent on the battlefield [CR 115.2], the Bolt resolves with no legal target and does nothing.

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. You cannot activate the equip ability in response to Lightning Bolt, and even if you could, it wouldn't save the creature.

**Why:** Colossus Hammer's equip ability states "Equip only as a sorcery," meaning it can only be activated during your main phase when the stack is empty [C2], [CR 702.6a]. Since Lightning Bolt is on the stack when you'd want to respond, the timing restriction prevents activation. Separately, even if the hammer were already attached, it grants +10/+10 and removes flying [C2]—none of which prevents Lightning Bolt's 3 damage [C1].

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost even though it just came under your control.

**Why:** The crew ability's cost is "tap any number of other untapped creatures you control with total power N or greater" [CR 702.122a]. This is not an activated ability of the creature itself—it's a cost paid to activate the Vehicle's ability. The official ruling for Smuggler's Copter explicitly confirms: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12]. Summoning sickness restricts a creature from attacking or using its own tap abilities, but it does not prevent it from being tapped as a cost for another permanent's ability.

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No. Since you cast it this turn, it hasn't been under your control continuously since the beginning of your turn, and it doesn't have haste to bypass that restriction.

**Why:** Once a Vehicle becomes a creature, it can't attack unless you've controlled it continuously since your turn began [C10]. Haste is the ability that overrides this requirement [CR 702.10b], but Smuggler's Copter doesn't have it [C1]. The crew ability only changes its type; it doesn't grant haste.

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from assigning combat damage.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends, whichever comes first [CR 509.1g]. Tapping is simply a change to the tapped/untapped state; it is not a "remove from combat" effect. During the combat damage step, a blocking creature assigns combat damage equal to its power to the creature(s) it is blocking [CR 510.1a], [CR 510.1d]. There is no requirement that the creature be untapped to assign that damage. To actually prevent the blocker from dealing damage, you would need an effect that removes it from combat, destroys it, or otherwise changes its status (e.g., giving it hexproof won't help here, but "remove from combat" or reducing its power to 0 would).

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 3 damage marked on it.

**Why:** In a fight, each creature deals damage equal to its power to the other [CR 701.14a]. Double strike is a static ability that modifies the combat damage step [CR 702.4a], but fight damage is explicitly not combat damage [CR 701.14d], so double strike has no effect on the fight. The 3/3 (toughness 3) has 4 damage marked on it and dies; the 4/4 (toughness 4) has 3 damage marked on it and survives.

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature remains on the battlefield under Alice's control.

**Why:** When Bob leaves the game, all objects he owns leave the game, and any effects giving him control of objects end [CR 800.4a]. Since Bob owns Control Magic (he cast it), it leaves the game. The creature is owned by Alice, who remains, so it stays on the battlefield and reverts to her control once the control-changing effect ends. This is directly analogous to the example in [CR 800.4a] where Mind Control (an Aura reading "You control enchanted creature") leaves the game when its controller leaves, and the enchanted creature reverts to its owner's control. Note also that gaining control of a creature does not cause you to gain control of Auras attached to it [C2], so the Aura's ownership was never transferred to Alice in the first place.

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, Lightning Bolt does not resolve. It leaves the game entirely.

**Why:** When a player leaves the game, all objects they own leave the game. [CR 800.4a] Lightning Bolt is a card owned by Bob, so it leaves the game the moment Bob does. Since it is no longer on the stack, it cannot resolve and deals no damage to Alice.

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 and 9 add together to 21, and you lose the game.

**Why:** The rule tracks combat damage dealt "by the same commander" over the course of the game — it is the commander card that is the reference point, not the player controlling it. [CR 903.10a] The commander designation is an attribute of the card itself and persists regardless of zone or controller changes. [CR 903.3] This is a state-based action checked whenever state-based actions are evaluated. [CR 704.6c]

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may put your commander into the command zone instead of your hand. This is a replacement effect, not a state-based action.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead, and identifies this as a replacement effect [CR 903.9b]. The state-based action in rule 903.9a applies to a different situation—when the commander is already in a graveyard or exile [CR 903.9a]. Since your commander is being moved to your hand (not to a graveyard or exile), the replacement effect in 903.9b is what applies.

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** The opponent (the player being dealt damage) chooses the order. The possible totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran).

**Why:** When multiple replacement effects modify how much damage a source would deal, the player who would be dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace doubles it to 10. Applying Furnace first gives 3 × 2 = 6, then Torbran adds 2 for 8. Each replacement effect gets one opportunity to affect the event [CR 614.5], so both apply exactly once regardless of order.

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having zero cards in your library does not, by itself, cause you to lose the game. You only lose if you *attempt to draw* a card from an empty library.

**Why:** The loss condition is specifically tied to the act of attempting a draw from an empty library, not to the library being empty. [CR 704.5b] states the player loses if they "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] confirms this is a state-based action triggered by the attempt. None of the listed ways to lose the game ([CR 104.3b], [CR 104.3d]) include simply having an empty library.

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** Your opponent takes the excess damage after you've assigned lethal damage to all blocking creatures.

**Why:** When a creature with trample is blocked, you must first assign lethal damage to each blocking creature (taking into account damage already marked on them and damage from other creatures assigned in the same combat damage step). Any damage beyond that lethal amount can then be assigned to the player or planeswalker you're attacking, as you choose [CR 702.19b]. For example, a 6/6 with trample blocked by a 2/2 must assign at least 2 damage to the blocker, and the remaining 4 can go to the defending player [CR 702.19b]. Note that you must assign lethal damage to *all* blockers before any damage can go through, even if you don't need to kill them all [CR 702.19b].

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No. A copy does not get the counters on the original creature, nor does it get the bonus from an enchantment attached to it.

**Why:** When copying an object, only its copiable values are acquired — the values derived from the text printed on the object (name, mana cost, color, types, rules text, power, toughness, loyalty), as modified by other copy effects and certain "as it enters" abilities. Counters, status, and other effects (including type-changing and text-changing effects like enchantment bonuses) are explicitly not copied. [CR 707.2]

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** You (the affected player) choose the order in which the two replacement effects are applied. Once the first is applied, the second is checked against the modified event and applied if it still applies. The final number of tokens depends on what each effect does.

**Why:** When multiple replacement effects attempt to modify the same event, the affected player chooses which to apply first, then the process repeats with any remaining applicable effects [CR 616.1], [CR 616.1f]. If one effect modifies an event *contained within* the other (e.g., an "enters the battlefield" effect vs. a "creates a token" effect), the outer event's effect must be applied first [CR 616.1g]. For example, if one effect says "create twice as many tokens" and another says "create three tokens instead," applying the doubling first gives 6, while applying the "three instead" first gives 6 as well—but different effect combinations can yield different results, which is why the choice of order matters.

If you share the specific card texts, I can work out the exact result.

Missing reference groups: none

