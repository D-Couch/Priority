# key-priority-heldout

Status: **complete** · implementation commit `14003d067382dde6c6dbf7bc4a56ed2e4888aca6`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 29/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 82.0% |
| Cases retrieving every expected evidence group | 19/32 |
| Answers with citations | 31/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 2 |
| Reviewed citation-support failures | 0 |
| Reviewed fully correct | 29/32 reviewed |
| Reviewed accuracy | 90.6% |
| Mean reviewed rubric score | 92.2% |
| Median successful response | 7.52 s |
| p95 successful response | 15.45 s |
| Median first visible answer token | 6.19 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 11.43 |
| h02-intervening-if (r1) | 100.0% | correct | 5.95 |
| h03-independent-trigger (r1) | 50.0% | correct | 9.94 |
| h04-replacement-death (r1) | 100.0% | correct | 7.09 |
| h05-simultaneous-death (r1) | 100.0% | correct | 6.05 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 5.36 |
| h07-infect-lifelink (r1) | 100.0% | correct | 9.24 |
| h08-protection-wrath (r1) | 100.0% | correct | 7.73 |
| h09-protection-aura (r1) | 100.0% | correct | 4.84 |
| h10-own-hexproof (r1) | 100.0% | correct | 5.22 |
| h11-ward-uncounterable (r1) | 66.7% | partial | 7.90 |
| h12-split-second (r1) | 100.0% | correct | 10.43 |
| h13-sacrifice-cost (r1) | 100.0% | correct | 8.70 |
| h14-flashback-countered (r1) | 66.7% | correct | 6.25 |
| h15-rebound-countered (r1) | 66.7% | correct | 6.81 |
| h16-persist-counter (r1) | 100.0% | correct | 7.24 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 12.37 |
| h18-blink-target (r1) | 75.0% | correct | 7.10 |
| h19-equip-timing (r1) | 75.0% | correct | 18.40 |
| h20-crew-new-creature (r1) | 66.7% | correct | 15.45 |
| h21-new-vehicle (r1) | 50.0% | correct | 6.92 |
| h22-tapped-blocker (r1) | 0.0% | correct | 8.95 |
| h23-fight-double-strike (r1) | 100.0% | correct | 8.09 |
| h24-leaving-controller (r1) | 100.0% | correct | 8.58 |
| h25-leaving-stack (r1) | 100.0% | correct | 7.73 |
| h26-commander-control (r1) | 100.0% | correct | 7.72 |
| h27-commander-hand (r1) | 100.0% | correct | 6.43 |
| h28-replacement-order (r1) | 100.0% | correct | 8.88 |
| h29-empty-library (r1) | 100.0% | correct | 5.81 |
| h30-ambiguous-combat (r1) | 50.0% | incorrect | 5.38 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 7.32 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 4.62 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** The triggered abilities go on the stack in APNAP order (Alice's lowest, then Bob's, then Charlie's on top), and they resolve in reverse: Charlie's first, Bob's second, Alice's last.

**Why:** When a step begins, triggered abilities are put on the stack before the active player receives priority [CR 117.3a]. When multiple objects are put on the stack at the same time, the active player's are put on lowest, followed by each other player's in APNAP order [CR 405.3]. The top of the stack resolves first [CR 608.1], so Charlie's ability resolves first, then Bob's, then Alice's.

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

Ruling: No, you do not win. The ability is removed from the stack and has no effect.

Why: Felidar Sovereign's ability uses an intervening "if" clause, which means the condition (having 40 or more life) is checked both when the ability triggers and again as it resolves. [CR 603.4] Since your life total is 39 when the ability tries to resolve, the condition is not met and the ability does nothing. [C2]

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. The ability is already on the stack and will resolve normally, allowing you to search for a basic land.

**Why:** Once a triggered ability goes on the stack, it exists independently of its source [CR 405.4]. The ability's effect is to search your library and put a land onto the battlefield—it does not attempt to do anything to the Simulacrum itself, so the Simulacrum being destroyed (and moving to the graveyard) has no bearing on resolution [CR 603.6]. The "may" choice is made when the ability resolves [CR 603.5].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** "Dies" means "is put into a graveyard from the battlefield" [CR 700.4]. Rest in Peace replaces that event with exile, so the creature is never put into a graveyard and therefore never dies [C1]. This is confirmed by the card-specific ruling: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

Ruling: Blood Artist's ability triggers three times.

Why: Blood Artist's trigger condition is "whenever this creature or another creature dies," so it triggers once for itself dying and once for each other creature that dies. The card-specific ruling confirms that if Blood Artist and one or more other creatures die at the same time, its ability triggers for each of those creatures [C2]. This works because leaves-the-battlefield triggers look back in time, so the ability triggers even though Blood Artist is no longer on the battlefield when the triggers go on the stack [CR 603.10a].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain only when damage is *dealt* by a source with lifelink [CR 702.15b]. If all 3 damage is prevented, no damage is dealt, so the condition for lifelink's effect is never met.

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, your opponent gets 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result of damage dealt to a player with gaining poison counters instead [CR 702.90b]. Lifelink causes the source's controller to gain life "in addition to any other results that damage causes" [CR 702.15b], so it functions independently of infect. The two abilities modify different aspects of the same damage event: infect changes what happens to the recipient, while lifelink adds a life-gain effect for the source's controller.

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature.

**Why:** Protection from white prevents being targeted by white spells, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b–f]. It does not grant immunity to "destroy all creatures" effects, which don't target. Since your creature lacks indestructible, nothing prevents the destruction [CR 702.12b].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality means the protected permanent can't be enchanted by Auras with that quality, and any such Auras already attached are put into their owners' graveyards as a state-based action [CR 702.16c].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes, you can target your own Slippery Bogle with your own Giant Growth.

