# focused-heldout-2026-10-26-6

Status: **complete** · implementation commit `ede0095c1ceea2f1e9ce845330abb457fd4f33d5`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 28/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 80.6% |
| Cases retrieving every expected evidence group | 19/32 |
| Answers with citations | 32/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 2 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 28/32 reviewed |
| Reviewed accuracy | 87.5% |
| Mean reviewed rubric score | 95.3% |
| Median successful response | 7.65 s |
| p95 successful response | 12.31 s |
| Median first visible answer token | 6.40 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 10.59 |
| h02-intervening-if (r1) | 100.0% | correct | 5.90 |
| h03-independent-trigger (r1) | 100.0% | correct | 7.18 |
| h04-replacement-death (r1) | 75.0% | correct | 5.84 |
| h05-simultaneous-death (r1) | 100.0% | correct | 9.65 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 5.28 |
| h07-infect-lifelink (r1) | 100.0% | correct | 7.49 |
| h08-protection-wrath (r1) | 100.0% | correct | 8.68 |
| h09-protection-aura (r1) | 100.0% | correct | 4.79 |
| h10-own-hexproof (r1) | 100.0% | correct | 5.77 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 7.78 |
| h12-split-second (r1) | 100.0% | correct | 11.00 |
| h13-sacrifice-cost (r1) | 100.0% | correct | 8.53 |
| h14-flashback-countered (r1) | 66.7% | correct | 5.83 |
| h15-rebound-countered (r1) | 66.7% | correct | 6.60 |
| h16-persist-counter (r1) | 100.0% | correct | 11.27 |
| h17-undying-simultaneous-sba (r1) | 100.0% | correct | 15.69 |
| h18-blink-target (r1) | 50.0% | correct | 11.99 |
| h19-equip-timing (r1) | 75.0% | correct | 9.19 |
| h20-crew-new-creature (r1) | 66.7% | correct | 8.84 |
| h21-new-vehicle (r1) | 50.0% | correct | 8.00 |
| h22-tapped-blocker (r1) | 0.0% | correct | 8.35 |
| h23-fight-double-strike (r1) | 100.0% | correct | 7.43 |
| h24-leaving-controller (r1) | 100.0% | correct | 9.12 |
| h25-leaving-stack (r1) | 100.0% | correct | 7.52 |
| h26-commander-control (r1) | 100.0% | correct | 7.26 |
| h27-commander-hand (r1) | 100.0% | correct | 7.31 |
| h28-replacement-order (r1) | 80.0% | partial | 10.49 |
| h29-empty-library (r1) | 100.0% | correct | 7.40 |
| h30-ambiguous-combat (r1) | 100.0% | partial | 7.06 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 6.87 |
| h32-ambiguous-replacements (r1) | 0.0% | partial | 12.31 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** Alice's ability goes on the stack first, then Bob's, then Charlie's. They resolve in reverse order: Charlie's first, then Bob's, then Alice's.

**Why:** In a multiplayer game, the active player puts their triggered abilities on the stack first, then each nonactive player in turn order does the same [CR 805.7]. Each ability is placed on top of the stack as it's added [CR 405.2], so the stack from bottom to top is Alice, Bob, Charlie. The top of the stack resolves first [CR 405.5], meaning Charlie's ability resolves first, then Bob's, then Alice's.

Review: **correct**. Correct order, but CR 805.7 concerns teams in shared-team turns; it does not support this ordinary three-player game. The directly relevant CR 603.3b/101.4 were absent.
Reviewer: Codex

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability checks your life total again as it resolves, and if you have 39 or less life at that time, it does nothing.

**Why:** Felidar Sovereign's ability uses an "intervening 'if' clause," which means the condition is checked both when the ability triggers and again as it resolves [CR 603.4]. The card-specific ruling confirms this: if you don't have 40 or more life when the ability tries to resolve, it won't do anything [C2].

