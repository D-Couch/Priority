# citation-contract-heldout-seed42

Status: **complete** · implementation commit `6ab8b65cb3c26a8697ddcea0c62f75ff144c3dfe`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 26/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 81.4% |
| Cases retrieving every expected evidence group | 18/32 |
| Answers with citations | 32/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 3 |
| Reviewed citation-support failures | 4 |
| Reviewed fully correct | 26/32 reviewed |
| Reviewed accuracy | 81.2% |
| Mean reviewed rubric score | 92.2% |
| Median successful response | 7.93 s |
| p95 successful response | 12.17 s |
| Median first visible answer token | 6.11 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 9.34 |
| h02-intervening-if (r1) | 100.0% | correct | 6.27 |
| h03-independent-trigger (r1) | 50.0% | correct | 10.85 |
| h04-replacement-death (r1) | 75.0% | correct | 6.56 |
| h05-simultaneous-death (r1) | 100.0% | correct | 6.58 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 4.84 |
| h07-infect-lifelink (r1) | 100.0% | correct | 7.29 |
| h08-protection-wrath (r1) | 100.0% | partial | 9.59 |
| h09-protection-aura (r1) | 100.0% | correct | 5.29 |
| h10-own-hexproof (r1) | 100.0% | correct | 5.60 |
| h11-ward-uncounterable (r1) | 66.7% | partial | 6.81 |
| h12-split-second (r1) | 100.0% | correct | 13.38 |
| h13-sacrifice-cost (r1) | 100.0% | correct | 7.78 |
| h14-flashback-countered (r1) | 66.7% | correct | 5.84 |
| h15-rebound-countered (r1) | 66.7% | correct | 6.45 |
| h16-persist-counter (r1) | 100.0% | correct | 6.29 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 10.64 |
| h18-blink-target (r1) | 50.0% | correct | 12.17 |
| h19-equip-timing (r1) | 75.0% | correct | 11.88 |
| h20-crew-new-creature (r1) | 66.7% | correct | 10.13 |
| h21-new-vehicle (r1) | 50.0% | correct | 8.35 |
| h22-tapped-blocker (r1) | 0.0% | correct | 8.13 |
| h23-fight-double-strike (r1) | 100.0% | partial | 7.87 |
| h24-leaving-controller (r1) | 100.0% | correct | 8.53 |
| h25-leaving-stack (r1) | 100.0% | correct | 9.05 |
| h26-commander-control (r1) | 100.0% | correct | 6.44 |
| h27-commander-hand (r1) | 100.0% | correct | 7.71 |
| h28-replacement-order (r1) | 80.0% | correct | 10.82 |
| h29-empty-library (r1) | 100.0% | correct | 7.98 |
| h30-ambiguous-combat (r1) | 100.0% | partial | 6.32 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 9.62 |
| h32-ambiguous-replacements (r1) | 100.0% | partial | 10.74 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** The abilities go on the stack in the order Alice, Bob, Charlie (bottom to top), so they resolve in the order Charlie, Bob, Alice.

**Why:** When multiple triggered abilities are waiting to be put on the stack, the active player's abilities go on first, then each nonactive player's in turn order. [CR 805.7] Since Alice is the active player, her ability is placed first (bottom of the stack), then Bob's, then Charlie's (top of the stack). The top of the stack resolves first when all players pass. [CR 405.5] [CR 608.1]

Review: **correct**. Correct order and resolution sequence. This run cites the specific APNAP multiplayer placement rule CR 805.7 and stack order rule CR 608.1.
Reviewer: Codex

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability checks your life total again as it resolves, and since you have only 39 life at that point, it does nothing.

**Why:** Felidar Sovereign's ability uses an "intervening 'if' clause," which means the condition is checked both when the ability triggers and again as it resolves. If the condition isn't met at resolution, the ability is removed from the stack and has no effect. [CR 603.4] This is confirmed by the card's specific ruling: "If you don't have 40 or more life at that time, the ability won't do anything." [C2]

Review: **correct**. Correctly explains the intervening-if check at trigger and resolution and applies the supplied card ruling.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. Once the enters-the-battlefield ability is on the stack, it resolves independently of the Simulacrum. The effect ("search your library for a basic land card, put it onto the battlefield tapped, then shuffle") doesn't reference the Simulacrum at resolution, so it works even if the Simulacrum is already in the graveyard.