**Why:** Hexproof only prevents *opponents* from targeting the creature with their spells or abilities. [CR 702.11b] Since you control both the Bogle and the Giant Growth, hexproof does not restrict you from choosing it as a target.

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

Ruling: No, Ward does not counter Abrupt Decay. Even if you decline to pay the ward cost, Abrupt Decay still resolves and destroys the target.

Why: Abrupt Decay's text states "This spell can't be countered," which is a static ability that makes it immune to any effect that would counter it, including Ward's [CR 702.21a]. The 2024 card-specific ruling confirms this directly: "Abrupt Decay won't be countered even if you don't [pay the ward cost]" [C2].

Review: **partial**. Correctly concludes Abrupt Decay resolves even if Ward is unpaid, but does not state that Ward triggers, as criterion 1 requires.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will resolve before Grip to redirect its target.

**Why:** Turning a face-down permanent face up is a special action, and special actions are permitted while a split-second spell is on the stack [CR 702.37e] [CR 702.61b] [C5]. Willbender's triggered ability goes on the stack above Grip [CR 405.2] and resolves first, changing Grip's target to your other artifact [C2].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice. The creature is sacrificed as part of paying Fling's cost, which happens during the casting process before anyone receives priority.

**Why:** The spell is put on the stack first [CR 601.2a], then costs are paid [CR 601.2h], and only after all those steps complete does the spell become cast and players receive priority [CR 601.2i]. The Fling ruling confirms this directly: "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell." [C3]

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** Because the flashback cost was paid, Think Twice is exiled instead of going to the graveyard any time it would leave the stack, including when it is countered [CR 702.34a] [C2]. Since the spell was countered, it never resolves, so its "Draw a card" instruction is never applied [CR 608.1].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not function. The card is put into your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never triggers. The card-specific ruling confirms this directly: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound. The spell will be put into its owner's graveyard and you won't get to cast it again on your next turn." [C5]

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

Ruling: No. If Kitchen Finks has a -1/-1 counter on it when it dies, persist does not trigger and it does not return to the battlefield.

Why: Persist's trigger condition requires that the permanent "had no -1/-1 counters on it" at the moment it is put into a graveyard from the battlefield [CR 702.79a]. If it has one or more -1/-1 counters on it at that time, the condition is not met and the ability does not trigger [C6].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** Undying is a leaves-the-battlefield ability that checks whether the creature had a +1/+1 counter on it when it was last on the battlefield [CR 702.93a]. Leaves-the-battlefield abilities look back in time to the object's appearance immediately prior to leaving [CR 603.10a]. In your scenario, Young Wolf had one +1/+1 counter on it when it was last on the battlefield, so the condition "if it had no +1/+1 counters on it" is not met. This is the same principle illustrated in the Young Wolf example in [CR 704.8].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. Lightning Bolt will not deal damage to the returned creature.

**Why:** Cloudshift's ruling explicitly states that "the returned card won't be the target of any spells or abilities that targeted it before" [C5]. Since Lightning Bolt's only target is no longer legal when it tries to resolve, it doesn't resolve and deals no damage [CR 608.2b].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 400.7

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. Colossus Hammer's equip ability cannot be activated in response to Lightning Bolt because it carries the timing restriction "Activate only as a sorcery," which limits activation to your main phase when the stack is empty.

**Why:** The equip ability's text explicitly states "Equip only as a sorcery" [C2], confirmed by [CR 702.6a]. A timing restriction of "as a sorcery" means the ability may only be activated when you could cast a sorcery—during your main phase with an empty stack. With Lightning Bolt on the stack, that condition is not met, so the equip ability is not legal to activate.

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost of Smuggler's Copter even though it was just cast and has no haste.

**Why:** The card-specific ruling for Smuggler's Copter explicitly states that "any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control" [C12]. The crew ability is an activated ability of the Vehicle, not the creature, so the creature is simply being tapped as part of another permanent's cost rather than using its own tap ability [CR 702.122a].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No, it cannot attack this turn.