Review: **correct**. Correctly explains the intervening-if check at trigger and resolution, with supplied CR 603.4 and card ruling.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. Once the ability is on the stack, it exists independently of its source, so destroying Solemn Simulacrum does not remove or affect the ability. It will still resolve and you may search for a basic land.

**Why:** A triggered ability, once on the stack, is not dependent on its source remaining on the battlefield [CR 113.7a]. Destruction or removal of the source after the ability has been put on the stack won't affect it [CR 113.7a].

Review: **correct**. Correct: the ability on the stack is independent of its source.
Reviewer: Codex

Missing reference groups: none

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** Rest in Peace's static ability replaces the event of the card being put into a graveyard with exiling it instead [C1]. Since the card is never actually put into a graveyard, the "dies" trigger condition is never met [C2]. The replacement effect means the original event never happens [CR 614.6], so there is no qualifying event for the triggered ability to watch.

Review: **correct**. Correct: Rest in Peace replaces the graveyard move, so the dies ability does not trigger.
Reviewer: Codex

Missing reference groups: CR 700.4

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **3 times** — once for itself dying and once for each of the two other creatures dying.

**Why:** The card text reads "Whenever this creature or another creature dies," so each creature's death is a separate trigger event. The card-specific ruling confirms that when Blood Artist and other creatures die simultaneously, its ability triggers for each of those creatures [C2]. Since three creatures died (Blood Artist + two others), the ability triggers three times.

Review: **correct**. Correctly counts all three deaths, including Blood Artist. The supplied card-specific ruling says the ability triggers for each of those creatures.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain based on damage *dealt* by the source [CR 702.15b]. If a prevention effect stops all 3 damage, that damage is never dealt, so the condition for lifelink's life gain is never met.

Review: **correct**. Correct: prevented damage is not dealt, so lifelink gains no life.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, your opponent gets 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result of damage dealt to a player with giving that player poison counters instead [CR 702.90b]. Lifelink causes the source's controller to gain that much life "in addition to any other results that damage causes" [CR 702.15b]. Both effects apply to the same damage event independently: infect handles what happens to the opponent, and lifelink handles what happens to you.

Review: **correct**. Correctly accounts for infect and lifelink on the same damage event.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature. Protection from white does not prevent it.

**Why:** Protection from white only prevents being targeted by white spells/abilities, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b]–[CR 702.16f]. Wrath of God says "Destroy all creatures" without targeting any specific creature [C1]. Since "destroy" is not one of the things protection prevents, your creature is destroyed along with all others.

Review: **correct**. Correct: Wrath does not target, so protection does not prevent its destruction effect.
Reviewer: Codex

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality means the protected permanent can't be enchanted by Auras that have that quality, and any such Auras already attached are put into their owners' graveyards as a state-based action [CR 702.16c]. Since the Aura is white and the creature now has protection from white, this applies immediately.

Review: **correct**. Correctly says the Aura goes to its owner’s graveyard as a state-based action.
Reviewer: Codex

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes. Hexproof only prevents a permanent from being targeted by spells or abilities your *opponents* control. Since you control both the Slippery Bogle and the Giant Growth, hexproof does not apply to this interaction.

**Why:** Hexproof is defined as "This permanent can't be the target of spells or abilities your opponents control" [CR 702.11b]. You are not an opponent of yourself, so the restriction simply doesn't apply when you target your own creature with your own spell.

Review: **correct**. Correct: hexproof restricts opponents’ spells and abilities, not the controller’s.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward's triggered ability triggers, but its effect cannot counter Abrupt Decay because Abrupt Decay has "This spell can't be countered."

**Why:** Ward {2} means "counter that spell or ability unless that player pays {2}" [CR 702.21a]. When you decline to pay, the counter effect would apply, but Abrupt Decay's "This spell can't be countered" clause makes it impossible to counter [C1]. The official ruling confirms this: "Abrupt Decay won't be countered even if you don't" pay the ward cost [C2]. So the ability triggers, but its effect fails to resolve successfully.