**Why:** A triggered ability goes on the stack as an object that's not a card and has the text of the ability that created it [CR 603.3]. The zone-change rule about looking for the object in the zone it moved to [CR 603.6] only applies when the ability attempts to do something *to* the object that changed zones—here, the ability searches your library, not the Simulacrum. The "may" is an optional effect whose choice is made when the ability resolves [CR 603.5].

Note: the Simulacrum's "when this creature dies" ability will also trigger, so you'll have both abilities on the stack and can choose their order [CR 603.3b].

Review: **correct**. Conclusion is correct. The cited CR 603.3/603.6 passages explain putting triggered abilities on the stack and zone-change triggers, but do not directly establish that removing the source does not remove the ability; CR 113.7a would be the direct citation.
Reviewer: Codex

Missing reference groups: CR 113.7a

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No. Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** "Dies" is shorthand for "is put into a graveyard from the battlefield." Rest in Peace replaces that event with exiling, so the creature is never put into a graveyard and the trigger condition is never met [C2]. This follows from the general principle that a replaced event never happens [CR 614.6].

Review: **correct**. Correct: “dies” requires a battlefield-to-graveyard move, which Rest in Peace replaces with exile. Oracle text and ruling support the application.
Reviewer: Codex

Missing reference groups: CR 700.4

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **three** times — once for each creature that dies (itself and the two tokens).

**Why:** Blood Artist's trigger condition is "whenever this creature or another creature dies," so each individual death event satisfies the condition independently. The official ruling confirms this: "If Blood Artist and one or more other creatures die at the same time, its ability will trigger for each of those creatures." [C2] This is consistent with the general principle that zone-change triggers look back in time and trigger for each qualifying event, even if the triggering source itself also leaves the battlefield. [CR 603.10a]

Review: **correct**. Correctly counts Blood Artist itself and both other creatures; the card ruling and last-known-information rule support the result.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain based on damage *dealt* by the source [CR 702.15b]. If all of the damage is prevented, no damage is dealt, so the condition for lifelink's life gain is never met.

Review: **correct**. Correct: prevented damage is not dealt, so lifelink grants no life.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, your opponent gains 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result with "get that many poison counters" [CR 702.90b], so no life is lost. Lifelink independently causes the source's controller to gain that much life "in addition to any other results that damage causes" [CR 702.15b], so both effects apply simultaneously. The two abilities don't conflict — infect changes what happens to the *recipient*, while lifelink changes what happens to the *controller*.

Review: **correct**. Correctly distinguishes infect’s result for the damaged player from lifelink’s life gain for the source controller.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature. Protection from white does not protect against it.

**Why:** Protection from white prevents the creature from being *targeted* by white spells, but Wrath of God says "Destroy all creatures" without targeting anything [C1]. Protection's relevant clauses cover targeting, enchanting, equipping, damage prevention, and blocking [CR 702.16b]–[CR 702.16f], none of which apply to a non-targeting "destroy all" effect. Only indestructible would prevent the destruction itself [CR 702.12b], which your creature lacks.

Review: **partial**. Correctly rules that protection does not stop Wrath. The extra absolute claim that indestructible is the only way to prevent destruction is overbroad; CR 702.12b establishes indestructible, not that it is the only possible effect.
Reviewer: Codex

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality means the protected permanent can't be enchanted by Auras that have that quality, and any such Auras already attached are put into their owners' graveyards as a state-based action [CR 702.16c]. The Aura doesn't need to be "removed" by an effect—the state-based action handles it automatically the next time state-based actions are checked.

Review: **correct**. Correctly applies protection’s Aura state-based action.
Reviewer: Codex

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes. Hexproof only prevents *opponents* from targeting the creature, so you can freely target your own Slippery Bogle with your own Giant Growth.

**Why:** Hexproof means "This permanent can't be the target of spells or abilities **your opponents** control" [CR 702.11b]. Since you are not your own opponent, the restriction doesn't apply to you. Giant Growth simply requires "target creature" [C2], and your own creature is a legal target for your own spell.

Review: **correct**. Correct: hexproof restricts opponents, not the creature’s controller.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost.