**Why:** Once a Vehicle becomes a creature, it can't attack unless you've controlled it continuously since your turn began [C10]. Since you cast it this turn, you haven't met that requirement, and it has no haste to bypass the restriction [CR 702.10b].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

Ruling: No. Tapping the blocker does not remove it from combat and does not prevent it from dealing combat damage. It remains a blocking creature and will still assign its combat damage to the creature it's blocking.

Why: A creature remains a blocking creature until it is removed from combat or the combat phase ends; tapping is neither of those events [CR 509.1g]. A blocking creature assigns combat damage to the creatures it's blocking [CR 510.1d]. Tapping has no effect on a creature's status as a blocker or its ability to deal combat damage.

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 1 damage on it. Double strike has no effect.

**Why:** Fight damage is not combat damage [CR 701.14d], and double strike is a static ability that modifies only the combat damage step [CR 702.4a]. In a fight, each creature simply deals damage equal to its power to the other [CR 701.14a].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game (it goes to Bob's graveyard), and the creature reverts to Alice's control.

**Why:** When a player leaves the game, all objects they own leave the game, and any effects giving them control of objects end [CR 800.4a]. The example in that rule directly parallels this scenario: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control" [CR 800.4a]. Since Bob owns Control Magic, it leaves the game, its control-changing effect ends, and the creature returns to its owner, Alice.

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, Lightning Bolt does not resolve. It leaves the game entirely.

**Why:** When a player leaves the game, all objects they own leave the game [CR 800.4a]. Since Bob owns the Lightning Bolt card, it leaves the game as part of that process and never gets the chance to resolve. The rule about objects on the stack "ceasing to exist" applies only to objects not represented by cards (e.g., copies, tokens); Lightning Bolt is a card, so it simply leaves the game [CR 800.4a].

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 and 9 add together, totaling 21, and you lose the game.

**Why:** Commander damage is tracked per commander, not per controller. Rule 903.10a states that a player who has been dealt 21 or more combat damage "by the same commander over the course of the game" loses the game [CR 903.10a]. The designation of a card as a commander is an attribute of the card itself and persists regardless of zone or controller [CR 903.3], so all combat damage that card deals to you across the game counts toward the threshold, no matter who controlled it when it dealt the damage.

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

Ruling: Yes, you may put your commander into the command zone instead of your hand. This is a replacement effect, not a state-based action.

Why: Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, the owner may put it into the command zone instead, and labels it a "replacement effect." [CR 903.9b] The state-based action in rule 903.9a applies to a different situation—when the commander is already in a graveyard or exile and was put there since the last state-based action check. [CR 903.9a]

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the affected player) chooses the order. The possible damage totals are **8** or **10**.

**Why:** When multiple replacement effects modify how damage is dealt, the affected player chooses the order [CR 616.1] [C4]. If Torbran's "+2" applies first, the damage becomes 5, then Furnace of Rath doubles it to 10. If Furnace of Rath doubles first, the damage becomes 6, then Torbran adds 2 for a total of 8.

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library by itself does not cause you to lose the game. You only lose if you *attempt to draw* a card from that empty library.

**Why:** The state-based action for losing due to an empty library specifically requires that a player "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked" [CR 704.5b]. Simply having zero cards in your library, without a draw attempt, is not a losing condition.

Review: **correct**. Satisfies the frozen criteria; cited rules or card rulings support the answer.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** Zero damage gets through to your opponent. A blocked creature assigns its combat damage to the creatures blocking it, not to the player.

**Why:** A blocked creature assigns its combat damage to the creatures blocking it [CR 510.1c]. It does not assign damage to the player it was attacking. If all its blockers are removed from combat before damage is assigned, it assigns no combat damage at all [CR 510.1c].

Review: **incorrect**. The question omits whether the attacker has trample and other relevant details. The answer gives an unconditional zero-damage ruling; CR 510.1c does not support that ruling for all blocked attackers.
Reviewer: Codex

Missing reference groups: CR 702.19b

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No. Your copy does not get the counters on the original creature, nor does it get the bonus from the enchantment attached to it.

**Why:** When copying an object, the copy acquires only the copiable values derived from the text printed on the object (as modified by other copy effects and certain "as it enters" abilities). "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied" [CR 707.2]. An enchantment's continuous effect is an "other effect" that modifies the object's characteristics, so it is not part of the copiable values.

Review: **incorrect**. The question does not identify the copy effect or the relevant card text. The answer gives an unconditional ruling instead of asking for details; copy effects can specify exceptions.
Reviewer: Codex

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

Need details: What are the two replacement effects? (e.g., Doubling Season, a "create twice as many" effect, a "create an additional token" effect, etc.) The number of tokens depends on what each effect does.

Review: **correct**. Correctly asks which replacement effects apply and avoids inventing a token total for the underspecified scenario.
Reviewer: Codex

Missing reference groups: none