Review: **correct**. Explicitly says Ward triggers and distinguishes that trigger from the counter effect failing against Abrupt Decay.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up, and its triggered ability will redirect Krosan Grip to your other artifact.

**Why:** Turning a face-down permanent face up is a special action, and special actions are permitted while a spell with split second is on the stack [CR 702.61b] [CR 702.37e]. This is confirmed by a Krosan Grip ruling: "Players may turn face-down creatures face up while a spell with split second is on the stack" [C5]. Willbender's triggered ability triggers when it is turned face up [C13], and triggered abilities are put on the stack as normal during split second [CR 702.61b]. Since Willbender's ability goes on the stack above Krosan Grip, it resolves first. Krosan Grip has a single target, making it a valid target for Willbender's "change the target" effect, and you may change it to your other artifact as a legal target [CR 115.7a].

Review: **correct**. Correctly permits the special action and the resulting triggered ability to change Grip’s target.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice. The creature is sacrificed as part of paying Fling's cost during the casting process, and no player receives priority until the spell is fully cast and all costs have been paid.

**Why:** The spell is put on the stack first [CR 601.2a], then costs are paid while it is already on the stack [CR 601.2h], and only after all those steps are complete does the spell become cast [CR 601.2i]. No one gets priority during this process, so there is no window to respond to the sacrifice. The Fling ruling confirms this directly: "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell." [C3]

Review: **correct**. Correct: the sacrifice is paid during casting before opponents receive priority.
Reviewer: Codex

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice goes to exile, and you do not draw a card.

**Why:** A spell cast using flashback is exiled any time it would leave the stack, including when it's countered [CR 702.34a] [C2]. Since the spell was countered, it never resolved, so its "Draw a card" effect never occurred.

Review: **correct**. Correct: a countered flashback spell is exiled and its effect does not resolve.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not exile it. The card goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" — if the spell is countered, it never resolves, so the replacement effect never triggers [CR 702.88a]. The card is put into its owner's graveyard as normal, and no delayed triggered ability is created [C5].

Review: **correct**. Correct: rebound does not apply when the spell does not resolve.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it's put into a graveyard from the battlefield, persist will not return it.

**Why:** Persist's condition is "if it had no -1/-1 counters on it" at the moment it's put into the graveyard [CR 702.79a]. The ability checks the creature's state just before it leaves the battlefield, so any -1/-1 counters present at that moment prevent the return [C6].

Review: **correct**. Correctly identifies the existing -1/-1 counter as blocking persist.
Reviewer: Codex

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** The counter removal (per [CR 704.5q]) and the creature dying from toughness 0 or less are both state-based actions performed simultaneously as a single event [CR 704.3]. Per [CR 704.8], when a state-based action results in a permanent leaving the battlefield at the same time other state-based actions were performed, the permanent's last known information is derived from the game state **before** any of those state-based actions were performed. Before the check, Young Wolf had a +1/+1 counter on it, so the undying condition "if it had no +1/+1 counters on it" is not met [CR 702.93a]. This is the same principle as the worked example in [CR 704.8], where Young Wolf with one +1/+1 counter and three -1/-1 counters dies and undying does not trigger because it had a +1/+1 counter when it was last on the battlefield.

Review: **correct**. Correctly separates simultaneous counter cancellation from the pre-action state used for last known information; cites CR 704.5q and 704.8.
Reviewer: Codex

Missing reference groups: none

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The original Lightning Bolt will not damage the returned creature.

**Why:** Cloudshift's ruling explicitly states that "the returned card won't be the target of any spells or abilities that targeted it before" [C5]. The returned card is considered a new object with no relation to the original [C3]. Since Lightning Bolt's target (the original object) is now in exile and no longer a legal target, the Bolt will fizzle when it tries to resolve.

Review: **correct**. Correct: Cloudshift returns a new object, leaving Lightning Bolt without a legal target.
Reviewer: Codex

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. You cannot activate the equip ability in response to Lightning Bolt.