**Why:** Ward's ability says "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but Abrupt Decay's text states "This spell can't be countered" [C1]. A "can't" clause overrides the ward's counter effect, so the spell remains uncountered regardless of whether you pay. The official ruling confirms this directly: "you may still pay the ward cost, but Abrupt Decay won't be countered even if you don't" [C2].

Review: **partial**. The conclusion is correct, including that nonpayment does not counter Abrupt Decay. The first frozen criterion also requires explicitly saying Ward triggers; the answer never states that.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will redirect the Grip to your other artifact.

**Why:** Turning a face-down permanent face up is a special action, not an activated ability, so split second does not prevent it [CR 702.37e] [CR 702.61b]. Willbender's "when turned face up" ability is a triggered ability, and triggered abilities trigger and are put on the stack as normal while split second is on the stack [CR 702.61b] [CR 117.2a]. When it resolves, it uses the "change the target" process, so the new target must be a legal target for Krosan Grip (an artifact or enchantment) [CR 115.7a]. Since your other artifact is a legal target, the redirect succeeds. This is confirmed by the specific ruling: "Players may turn face-down creatures face up while a spell with split second is on the stack" [C5].

Review: **correct**. Correct: turning a face-down creature face up is permitted during split second, and Willbender’s trigger resolves above the spell.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice. The creature is sacrificed as part of paying Fling's additional cost, and no player receives priority during the casting process.

**Why:** The spell is placed on the stack first, then costs (including the sacrifice) are paid, and only after all steps are complete does the spell become "cast" [CR 601.2a], [CR 601.2h], [CR 601.2i]. No player has priority at any point during this sequence, so no one can interrupt it [CR 117.2e]. The card-specific ruling confirms this directly: "No one can try to interfere with the creature you sacrificed to prevent you from casting this spell" [C3].

Review: **correct**. Correct: the sacrifice is paid as a casting cost before opponents receive priority; the Fling ruling directly supports this.
Reviewer: Codex

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** Flashback creates a static ability that says "exile this card instead of putting it anywhere else any time it would leave the stack" [CR 702.34a]. This applies whether the spell resolves, is countered, or leaves the stack for any other reason [C2]. Since the spell was countered, it never resolved, so the "Draw a card" instruction was never carried out.

Review: **correct**. Correct: flashback exiles the spell as it leaves the stack even when countered; a countered spell does not draw a card.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not trigger. The card goes to your graveyard and you do not get to cast it again next upkeep.

**Why:** Rebound's replacement effect only applies "as it resolves" [CR 702.88a]. A countered spell never resolves, so the replacement effect never applies and the card goes to the graveyard as normal. The official ruling confirms this explicitly: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound" [C5].

Review: **correct**. Correct: rebound applies as the spell resolves; the supplied ruling confirms that a countered spell goes to the graveyard without rebound.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it is put into the graveyard from the battlefield, persist does not trigger and it does not return to the battlefield.

**Why:** Persist's trigger condition is "if it had no -1/-1 counters on it" [CR 702.79a]. The game checks the creature's state just before it leaves the battlefield, and if it has any -1/-1 counters at that moment, the condition fails and the ability does not trigger [C6].

Review: **correct**. Correctly applies persist’s no-minus-counter condition using the state just before death.
Reviewer: Codex

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** When a state-based action causes a permanent to leave the battlefield at the same time other state-based actions are performed (such as removing opposing counters), the permanent's last known information is derived from the game state *before* any of those state-based actions were performed. [CR 704.8] In your scenario, before state-based actions are checked, Young Wolf has a +1/+1 counter on it, so undying's condition ("if it had no +1/+1 counters on it") is not met. [CR 702.93a] This is the exact example given in the rule: a Young Wolf with one +1/+1 counter that receives enough -1/-1 counters to die will not trigger undying because it had a +1/+1 counter when it was last on the battlefield. [CR 704.8]

Review: **correct**. Correctly uses the pre-state-based-action game state for last-known information; undying sees the +1/+1 counter.
Reviewer: Codex

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The returned creature is not damaged by the original Lightning Bolt.

**Why:** When Cloudshift resolves, the creature is exiled and then returns as a new object with no relation to the original [C3]. The returned card is not the target of any spell that targeted it before [C5]. So when the Lightning Bolt resolves, its target (the old object) is no longer on the battlefield, and the new creature was never targeted by the Bolt. The Bolt resolves but deals no damage to the returned creature.

