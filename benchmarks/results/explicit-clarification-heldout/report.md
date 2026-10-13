# explicit-clarification-heldout

Status: **complete** · implementation commit `a3e979858814881e7b246812582a65e20fd07351`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 29/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 81.2% |
| Cases retrieving every expected evidence group | 18/32 |
| Answers with citations | 31/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 3 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 29/32 reviewed |
| Reviewed accuracy | 90.6% |
| Mean reviewed rubric score | 93.8% |
| Median successful response | 7.42 s |
| p95 successful response | 14.04 s |
| Median first visible answer token | 6.12 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 10.05 |
| h02-intervening-if (r1) | 100.0% | correct | 5.74 |
| h03-independent-trigger (r1) | 50.0% | correct | 10.45 |
| h04-replacement-death (r1) | 75.0% | correct | 6.41 |
| h05-simultaneous-death (r1) | 100.0% | correct | 6.14 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 6.38 |
| h07-infect-lifelink (r1) | 100.0% | correct | 9.81 |
| h08-protection-wrath (r1) | 100.0% | correct | 8.66 |
| h09-protection-aura (r1) | 100.0% | correct | 5.06 |
| h10-own-hexproof (r1) | 100.0% | correct | 5.88 |
| h11-ward-uncounterable (r1) | 66.7% | correct | 6.30 |
| h12-split-second (r1) | 100.0% | correct | 10.57 |
| h13-sacrifice-cost (r1) | 100.0% | correct | 9.17 |
| h14-flashback-countered (r1) | 66.7% | correct | 6.49 |
| h15-rebound-countered (r1) | 66.7% | correct | 6.65 |
| h16-persist-counter (r1) | 100.0% | correct | 7.09 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 12.14 |
| h18-blink-target (r1) | 75.0% | correct | 7.59 |
| h19-equip-timing (r1) | 75.0% | correct | 14.04 |
| h20-crew-new-creature (r1) | 66.7% | correct | 14.93 |
| h21-new-vehicle (r1) | 50.0% | correct | 7.56 |
| h22-tapped-blocker (r1) | 0.0% | correct | 10.93 |
| h23-fight-double-strike (r1) | 100.0% | correct | 7.67 |
| h24-leaving-controller (r1) | 100.0% | correct | 7.03 |
| h25-leaving-stack (r1) | 100.0% | partial | 8.32 |
| h26-commander-control (r1) | 100.0% | correct | 8.36 |
| h27-commander-hand (r1) | 100.0% | correct | 6.58 |
| h28-replacement-order (r1) | 100.0% | correct | 9.59 |
| h29-empty-library (r1) | 100.0% | correct | 7.28 |
| h30-ambiguous-combat (r1) | 50.0% | incorrect | 4.87 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 5.67 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 5.54 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** The abilities go on the stack in the order Alice, Bob, Charlie (bottom to top), so they resolve in the order Charlie, Bob, Alice.

**Why:** When multiple objects are put on the stack at the same time, the active player's objects are placed lowest, followed by the other players' objects in APNAP order [CR 405.3]. Since Alice is the active player and turn order is Alice → Bob → Charlie, her ability is placed lowest, Bob's above it, and Charlie's on top. The top of the stack resolves first [CR 608.1], so Charlie's ability resolves, then Bob's, then Alice's.

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability is removed from the stack and has no effect.

**Why:** Felidar Sovereign's ability uses an intervening "if" clause, which means the condition is checked both when the ability triggers and again as it resolves. Since you have 39 life when it resolves, the condition is not met and the ability does nothing. [CR 603.4] [C2]

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. The enters-the-battlefield ability resolves normally even though the Simulacrum is no longer on the battlefield.