**Why:** Colossus Hammer's equip ability states "Equip only as a sorcery." Under [CR 307.5], this means the player must have priority, it must be during the main phase of their turn, **and the stack must be empty**. Since Lightning Bolt is on the stack, the stack is not empty, so the equip ability cannot be activated at that time.

Review: **correct**. Correct: equip’s sorcery timing requires an empty stack; CR 307.5 was packed.
Reviewer: Codex

Missing reference groups: CR 702.6a

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost even though it just came under your control and has no haste.

**Why:** Crew is an activated ability of the Vehicle, and the creature is simply tapped as part of the cost to activate it [CR 702.122a]. The restriction on creatures that haven't been under your control since the start of your turn applies to *their own* tap abilities and attacking, not to being tapped as a cost for another object's ability. The official ruling for Smuggler's Copter confirms this explicitly: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12].

Review: **correct**. Correct: crew taps a creature to pay another permanent’s cost, not to activate its own tap ability.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No, it cannot attack this turn.

**Why:** A creature can't attack unless it has been under your control continuously since your most recent turn began, and haste is the ability that overrides this restriction [CR 702.10b]. Since you cast Smuggler's Copter this turn, you haven't controlled it continuously since your turn began, and it has no haste. Once a Vehicle becomes a creature, it behaves exactly like any other artifact creature regarding this restriction [C10].

Review: **correct**. Correct: the Vehicle itself has not been controlled since the turn began and has no haste.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from assigning combat damage.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends, whichever comes first [CR 509.1g]. Tapping is not one of those conditions, so the creature is still blocking and still assigns its combat damage to the creature it's blocking [CR 510.1d].

Review: **correct**. Correct: tapping a declared blocker neither removes it from combat nor stops its combat damage.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 3 damage marked on it.

**Why:** In a fight, each creature deals damage equal to its power to the other [CR 701.14a]. The damage dealt when a creature fights isn't combat damage [CR 701.14d], so double strike—which modifies the combat damage step [CR 702.4a]—has no effect on a fight. The 3/3 has 4 damage marked on it (lethal for a 3-toughness creature), and the 4/4 has 3 damage marked on it (non-lethal for a 4-toughness creature).

Review: **correct**. Correct: fight damage is not combat damage, so double strike adds no second damage event.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature reverts to Alice's control.

**Why:** When a player leaves the game, all objects they own leave the game, and any effects giving them control of objects end [CR 800.4a]. Since Bob owns Control Magic, it leaves the game; since the control-changing effect ends, the creature (owned by Alice) returns to her control. This is the exact scenario described in the example for [CR 800.4a], where the controller of a "You control enchanted creature" Aura leaves the game and the creature reverts to its owner.

Review: **correct**. Correctly applies CR 800.4a to the Aura and the control-changing effect.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, Lightning Bolt does not resolve. It leaves the game entirely.

**Why:** When a player leaves the game, all objects they own leave the game [CR 800.4a]. Lightning Bolt is a card owned by Bob, so it leaves the game as part of this process. Since it is no longer on the stack, it cannot resolve and deals no damage to Alice.

Review: **correct**. Correct: Bob-owned Lightning Bolt leaves the game with him before resolving.
Reviewer: Codex

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes, they add together. The 12 + 9 = 21 combat damage meets the threshold, and you lose the game.

**Why:** Commander damage is tracked per commander (the card), not per controller. The rule states that a player who has been dealt 21 or more combat damage "by the same commander over the course of the game" loses [CR 903.10a]. The commander designation is an attribute of the card itself and persists even when it changes zones or controllers [CR 903.3], so all combat damage that card deals to you accumulates regardless of who controls it at the time.