Review: **correct**. Correct: Cloudshift returns a new object, leaving Lightning Bolt with no legal target.
Reviewer: Codex

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. Colossus Hammer's equip ability can only be activated as a sorcery, meaning it requires the stack to be empty. Since Lightning Bolt is on the stack, you cannot activate the equip ability in response.

**Why:** The equip ability's text explicitly states "Equip only as a sorcery," which is a timing restriction limiting activation to your main phase when the stack is empty. [C2] [CR 702.6a] When your opponent casts Lightning Bolt, it goes on the stack, so the stack is no longer empty and the equip ability is not legally activatable at that moment. Even though it's your main phase, the "as a sorcery" restriction is not satisfied while a spell is on the stack.

Review: **correct**. Correct: equip’s sorcery timing cannot be used while Lightning Bolt is on the stack.
Reviewer: Codex

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost even though it was just cast and has no haste.

**Why:** While the general rule is that a creature without haste can't be tapped to pay an activated ability's cost that includes the tap symbol unless it's been under your control since the beginning of your turn [CR 702.10c], crew is an explicit exception. The official ruling for Smuggler's Copter states: "Any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control." [C12]

Review: **correct**. Correct. The direct Smuggler’s Copter ruling says any untapped creature may be tapped to crew, including one just controlled; CR 702.10c supports the tap-symbol contrast.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No. Smuggler's Copter cannot attack the turn it's cast, even after being crewed.

**Why:** Once a Vehicle becomes a creature, it's subject to the same summoning sickness rule as any other creature — it can't attack unless you've controlled it continuously since your turn began [C10]. Haste is the ability that overrides this restriction [CR 702.10b], and Smuggler's Copter doesn't have it. Since you cast it this turn, you haven't controlled it since the beginning of your turn, so it can't attack.

Review: **correct**. Correct: the newly cast Vehicle cannot attack after becoming a creature without haste; the supplied Vehicle ruling and haste rule support it.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from dealing combat damage. It remains a valid blocker and will still assign combat damage in the combat damage step.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends, whichever comes first [CR 509.1g]. Tapping is not "removal from combat"—only effects that specifically say "remove from combat" do that. In the combat damage step, a blocking creature assigns combat damage to the creatures it's blocking as long as it is still blocking [CR 510.1d]. Since tapping doesn't change its blocking status, it deals damage normally.

Review: **correct**. Correct: tapping a declared blocker does not remove it from combat or stop it dealing damage.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 1 toughness remaining.

**Why:** When creatures fight, each deals damage equal to its power to the other [CR 701.14a]. That damage is explicitly not combat damage [CR 701.14d]. Double strike is a static ability that modifies the combat damage step [CR 702.4a], so it has no effect on a fight interaction. The 3/3's double strike is irrelevant here—both creatures simply deal their power as damage simultaneously.

Review: **partial**. The fight/double-strike ruling is correct, but “with 1 toughness remaining” is technically inaccurate: toughness is still 4 and 3 damage is marked. Report the marked damage instead.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature reverts to Alice's control.

**Why:** When a player leaves the game, all objects they own leave the game and any effects giving them control of objects end [CR 800.4a]. Since Bob owns Control Magic (he cast it), it leaves the game along with him, and the creature returns to its owner, Alice. This is exactly the scenario illustrated in the rule's example: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control" [CR 800.4a]. Note that Bob never gained control of the Aura itself—gaining control of a creature doesn't cause you to gain control of attached Auras [C2].

Review: **correct**. Correctly applies CR 800.4a: Bob’s Aura leaves, the control effect ends, and Alice’s creature remains under Alice’s control.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, Lightning Bolt does not resolve. It leaves the game entirely.

**Why:** When a player leaves the game, all objects they own leave the game. Since Bob owns the Lightning Bolt card on the stack, it leaves the game as part of the process of Bob leaving — it never gets the chance to resolve. [CR 800.4a]

Review: **correct**. Correctly says the Lightning Bolt leaves the game and does not resolve; it no longer incorrectly assigns a graveyard destination.
Reviewer: Codex

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 and 9 add together to 21, and you lose the game.

**Why:** The rule tracks combat damage dealt "by the same commander" over the course of the game — it does not matter who controlled the commander when the damage was dealt. [CR 903.10a] The controller is irrelevant to the tally; only the identity of the commander and the total combat damage it dealt to you matter.