**Why:** Once a triggered ability is on the stack, it exists independently of its source and retains the text of the ability that created it [CR 603.3] [CR 405.4]. The ETB effect ("you may search your library for a basic land card, put that card onto the battlefield tapped, then shuffle") does not require the Simulacrum to still be on the battlefield, so it resolves as written. Additionally, the Simulacrum's "When this creature dies, you may draw a card" ability would also trigger when it is destroyed.

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** Rest in Peace replaces the event of the card being put into a graveyard with exiling it, so the card is never actually put into a graveyard. Since the trigger condition ("when this creature dies") requires the card to be put into a graveyard, it is never met. [C1] [C2]

Review: **correct**. Correctly says the dies ability does not trigger because Rest in Peace exiles the card instead of putting it into the graveyard; both the rule/card-specific ruling citations support this.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 700.4

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers three times.

**Why:** Blood Artist's trigger condition is "whenever this creature or another creature dies," so it triggers once for itself dying and once for each of the two other creatures dying. The card-specific ruling confirms this: "If Blood Artist and one or more other creatures die at the same time, its ability will trigger for each of those creatures." [C2] This is consistent with the general rule that leaves-the-battlefield abilities look back in time and trigger for each qualifying event, even if the source also leaves the battlefield simultaneously. [CR 603.10a]

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain only when damage is *dealt* by the source [CR 702.15b]. If all 3 damage is prevented, no damage is dealt, so the condition for lifelink is never met.

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, your opponent gets 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result of damage dealt to a player with gaining poison counters [CR 702.90b]. Lifelink causes the source's controller to gain life "in addition to any other results that damage causes" [CR 702.15b]. These operate on different aspects of the same damage event—so both apply simultaneously: the opponent receives poison counters instead of losing life, and you gain life.

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature.

**Why:** Protection from white prevents being targeted by white spells, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b]–[CR 702.16f]. Wrath of God says "Destroy all creatures" without targeting any specific creature [C1]. Since protection does not prevent a permanent from being destroyed by a non-targeting effect, the creature is destroyed.

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality prevents the protected permanent from being enchanted by Auras with that quality. Any such Auras already attached are put into their owners' graveyards as a state-based action [CR 702.16c].

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes, you can target your own Slippery Bogle with your own Giant Growth.

**Why:** Hexproof only prevents *opponents* from targeting the creature with their spells or abilities. [CR 702.11b] Since you control both the Slippery Bogle and the Giant Growth, the hexproof restriction does not apply to you.

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward does not counter Abrupt Decay. Even if you decline to pay the ward cost, Abrupt Decay resolves normally and destroys the creature.

**Why:** Abrupt Decay's text states "This spell can't be countered" [C1]. Ward's ability instructs the player to counter the spell unless they pay the cost [CR 702.21a], but a "can't be countered" clause makes the spell immune to any countering effect, including Ward. The official ruling confirms this: "Abrupt Decay won't be countered even if you don't" pay the ward cost [C2].

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will resolve before Grip, redirecting Grip's target to your other artifact.

**Why:** Turning a face-down permanent face up is a special action, and special actions are permitted while a spell with split second is on the stack [CR 702.37e] [CR 702.61b] [C5]. Willbender's trigger fires when it is turned face up [C13], and triggered abilities are put on the stack as normal under split second [CR 702.61b]. The trigger goes on top of the stack [CR 405.2], so it resolves before Grip and changes Grip's target to your other artifact.

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice. The creature is sacrificed as part of paying Fling's cost, and no player receives priority during the casting process.

**Why:** Costs are paid as part of casting (601.2h), and the spell only becomes cast after all costs are paid (601.2i). No one has priority to respond until the spell is fully cast and on the stack. The Fling ruling confirms this directly: "No one can try to interfere with the creature you sacrificed to prevent you from casting this spell" [C3]. By the time your opponent could act, the creature is already in the graveyard.

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** Because the flashback cost was paid, Think Twice is exiled instead of going to the graveyard any time it would leave the stack, including when it is countered [CR 702.34a] [C2]. Since the spell was countered, it never resolves, so its "Draw a card" instruction is never applied [CR 608.1].

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not function. The card is put into your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never triggers. The card-specific ruling confirms this directly: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn." [C5]

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it dies, persist does not trigger and it does not return to the battlefield.