Review: **correct**. Correct: commander damage is tracked by commander identity across control changes.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may put your commander into the command zone instead of your hand. This is a replacement effect, not a state-based action.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead, and labels this a replacement effect [CR 903.9b]. The state-based action in rule 903.9a applies only when the commander is already in a graveyard or in exile [CR 903.9a]. Since your scenario involves the commander being put into your hand, the replacement effect in 903.9b is what applies.

Review: **correct**. Correctly identifies the hand replacement option and distinguishes it from the graveyard/exile state-based action.
Reviewer: Codex

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The possible totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran).

**Why:** When multiple replacement effects modify how much damage a source would deal, the player being dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace doubles it to 10. Applying Furnace first gives 3 × 2 = 6, then Torbran adds 2 for 8. Your opponent will choose the order that results in more damage to them (10), but the choice is theirs to make.

Review: **partial**. Gives the chooser and both totals correctly, but predicts that the opponent will choose 10. That preference is not established by rules and conflicts with the instruction not to predict the choice.
Reviewer: Codex

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library is not itself a losing condition. You only lose if you *attempt to draw* a card from a library with no cards in it.

**Why:** The state-based action that causes a loss specifically requires that a player "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked" [CR 704.5b]. Similarly, the general rule states that a player who "attempts to draw a card from a library with no cards in it" loses the game the next time a player would receive priority [CR 121.4]. Neither rule imposes a loss merely for having zero cards in the library.

Review: **correct**. Correct: losing requires an attempted draw from an empty library.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** If your attacking creature has trample, you must assign at least lethal damage to the blocking creature(s) first, and any excess damage beyond that can be assigned to your opponent. "Lethal damage" means damage equal to the blocker's toughness minus any damage already marked on it (plus damage from other creatures being assigned in the same combat damage step).

**Why:** Trample modifies damage assignment so that once all blocking creatures have been assigned lethal damage, the controller may assign the remaining damage to the player they're attacking [CR 702.19b]. The amount that "gets through" is your creature's power minus the lethal damage required for the blocker(s). For example, a 4/4 with trample blocked by a 2/2 would deal 2 damage to the blocker and 2 to your opponent. If the blocker already has 1 damage marked on it, only 1 more is needed to be lethal, so 3 would get through.

If your creature does **not** have trample, none of its damage can be assigned to your opponent while it is blocked [CR 510.1c].

Review: **partial**. The conditional ruling is useful and avoids an unconditional total, but frozen criterion 1 specifically asks for the missing attacker/blocker stats and abilities. The answer instead adds an unrequested hypothetical example.
Reviewer: Codex

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No to both. A copy does not get the counters on the original creature, and it does not get the bonus from an enchantment (or any other continuous effect) modifying the original.

**Why:** When copying an object, the copy acquires only the copiable values — the characteristics derived from the text printed on the object, as modified by other copy effects, face-down status, and "as it enters" abilities that set power and toughness. Counters, status, and other continuous effects (including type-changing and text-changing effects) are explicitly excluded from what gets copied [CR 707.2]. Once the copy exists, it is an independent object; changes to the original don't affect it [CR 707.2b].

Review: **incorrect**. Gives a useful general copy rule, but answers “No to both” definitively without inviting the copy effect or card details as the frozen criteria require.
Reviewer: Codex

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** The number of tokens you get depends on the exact wording of each replacement effect. The supplied excerpts confirm that replacement effects modifying token creation apply to the event of creation [CR 614.16], but they don't specify how multiple such effects combine.

**Why:** Replacement effects modify the event they replace [CR 614.1], so the outcome depends on whether each effect says "create an additional token," "create N tokens instead," or something else. The controller of the affected object typically chooses the order in which multiple replacement effects apply, but that ordering rule isn't included in the supplied excerpts.

**Need details:** Please share the exact text of both replacement effects so I can determine the combined result.

Review: **partial**. Requests both replacement-effect texts and gives no token total. It adds an uncited claim about who typically chooses the order, then says that rule is absent from the supplied excerpts.
Reviewer: Codex

Missing reference groups: CR 616.1

