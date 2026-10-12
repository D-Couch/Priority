# reasoning-off-heldout

Status: **complete** · implementation commit `f3d0bfb7b980ac1c39bbcac3386a1bb85b567b32`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 26/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 81.2% |
| Cases retrieving every expected evidence group | 18/32 |
| Answers with citations | 31/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 6 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 26/32 reviewed |
| Reviewed accuracy | 81.2% |
| Mean reviewed rubric score | 92.2% |
| Median successful response | 4.99 s |
| p95 successful response | 13.36 s |
| Median first visible answer token | 3.86 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 5.68 |
| h02-intervening-if (r1) | 100.0% | correct | 4.82 |
| h03-independent-trigger (r1) | 50.0% | partial | 5.23 |
| h04-replacement-death (r1) | 75.0% | correct | 4.35 |
| h05-simultaneous-death (r1) | 100.0% | correct | 4.43 |
| h06-lifelink-prevented (r1) | 50.0% | partial | 4.62 |
| h07-infect-lifelink (r1) | 100.0% | correct | 4.95 |
| h08-protection-wrath (r1) | 100.0% | correct | 5.05 |
| h09-protection-aura (r1) | 100.0% | correct | 4.46 |
| h10-own-hexproof (r1) | 100.0% | correct | 4.58 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 5.33 |
| h12-split-second (r1) | 100.0% | correct | 5.94 |
| h13-sacrifice-cost (r1) | 100.0% | correct | 4.83 |
| h14-flashback-countered (r1) | 66.7% | correct | 5.08 |
| h15-rebound-countered (r1) | 66.7% | correct | 4.82 |
| h16-persist-counter (r1) | 100.0% | correct | 5.03 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 5.61 |
| h18-blink-target (r1) | 75.0% | correct | 5.71 |
| h19-equip-timing (r1) | 75.0% | correct | 4.89 |
| h20-crew-new-creature (r1) | 66.7% | correct | 13.36 |
| h21-new-vehicle (r1) | 50.0% | correct | 5.04 |
| h22-tapped-blocker (r1) | 0.0% | correct | 4.79 |
| h23-fight-double-strike (r1) | 100.0% | partial | 5.38 |
| h24-leaving-controller (r1) | 100.0% | correct | 5.45 |
| h25-leaving-stack (r1) | 100.0% | correct | 4.95 |
| h26-commander-control (r1) | 100.0% | correct | 4.86 |
| h27-commander-hand (r1) | 100.0% | correct | 5.21 |
| h28-replacement-order (r1) | 100.0% | partial | 13.37 |
| h29-empty-library (r1) | 100.0% | correct | 4.50 |
| h30-ambiguous-combat (r1) | 50.0% | incorrect | 4.75 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 5.25 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 4.62 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