**Why:** Persist's trigger condition is "if it had no -1/-1 counters on it" [CR 702.79a]. The game checks the creature's state just before it leaves the battlefield, and if it has any -1/-1 counters at that moment, the condition is not met and the ability does not trigger [C6].

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** When state-based actions are performed, the creature's last known information is derived from the game state *before* those actions were performed [CR 704.8]. At that moment, Young Wolf still had a +1/+1 counter on it, so undying's condition ("if it had no +1/+1 counters on it") is not met [CR 702.93a]. This is the same principle as the worked example in [CR 704.8], where a Young Wolf with one +1/+1 counter and three -1/-1 counters dies and undying does not trigger because the +1/+1 counter was present.

Review: **correct**. Correctly applies last-known information to the pre-SBA +1/+1 counter, so undying does not trigger; citations 702.93a, 603.10a, and the exact 704.8 example support it.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The original Lightning Bolt will not damage the returned creature.

**Why:** When Cloudshift resolves, the creature is exiled and then returns to the battlefield as a new object. The original target is no longer in the battlefield zone, making it an illegal target [CR 608.2b]. The returned card is not the target of any spell that targeted it before [C5]. Since all of Lightning Bolt's targets are illegal, it doesn't resolve [CR 608.2b].

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. Colossus Hammer's equip ability can only be activated as a sorcery, meaning during your main phase when the stack is empty. Since Lightning Bolt is on the stack, the stack is not empty, so you cannot activate the equip ability in response.

**Why:** The equip ability explicitly states "Activate only as a sorcery" [C2] [CR 702.6a], which restricts activation to times when you could cast a sorcery—your main phase with an empty stack [CR 117.1a]. A Lightning Bolt on the stack means the stack is not empty, so the timing restriction is not met. Additionally, even if you could equip it, Colossus Hammer grants +10/+10 and removes flying [C2]; it does not prevent damage, so it would not save the creature from Lightning Bolt's 3 damage [C1].

Review: **correct**. Correct ruling and explanation: “only as a sorcery” requires sorcery timing, and the stack is not empty while Bolt is pending. The card ruling also supports this restriction.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap your 3/3 creature to pay the crew 1 cost of Smuggler's Copter even though it was just cast and has no haste.

**Why:** The crew cost requires tapping "any number of other untapped creatures you control with total power N or greater" [CR 702.122a]. A creature that just entered the battlefield is untapped, and summoning sickness only restricts a creature from attacking or activating its *own* tap abilities [CR 702.10c]—it does not prevent it from being tapped to pay a cost for another permanent's ability. This is confirmed by the card-specific ruling: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12].

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No, it cannot attack this turn.

**Why:** A creature can't attack unless it has been controlled by its controller continuously since their most recent turn began, unless it has haste [CR 702.10b]. Since you cast Smuggler's Copter this turn, you haven't controlled it continuously since your turn began, and it has no haste. Once crewed, it behaves exactly like any other artifact creature subject to the same summoning-sickness restriction [C10].

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a blocking creature does not remove it from combat and does not prevent it from assigning combat damage. It will still deal combat damage equal to its power (3 in this case).

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends; tapping is not a form of removal from combat [CR 509.1g]. A blocking creature assigns combat damage equal to its power [CR 510.1a], and the rules for assigning damage only exclude a blocker that is no longer blocking any creatures [CR 510.1d]. Tapping has no bearing on either condition.

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 1 life remaining. Double strike has no effect.

**Why:** A fight instructs each creature to deal damage equal to its power to the other [CR 701.14a]. The damage dealt when a creature fights isn't combat damage [CR 701.14d]. Double strike is a static ability that modifies the rules for the combat damage step [CR 702.4a], so it has no application to a fight.

Review: **correct**. The answer correctly reports that the 4/4 survives with one damage marked; the phrasing is correct and its rule citations support the explanation.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature reverts to Alice's control.