Review: **correct**. Correct: commander damage tracks the same commander across controllers, reaching 21.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may put your commander into the command zone instead of your hand. This is a replacement effect, not a state-based action.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand or library from anywhere, its owner may put it into the command zone instead, and it identifies this as a replacement effect [CR 903.9b]. The state-based action in rule 903.9a applies to a different situation—when a commander is already in a graveyard or exile [CR 903.9a]. Since your scenario involves the commander being returned to your hand (not already in a graveyard or exile), the replacement effect in 903.9b is what applies.

Review: **correct**. Correctly distinguishes the owner’s optional replacement effect for a move to hand from the graveyard/exile state-based action.
Reviewer: Codex

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The two possible totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran). They will choose 8.

**Why:** When multiple replacement effects modify how much damage a source would deal, the player being dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace doubles it to 10. Applying Furnace first gives 3 × 2 = 6, then Torbran adds 2 for 8. Each replacement effect gets only one opportunity to affect the event [CR 614.5], so neither loops.

Review: **correct**. Correctly gives both legal orders and totals; the affected player chooses and will choose 8 damage.
Reviewer: Codex

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library by itself is not a loss condition. You only lose if you *attempt to draw* a card from a library that has no cards in it, and that attempt is not replaced.

**Why:** The state-based action that causes a loss is specifically triggered by an attempted draw from an empty library, not by the library being empty. [CR 704.5b] states the player loses if they "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked," and [CR 121.4] confirms this is the condition. None of the listed ways to lose the game ([CR 104.3b], [CR 104.3d]) include simply having zero cards in your library. So as long as no effect forces or offers you to draw, you can continue playing with an empty library.

Review: **correct**. Correct: an empty library alone does not lose the game; the relevant state-based action follows an attempted draw.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** You must assign lethal damage to the blocking creature first; any excess beyond that goes through to your opponent.

**Why:** Trample modifies damage assignment so that once all blocking creatures have been assigned lethal damage (damage equal to their toughness, accounting for damage already marked on them and damage from other creatures in the same combat damage step), the remaining damage may be assigned to the defending player as you choose [CR 702.19b]. For example, a 5/5 with trample blocked by a 2/2 deals 2 to the blocker and 3 to the player. If multiple creatures block, you can split the excess among them and the player, but you can't assign any to the player until each blocker has received lethal damage [CR 702.19b].

Review: **partial**. This answer assumes trample even though the question does not say the attacker has it. CR 702.19b supports the trample branch only. A direct general answer should state both the trample and no-trample outcomes or briefly identify the missing ability.
Reviewer: Codex

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No to both. Your copy does not get the counters on the original creature, and it does not get the bonus from the enchantment attached to it.

**Why:** When copying an object, only its copiable values are acquired—those derived from the text printed on the object (name, mana cost, color, types, rules text, power, toughness, loyalty), as modified by other copy effects and certain "as it enters" abilities. "Other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied." [CR 707.2] An enchantment's bonus is a continuous effect from another source, and counters are explicitly excluded, so neither transfers to the copy. For example, if a creature is a 5/5 due to a +1/+1 enchantment and has two +1/+1 counters on it, a Clone that copies it will only have the creature's printed (or characteristic-defining) power and toughness, not the enchantment's bonus or the counters. [CR 707.2]

Review: **incorrect**. The general copy rule is correct and matches the user’s updated preference for direct general answers. The frozen criteria require asking for details and prohibit a definitive answer; retain their grades and record the mismatch in the addendum.
Reviewer: Codex

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** Both replacement effects apply, in the order you (as the affected player) choose. The second effect applies to the modified event produced by the first.

**Why:** When two or more replacement effects attempt to modify the same event, the affected player chooses which to apply first, then the process repeats with any remaining applicable effects [CR 616.1], [CR 616.1f]. So if, for example, one effect says "create twice as many tokens" and another says "create twice as many tokens," you'd get four times the original number (2 × 2), not just two. The exact total depends on what each effect does to the event.

If you share the specific card texts, I can walk through the exact result.

Review: **partial**. The general process and examples are useful and correctly avoid an exact total. It asks for card text at the end but not the starting number required by the old frozen criterion; the answer is aligned with the user’s preference to answer generally first.
Reviewer: Codex

Missing reference groups: none