Ruling: The abilities go on the stack in the order Alice, Bob, Charlie (Alice's ability is at the bottom, Charlie's is on top). They resolve in the order Charlie, Bob, Alice (Charlie's ability resolves first, then Bob's, then Alice's).

Why: Triggered abilities are put on the stack when a player would receive priority, which occurs at the beginning of the upkeep step after turn-based actions are dealt with [CR 117.3a] [CR 117.5]. When multiple objects are put on the stack at the same time, those controlled by the active player are put on lowest, followed by each other player’s objects in APNAP order [CR 405.3]. The stack resolves in last-in, first-out order, so the topmost object (Charlie's) resolves first [CR 608.1] [CR 405.5].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win.
Why: The ability checks your life total again as it resolves, and if you have 39 or less life at that time, it is removed from the stack and has no effect [CR 603.4]. This is confirmed by the specific ruling for Felidar Sovereign, which states that if you don't have 40 or more life when the ability tries to resolve, it won't do anything [C2].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

Ruling: Yes, you may still search for a basic land.

Why: The ability is a triggered ability that goes on the stack when the creature enters the battlefield, and it does not require the source to remain on the battlefield to resolve [CR 603.3]. The ability's effect is to search your library, put a basic land onto the battlefield tapped, and shuffle, which is independent of the creature's current location [C1]. The destruction of the creature does not counter or remove the ability from the stack [CR 603.3].

Review: **partial**. Correct conclusion, but CR 603.3 cited here covers putting triggered abilities on the stack and does not establish that the ability exists independently of its source; the answer does not cite the rule that directly supports that claim.
Reviewer: Codex

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

Ruling: No, the ability does not trigger.
Why: Rest in Peace causes cards that would be put into a graveyard to be exiled instead, meaning the creature is never put into a graveyard [C1]. Because the card is not put into a graveyard, abilities that trigger when a creature dies do not trigger [C2].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 614.6

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist triggers three times.
Why: The card's ability triggers whenever it or another creature dies, and "dies" means being put into a graveyard from the battlefield [C1] [CR 700.4]. When multiple creatures die simultaneously, the ability triggers for each of those creatures, including itself [C2].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

Ruling: You gain 0 life.

Why: Lifelink causes life gain only when damage is actually dealt by the source [CR 702.15b]. Since the damage was prevented, no damage was dealt, so the condition for lifelink to trigger is not met.

Review: **partial**. Correct zero-life result, but incorrectly calls lifelink a condition that must trigger; lifelink is a static ability and the rules phrase is damage dealt.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

Ruling: Your opponent gains 3 poison counters and does not lose life. You gain 3 life.

Why: Damage dealt to a player by a source with infect causes that player to gain poison counters rather than lose life [CR 702.90b]. Simultaneously, damage dealt by a source with lifelink causes that source’s controller to gain that much life [CR 702.15b]. These are separate results that both apply to the same damage event [CR 120.3a], [CR 120.3b].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

Ruling: Yes, Wrath of God destroys your creature.

Why: Protection from white prevents the creature from being targeted by white spells, but Wrath of God is a sorcery that destroys all creatures without requiring a target [C1] [CR 702.16b]. Since the creature lacks indestructible, it is not protected from the destruction effect itself [CR 702.12b].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

Ruling: The Aura is put into its owner’s graveyard as a state-based action.

Why: A permanent with protection from white can’t be enchanted by Auras that have the stated quality [CR 702.16c]. Such Auras attached to the permanent with protection are put into their owners’ graveyards as a state-based action [CR 702.16c].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

Ruling: Yes, you can target your own Slippery Bogle with your own Giant Growth.
Why: Hexproof only prevents a permanent from being targeted by spells or abilities your opponents control [CR 702.11b]. Since you control both the Slippery Bogle and the Giant Growth, the hexproof restriction does not apply to your own spell [C1] [C2].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No, Ward does not counter Abrupt Decay.
Why: Abrupt Decay has the static ability "This spell can't be countered," which prevents Ward from countering it even if you decline to pay the Ward cost. The card-specific ruling explicitly states that while you may still pay the Ward cost, Abrupt Decay won't be countered even if you don't [C2]. Ward is a triggered ability that attempts to counter the spell unless the cost is paid, but the "can't be countered" ability overrides this [CR 702.21a].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

Ruling: Yes, you can turn Willbender face up and use its trigger to redirect Krosan Grip.

Why: Turning a face-down permanent face up is a special action that does not use the stack, and players may take special actions while a spell with split second is on the stack [CR 702.37e] [CR 702.61b] [C5]. Willbender’s ability triggers when it is turned face up, and triggered abilities are put on the stack as normal while a spell with split second is on the stack [C13] [CR 702.61b]. Since Willbender’s ability targets a spell with a single target, it can legally target Krosan Grip to change its target to your other artifact [C8] [C11].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

Ruling: No, your opponent cannot respond to destroy the creature to stop you from paying the cost.
Why: The creature is sacrificed as part of paying the total cost, which occurs after the spell is put on the stack and before the spell is considered cast [CR 601.2a], [CR 601.2h]. Players can only respond once the spell has been cast and all its costs have been paid, meaning no one can interfere with the sacrificed creature to prevent the casting [C3].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

Ruling: Think Twice is exiled, and you do not draw a card.
Why: A spell cast using flashback is exiled instead of being put into its owner’s graveyard any time it leaves the stack, including when it is countered [C2] [CR 702.34a]. Because the spell is countered, it does not resolve, so its "Draw a card" instruction is not performed [CR 608.2c].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

Ruling: No, the spell is not exiled and you do not get to cast it next upkeep.
Why: If a spell with rebound is countered or doesn't resolve, none of its effects happen, including the rebound effect, and the spell is put into its owner's graveyard [C5]. Rebound only functions if the spell resolves, at which point it is exiled instead of going to the graveyard [CR 702.88a].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No, persist will not return it to the battlefield.

Why: Persist only triggers if the permanent had no -1/-1 counters on it when it was put into a graveyard from the battlefield [CR 702.79a]. If it has a -1/-1 counter on it at that moment, the condition is not met and the ability does not trigger [C6].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

Ruling: No, Undying does not trigger.

Why: The game checks the permanent's status immediately before it is put into the graveyard to determine if it had any +1/+1 counters. Since the Young Wolf had a +1/+1 counter on it at that moment, the condition for Undying ("if it had no +1/+1 counters on it") is not met. This is explicitly illustrated in the provided rules for a similar scenario involving counters and state-based actions. [CR 704.8]

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

Ruling: No, the original Lightning Bolt will not damage the returned creature.

Why: Cloudshift exiles the creature and returns it to the battlefield, causing it to leave the zone it was in when targeted [C2]. A target that is no longer in the zone it was in when it was targeted is illegal [CR 608.2b]. Because the target is illegal, the Lightning Bolt does not resolve and its effects do not happen [CR 608.2b].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

Ruling: No, you cannot activate Colossus Hammer’s equip ability in response to Lightning Bolt.

Why: The equip ability is an activated ability that can only be activated as a sorcery, meaning it can only be activated during your main phase when the stack is empty [CR 702.6a]. Since Lightning Bolt is on the stack, the stack is not empty, so you cannot activate the equip ability [CR 117.1a].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

Ruling: No, you cannot tap it to pay the crew cost.

Why: The crew ability requires tapping "other" untapped creatures you control [CR 702.122a]. Since the 3/3 creature is the permanent being tapped to pay the cost for itself (or is the same permanent as the Vehicle if it were a Vehicle, but here it is a separate creature), the rule specifically excludes the Vehicle itself from being used to crew itself, but more importantly, the definition of crewing involves tapping creatures to pay the cost [CR 702.122b]. However, the critical restriction is that the creature must be "other" than the Vehicle. Wait, the question is about tapping a *separate* 3/3 creature to crew the Copter. The rule says "Tap any number of **other** untapped creatures you control". The 3/3 creature is "other" than the Smuggler's Copter. Therefore, the "other" requirement is met. The second requirement is that the creature must be untapped. The prompt states you "just cast" it. A creature that has just been cast is untapped unless an effect says otherwise. The third requirement is that it must be a creature you control. The prompt states it is a 3/3 creature you control. The fourth requirement is that the total power must be 1 or greater. 3 is greater than 1. The fifth requirement is that the Vehicle must be a Vehicle. Smuggler's Copter is a Vehicle [C1]. The sixth requirement is that the creature must be able to be tapped. The prompt states it has "no haste". Haste allows a creature to attack or activate tap abilities even if it hasn't been under your control since your turn began. However, tapping a creature to pay a cost is not an activated ability of that creature; it is a cost paid by the controller of the Vehicle's ability. Rule 702.10c states that haste allows a player to activate *its* (the creature's) activated abilities. It does not allow a creature to be tapped to pay costs for *other* permanents' abilities if it is subject to the "summoning sickness" restriction regarding attacking. Does summoning sickness prevent a creature from being tapped to pay a crew cost? Rule 702.122a says "Tap any number of other untapped creatures you control". It does not explicitly say "untapped creatures that can attack". However, standard rules state that a creature that hasn't been under your control since your turn began cannot be tapped to pay a crew cost? Let's check the provided excerpts. [C12] says "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control." This explicitly confirms that a creature that just came under your control (i.e., just cast) can be tapped to pay a crew cost. Therefore, the lack of haste does not prevent it from being tapped for crew, because crew is not an activated ability of the creature itself, but a cost paid by the controller of the Vehicle. The "other" requirement is satisfied because the 3/3 creature is not the Smuggler's Copter.

Ruling: Yes, you can tap it.

Why: The crew ability allows you to tap any number of *other* untapped creatures you control with total power 1 or greater [CR 702.122a]. The 3/3 creature is "other" than the Smuggler's Copter, is untapped, and has sufficient power. The ruling for Smuggler's Copter explicitly states that any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control [C12].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

Ruling: No, it cannot attack this turn.

Why: A Vehicle that becomes a creature behaves exactly like any other artifact creature, meaning it can't attack unless you've controlled it continuously since your turn began [C10]. Since you cast Smuggler's Copter this turn, you have not controlled it continuously since your turn began, and it lacks haste to bypass this restriction [CR 702.10b].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: No, tapping the blocker does not remove it from combat, and it still assigns combat damage.

Why: A creature remains a blocking creature until it is removed from combat or the combat phase ends, regardless of its tapped status [CR 509.1g]. A blocking creature assigns combat damage to the creatures it is blocking, and being tapped does not prevent this assignment [CR 510.1d].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

Ruling: The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 is destroyed, and the 4/4 survives with 1 damage remaining.

Why: When creatures fight, each deals damage equal to its power to the other creature simultaneously [CR 701.14a]. This damage is not combat damage, so double strike does not apply to the interaction [CR 701.14d]. Since the 3/3 takes 4 damage (exceeding its toughness of 3) and the 4/4 takes 3 damage (less than its toughness of 4), only the 3/3 is destroyed.

Review: **partial**. Damage and survival conclusion are correct, but “survives with 1 damage remaining” is inaccurate terminology for a 4/4 with 3 marked damage.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

Ruling: The Control Magic Aura is put into Alice’s graveyard, and the creature remains on the battlefield under Alice’s control.
Why: When Bob leaves the game, all objects he owned leave the game, and any effects giving him control of objects end [CR 800.4a]. Since Bob owned the Control Magic Aura, it leaves the game and is put into his graveyard [CR 800.4a]. The creature, which Alice owns, remains on the battlefield, and because the control-changing effect from the Aura has ended, Alice regains control of it [CR 800.4a].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

Ruling: No, Lightning Bolt does not resolve.

Why: When Bob leaves the game, all objects he controls on the stack that are not represented by cards cease to exist, and any objects still controlled by him are exiled [CR 800.4a]. Since Lightning Bolt is a spell on the stack controlled by Bob, it leaves the stack and is removed from the game before it can resolve [CR 800.4a].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

Ruling: Yes, the damage adds together.
Why: A player loses the game if they have been dealt 21 or more combat damage by the same commander over the course of the game [CR 903.10a]. The rule tracks damage dealt by the specific commander object, not the player controlling it at the time of the damage, so the 12 damage from Alice and 9 damage from Bob total 21 [CR 903.10a].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may choose to put your commander into the command zone instead of your hand, and this is a replacement effect.

Why: Rule 903.9b explicitly states that if a commander would be put into its owner’s hand from anywhere, its owner may put it into the command zone instead, and identifies this as a replacement effect [CR 903.9b]. This is distinct from the state-based action in rule 903.9a, which only applies when a commander is in a graveyard or in exile [CR 903.9a].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

Ruling: The opponent (the player being dealt damage) chooses the order. The possible damage totals are 10 or 12.

Why: When multiple replacement effects modify damage, the affected player chooses the order in which they are applied [CR 616.1]. If Torbran’s effect is applied first, the damage becomes 5 (3 + 2), and then Furnace of Rath doubles it to 10 [C1][C5]. If Furnace of Rath is applied first, the damage becomes 6 (3 × 2), and then Torbran’s effect adds 2 to make 8, but wait—Torbran’s text says "deals that much damage plus 2 instead," which is a replacement effect that modifies the amount. However, the specific ruling for Torbran states that if another effect modifies how much damage your red source would deal, the player chooses the order [C4]. The standard interaction for these two specific cards, as illustrated by the Furnace of Rath ruling example involving Mending Hands (a prevention effect, but the logic of order choice applies to replacement effects modifying the amount), is that the player chooses. Let's re-evaluate the math based on the card texts.
Torbran: "If a red source you control would deal damage... it deals that much damage plus 2 instead."
Furnace: "If a source would deal damage... it deals double that damage... instead."
If Torbran applies first: 3 + 2 = 5. Then Furnace doubles 5 to 10.
If Furnace applies first: 3 * 2 = 6. Then Torbran adds 2 to 6 to make 8? No, Torbran's effect is "deals that much damage plus 2 instead". If the event is "deal 6 damage", Torbran replaces it with "deal 6+2=8 damage".
Wait, let's look at the specific ruling [C4] for Torbran. It says "If another effect modifies how much damage your red source would deal... the player... chooses an order".
Let's check the math again.
Option A (Torbran first): 3 + 2 = 5. Furnace doubles 5 to 10.
Option B (Furnace first): 3 * 2 = 6. Torbran adds 2 to 6 to make 8.
Is there a precedent? The Furnace of Rath ruling [C6] uses Mending Hands (prevention) as an example, but the rule [CR 616.1] applies to replacement effects.
Let's re-read Torbran's text carefully. "deals that much damage plus 2 instead".
If Furnace is applied first, the event is "deal 6 damage". Torbran replaces this with "deal 6+2=8 damage".
If Torbran is applied first, the event is "deal 5 damage". Furnace replaces this with "deal 10 damage".
So the totals are 8 and 10.

Let's double check if I missed a detail.
[C1] Torbran: "deals that much damage plus 2 instead".
[C5] Furnace: "deals double that damage... instead".
[CR 616.1] Affected player chooses order.
If Torbran first: 3+2=5. Furnace doubles 5 to 10.
If Furnace first: 3*2=6. Torbran adds 2 to 6 to make 8.

Why: The player being dealt damage chooses the order of the replacement effects [CR 616.1]. If Torbran’s effect is applied first, the damage becomes 5 (3 + 2), and then Furnace of Rath doubles it to 10 [C1][C5]. If Furnace of Rath is applied first, the damage becomes 6 (3 × 2), and then Torbran’s effect adds 2 to make 8 [C1][C5].

Review: **partial**. The direct ruling says totals are 10 or 12, which is wrong; later text gives 10 or 8, then self-corrects repeatedly. Criterion 2 fails and the answer contains contradictory totals.
Reviewer: Codex

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

Ruling: No, you do not lose the game merely for having an empty library.

Why: A player loses the game only if they attempted to draw a card from a library with no cards in it since the last time state-based actions were checked [CR 704.5b]. Having zero cards in your library is not itself a state-based action that causes a loss [CR 704.5].

Review: **correct**. The material ruling addresses the scenario and its cited rule/card text supports the substantive claims.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

Ruling: Zero damage gets through to your opponent.

Why: A blocked creature assigns its combat damage to the creatures blocking it, not to the player it is attacking [CR 510.1c]. Consequently, no combat damage is assigned to the opponent in this scenario [CR 510.1c].

Review: **incorrect**. Gives unconditional zero damage without asking about trample or other relevant abilities. Both clarification criteria fail.
Reviewer: Codex

Missing reference groups: CR 702.19b

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

Ruling: No, your copy does not get the counters or the bonus from the enchantment.

Why: When copying an object, the copy acquires only the copiable values derived from the text printed on the object, as modified by other copy effects, face-down status, and specific "as it enters" abilities that set characteristics [CR 707.2]. Counters, status, and other effects (such as those from enchantments) are explicitly not copied [CR 707.2].

Review: **incorrect**. Gives a definitive answer without asking which copy effect or what characteristics/effects are involved. Both clarification criteria fail.
Reviewer: Codex

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details:
1. What are the specific texts of the two replacement effects?
2. Do either of the effects modify the number of tokens created (e.g., "create twice as many") or do they modify other aspects of the token creation (e.g., "create a token with +1/+1 counters instead")?
3. Are both effects attempting to replace the same event (the creation of the token), or is one applying to a sub-event?

Review: **correct**. Appropriately asks what effects apply and avoids inventing a result.
Reviewer: Codex

Missing reference groups: none