**Why:** When a player leaves the game, all objects owned by that player leave the game, and any effects giving that player control of objects end [CR 800.4a]. Since Bob owns the Control Magic, it leaves the game, and the creature reverts to its owner, Alice. This is the exact scenario illustrated in the example: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control" [CR 800.4a].

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, the Lightning Bolt does not resolve. It leaves the game entirely.

**Why:** When a player leaves the game, all objects owned by that player leave the game [CR 800.4a]. Since Bob owns the Lightning Bolt card, it leaves the game (to his graveyard or wherever "leaving the game" places it for that player), removing it from the stack before it can resolve.

Review: **partial**. Core ruling is correct, but the added parenthetical speculates that the object may go to its owner’s graveyard; CR 800.4a says owned objects leave the game and does not support that destination. This is an unsupported extra claim.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 damage dealt while controlled by Alice and the 9 damage dealt while controlled by Bob add together. Since the total is 21, you lose the game.

**Why:** Rule 903.10a states that a player who has been dealt 21 or more combat damage "by the same commander over the course of the game" loses. The rule tracks damage dealt by the same commander card to you, regardless of who controls it at the time the damage is dealt. The commander designation is an attribute of the card itself and persists across zone changes and controller changes [CR 903.3].

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may put your commander into the command zone instead of your hand. This is a replacement effect, not a state-based action.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead, and labels this a replacement effect [CR 903.9b]. The state-based action in rule 903.9a applies to a different situation—when the commander is already in a graveyard or in exile [CR 903.9a] [CR 704.6d].

Review: **correct**. Correctly identifies the command-zone option as a replacement effect for a move to hand or library, and distinguishes the graveyard/exile SBA in 903.9a.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** The opponent (the player being dealt damage) chooses the order. The possible damage totals are **10** (Torbran first, then Furnace of Rath) or **8** (Furnace of Rath first, then Torbran).

**Why:** When multiple replacement effects modify how damage is dealt, the affected player chooses the order to apply them [CR 616.1] [C4]. Applying Torbran first changes 3 to 5, then Furnace of Rath doubles it to 10; applying Furnace of Rath first changes 3 to 6, then Torbran adds 2 for 8 [C4] [C6].

Review: **correct**. Correctly identifies the affected opponent as chooser and computes Torbran-first as 10 and Furnace-first as 8; CR 616.1 and the supplied rulings support the order and results.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library is not itself a losing condition. You only lose if you *attempt to draw* a card from a library with no cards in it.

**Why:** The state-based action that causes a loss is specifically tied to the act of attempting a draw from an empty library, not to the library being empty in general. [CR 704.5b] states the loss occurs "if a player attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] confirms it is the attempt to draw that triggers the loss.

Review: **correct**. Answer addresses the stated facts and satisfies the scenario rubric; cited rule/card identifiers support its material rules claims.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** Zero. A blocked creature assigns its combat damage to the creature(s) blocking it, not to the player.

**Why:** A blocked creature assigns its combat damage to the creatures blocking it [CR 510.1c]. It does not assign any damage to the player it was attacking.

Review: **incorrect**. Still gives an unconditional zero-damage ruling without asking whether the attacker has trample or for other relevant combat details. Both clarification criteria fail.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 702.19b

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No to both. The copy does not get the counters on the original creature, and it does not get the bonus from the enchantment attached to it.

**Why:** When copying an object, the copy acquires the copiable values of the original's characteristics, but "other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied" [CR 707.2]. An enchantment's bonus is a continuous effect from a separate source, not a copiable value of the creature itself, so it is not transferred to the copy.

Review: **incorrect**. Still gives a definitive answer without identifying the copy effect or the creature/enchantment. Both clarification criteria fail.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details: What are the two replacement effects? (e.g., Doubling Season, "create three instead of one," etc.) The number of tokens depends on what each effect does and how they interact.

Review: **correct**. Appropriately asks which replacement effects apply and avoids inventing a token total; this satisfies both frozen clarification criteria.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

