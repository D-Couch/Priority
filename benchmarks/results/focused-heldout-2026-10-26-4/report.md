# focused-heldout-2026-10-26-4

Status: **complete** · implementation commit `a2be46ded16abba4fd06cadc1d07d995afaf5dd8`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 26/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 78.8% |
| Cases retrieving every expected evidence group | 16/32 |
| Answers with citations | 31/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 3 |
| Reviewed citation-support failures | 4 |
| Reviewed fully correct | 26/32 reviewed |
| Reviewed accuracy | 81.2% |
| Mean reviewed rubric score | 93.8% |
| Median successful response | 7.50 s |
| p95 successful response | 14.51 s |
| Median first visible answer token | 6.07 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 10.85 |
| h02-intervening-if (r1) | 100.0% | correct | 6.47 |
| h03-independent-trigger (r1) | 100.0% | correct | 7.96 |
| h04-replacement-death (r1) | 75.0% | correct | 6.56 |
| h05-simultaneous-death (r1) | 100.0% | correct | 8.26 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 5.24 |
| h07-infect-lifelink (r1) | 100.0% | correct | 7.57 |
| h08-protection-wrath (r1) | 100.0% | correct | 8.46 |
| h09-protection-aura (r1) | 100.0% | correct | 4.80 |
| h10-own-hexproof (r1) | 100.0% | correct | 5.67 |
| h11-ward-uncounterable (r1) | 66.7% | partial | 7.08 |
| h12-split-second (r1) | 100.0% | correct | 9.90 |
| h13-sacrifice-cost (r1) | 66.7% | correct | 8.29 |
| h14-flashback-countered (r1) | 66.7% | correct | 6.35 |
| h15-rebound-countered (r1) | 66.7% | correct | 6.94 |
| h16-persist-counter (r1) | 100.0% | correct | 7.48 |
| h17-undying-simultaneous-sba (r1) | 75.0% | correct | 14.51 |
| h18-blink-target (r1) | 50.0% | correct | 7.27 |
| h19-equip-timing (r1) | 75.0% | partial | 15.27 |
| h20-crew-new-creature (r1) | 66.7% | correct | 9.11 |
| h21-new-vehicle (r1) | 50.0% | correct | 7.02 |
| h22-tapped-blocker (r1) | 0.0% | correct | 9.11 |
| h23-fight-double-strike (r1) | 100.0% | correct | 6.92 |
| h24-leaving-controller (r1) | 100.0% | correct | 7.69 |
| h25-leaving-stack (r1) | 50.0% | partial | 14.32 |
| h26-commander-control (r1) | 100.0% | correct | 7.39 |
| h27-commander-hand (r1) | 100.0% | correct | 6.14 |
| h28-replacement-order (r1) | 80.0% | partial | 10.61 |
| h29-empty-library (r1) | 100.0% | correct | 6.75 |
| h30-ambiguous-combat (r1) | 100.0% | partial | 6.14 |
| h31-ambiguous-copy (r1) | 50.0% | incorrect | 14.01 |
| h32-ambiguous-replacements (r1) | 100.0% | correct | 7.52 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** The stack (bottom to top) is Alice's ability, Bob's ability, Charlie's ability. They resolve in the order Charlie, Bob, Alice.

**Why:** When multiple objects are put on the stack at the same time, those controlled by the active player go on lowest, followed by each other player's objects in APNAP order [CR 405.3]. Since Alice is the active player, her ability is lowest; Bob's is next; Charlie's is on top. The top object resolves first when all players pass [CR 405.5], so Charlie's resolves first, then Bob's, then Alice's.

Review: **correct**. Correctly places triggers in Alice/Bob/Charlie order and resolves in reverse. The supplied stack rules support this sequence.
Reviewer: Codex

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability triggers because you had 40 or more life when your upkeep began, but it checks the condition again as it resolves. Since you now have only 39 life, the ability is removed from the stack and does nothing.

**Why:** This is the "intervening if clause" rule: a triggered ability with an "if" condition checks that condition both when it triggers and again as it resolves, and fails if the condition isn't met at resolution [CR 603.4]. The specific ruling for Felidar Sovereign confirms this two-step check [C2].

Review: **correct**. Correctly says the win does not occur after life drops below 40; CR 603.4 and the card ruling support the recheck.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. Once the ability is on the stack, it exists independently of its source. Destroying the Solemn Simulacrum before the ability resolves does not prevent it from resolving. You will still search your library for a basic land, put it onto the battlefield tapped, and shuffle.

**Why:** A triggered ability that is on the stack is not affected by the destruction or removal of its source [CR 113.7a]. In this case, the ability's effect (searching your library) doesn't even reference the creature, so there's no issue of the ability failing to find its source in a zone [CR 603.6].

Review: **correct**. Correct; directly cites CR 113.7a and correctly explains the optional search at resolution.
Reviewer: Codex

Missing reference groups: none

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No, Solemn Simulacrum's "when this creature dies" ability does not trigger.

**Why:** "Dies" is shorthand for "is put into a graveyard from the battlefield." Rest in Peace's replacement effect causes the card to be exiled instead, so it is never put into a graveyard and the trigger condition is never met [C1]. This is confirmed by the official ruling: "While Rest in Peace is on the battlefield, abilities that trigger whenever a creature dies won't trigger because cards and tokens are never put into a player's graveyard" [C2].

Review: **correct**. Correct; the supplied Rest in Peace ruling directly confirms dies abilities do not trigger when the event is replaced with exile.
Reviewer: Codex

Missing reference groups: CR 700.4

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **3 times** — once for itself dying and once for each of the two other creatures dying.

**Why:** Blood Artist's trigger condition is "whenever this creature or another creature dies," so each individual death event that matches the condition generates a separate trigger. The official ruling confirms that when Blood Artist and other creatures die simultaneously, its ability triggers for each of those creatures [C2]. This is consistent with the general principle that zone-change triggers look back in time and each qualifying event produces its own trigger [CR 603.10a].

Review: **correct**. Correctly counts all three deaths; the supplied Blood Artist ruling directly confirms this.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain only when damage is *dealt* by the source [CR 702.15b]. If all 3 damage is prevented, no damage is dealt, so the condition for lifelink's effect is never met.

Review: **correct**. Correct; prevented damage is not dealt and does not cause lifelink gain.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, they get 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result with giving the player that many poison counters, so the 3 damage does not reduce their life total [CR 702.90b]. Lifelink causes its controller to gain that much life "in addition to any other results that damage causes," so you gain 3 life regardless of the infect replacement [CR 702.15b]. Both effects apply simultaneously to the same damage event.

Review: **correct**. Correctly states infect gives poison counters while lifelink still grants life.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature. Protection from white does not prevent it.

**Why:** Protection prevents being targeted by white spells, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b]–[CR 702.16f]. None of those apply here. Wrath of God is a "destroy all creatures" effect that doesn't target, deal damage, or attach anything [C1]. Protection does not grant indestructibility, so the creature is destroyed.

Review: **correct**. Correct; protection does not prevent the nontargeting destroy effect.
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

**Ruling:** Yes. Hexproof only prevents a permanent from being targeted by spells or abilities your *opponents* control. Since you are casting Giant Growth on your own Slippery Bogle, you are not an opponent of yourself, so hexproof does not apply.

**Why:** Hexproof on a permanent means "This permanent can't be the target of spells or abilities your opponents control" [CR 702.11b]. The restriction is limited to opponents' spells and abilities; it does not restrict the controller from targeting their own permanent with their own spells.

Review: **correct**. Correct; hexproof restricts opponents, not the controller.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost. The spell resolves and destroys the target.

**Why:** Ward's effect says "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but Abrupt Decay has the static ability "This spell can't be countered" [C1]. A spell that can't be countered is not a legal subject of a counter effect, so Ward's counter simply doesn't apply. The official ruling confirms this directly: "Abrupt Decay won't be countered even if you don't" [C2].

Review: **partial**. Correct conclusion and interaction, but it does not explicitly say Ward triggers, which frozen criterion 1 requires.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will resolve to redirect the Grip to your other artifact.

**Why:** Turning a face-down permanent face up is a special action, and special actions are explicitly allowed while a spell with split second is on the stack [CR 702.61b]. The specific ruling for Krosan Grip confirms this [C5]. Willbender's ability triggers when it is turned face up [C13], and triggered abilities are put on the stack as normal under split second [CR 702.61b]. When it resolves, you change the target to another legal target [CR 115.7a], which your second artifact is.

Review: **correct**. Correct; turning face up is a special action and the supplied Willbender ruling supports redirection.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice to prevent Fling from being cast.

**Why:** The spell is put on the stack first, then costs (including the sacrifice) are paid, and only after all steps are complete does the spell become cast and players receive priority [CR 601.2a], [CR 601.2h], [CR 601.2i]. The sacrifice is part of paying costs, not a separate action that opponents can interrupt. The official ruling confirms: "Players can only respond once this spell has been cast and all its costs have been paid. No one can try to interfere with the creature you sacrificed to prevent you from casting this spell" [C3].

Review: **correct**. Correct; costs are paid during casting before opponents receive priority.
Reviewer: Codex

Missing reference groups: CR 117.2e

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** The flashback ability creates a replacement effect that exiles the card instead of putting it anywhere else any time it would leave the stack, including when it's countered [CR 702.34a]. This is confirmed by the card's ruling: "A spell cast using flashback will always be exiled afterward, whether it resolves, is countered, or leaves the stack in some other way" [C2]. Since the spell was countered, it never resolved, so its "Draw a card" effect never happened [CR 608.1].

Review: **correct**. Correct; flashback exiles the spell when it leaves the stack even when countered.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not function. The card goes to your graveyard and you do not get to cast it again on your next turn.

**Why:** Rebound is a static ability that functions while the spell is on the stack and creates a replacement effect that applies "as it resolves" [CR 702.88a]. Since a countered spell never resolves, the replacement effect never triggers. The card simply goes to its owner's graveyard as normal, and no delayed triggered ability is created [C5].

Review: **correct**. Correct; rebound applies as the spell resolves, so a countered spell does not rebound.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. Persist only triggers if the creature had **no** -1/-1 counters on it when it was put into the graveyard from the battlefield. If it has one or more -1/-1 counters at that moment, the condition isn't met and persist won't trigger.

**Why:** The persist ability explicitly checks "if it had no -1/-1 counters on it" as a condition for the return effect [CR 702.79a]. The game looks back in time to the creature's state just before it left the battlefield to determine whether that condition is satisfied [C6]. Since a -1/-1 counter is present, the condition fails and the ability does not trigger.

Review: **correct**. Correct; the existing -1/-1 counter prevents persist from triggering.
Reviewer: Codex

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** Undying is a leaves-the-battlefield ability that looks back in time to check the creature's appearance immediately before it was put into the graveyard [CR 603.10]. At that moment, Young Wolf had a +1/+1 counter on it, so the condition "if it had no +1/+1 counters on it" is not met [CR 702.93a]. The -1/-1 counter and the -1/-1 continuous effect don't cancel or remove the +1/+1 counter; they simply reduce the creature's toughness to 0, causing it to die at the next state-based action check [CR 704.8]. This is the same principle as the supplied example where Young Wolf with one +1/+1 counter and three -1/-1 counters dies and undying does not trigger [CR 704.8].

(Note: counters are not "removed" when a creature dies—they remain on the object in the graveyard but simply have no effect there.)

Review: **correct**. Correct; last known information sees the +1/+1 counter before simultaneous state-based actions.
Reviewer: Codex

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The original Lightning Bolt will not deal damage to the returned creature.

**Why:** Cloudshift's ruling explicitly states that the returned card "won't be the target of any spells or abilities that targeted it before" [C5]. Additionally, the returned creature is considered a new object with no relation to the original [C3]. When the Lightning Bolt resolves, its target is no longer a legal target (the original creature is no longer on the battlefield), so the Bolt has no legal target and its effect does nothing.

Review: **correct**. Correct; Cloudshift returns a new object and the supplied ruling says it is not the old Bolt target.
Reviewer: Codex

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. Colossus Hammer's equip ability can only be activated as a sorcery, which means it can only be activated during your main phase when the stack is empty. Since Lightning Bolt is already on the stack, you cannot activate the equip ability in response to it.

**Why:** The equip ability's text includes the timing restriction "Activate only as a sorcery" [CR 702.6a]. Sorcery-speed actions are only legal during your main phase when the stack is empty. A spell on the stack (like Lightning Bolt) means the stack is not empty, so the equip ability is not legal to activate at that time. Even if you could activate it, the +10/+10 would only help if the creature's toughness without the Equipment is 3 or less (since 3 damage would then be nonlethal), but the timing restriction prevents the activation entirely.

Review: **partial**. The no-response conclusion is correct, but the extra claim that the bonus only helps when the creature’s unequipped toughness is 3 or less is incorrect; the +10 toughness itself makes that conditional statement false for ordinary creature toughness values.
Reviewer: Codex

Missing reference groups: CR 307.5

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost even though it just came under your control and lacks haste.

**Why:** Tapping a creature to pay a crew cost is not the same as activating that creature's own tap ability or having it attack. The ruling for Smuggler's Copter explicitly states that any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control [C12]. The "summoning sickness" restriction (which haste overrides) applies to attacking and to activating a creature's own tap/untap abilities [CR 702.10b], [CR 702.10c], but does not prevent a creature from being tapped as part of another permanent's activated ability cost.

Review: **correct**. Correct; the supplied Smuggler’s Copter ruling directly supports using a newly controlled creature to pay crew.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No, it cannot attack this turn.

**Why:** A creature can't attack unless it has been under its controller's control continuously since their most recent turn began, unless it has haste [CR 702.10b]. Since you cast the Copter this turn, it hasn't met that requirement, and it has no haste to bypass it. Once a Vehicle becomes a creature, it behaves exactly like any other artifact creature for these purposes [C10].

Review: **correct**. Correct; the Vehicle cannot attack without haste after becoming a creature this turn.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from assigning combat damage. It will still deal 3 damage in the combat damage step.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends; tapping is neither of those events [CR 509.1g]. In the combat damage step, each blocking creature assigns combat damage equal to its power [CR 510.1a], and a blocking creature that is still blocking assigns all its combat damage to the creature it's blocking [CR 510.1d]. Only effects that specifically remove a creature from combat (or destroy/exile it, etc.) would stop it from dealing combat damage.

Review: **correct**. The answer gives the correct result and criteria, but provides no citations despite making rules claims; citation support is absent.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 3 damage marked on it.

**Why:** In a fight, each creature deals damage equal to its power to the other [CR 701.14a]. Double strike has no effect here because it modifies the combat damage step [CR 702.4a], and fight damage is explicitly not combat damage [CR 701.14d].

Review: **correct**. Correct and precise: the 4/4 survives with 3 damage marked; double strike does not affect fight damage.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature reverts to Alice's control.

**Why:** When a player leaves the game, all objects they own leave the game, and any effects giving them control of objects end [CR 800.4a]. Since Bob owns the Control Magic, it leaves the game along with him, and the creature returns to its owner, Alice. This is the exact scenario illustrated in the example for [CR 800.4a].

Review: **correct**. Correct; Bob’s owned Aura leaves and its control-changing effect ends.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, the Lightning Bolt does not resolve. When Bob leaves the game, the spell he controls on the stack leaves the game with him. A spell that is no longer on the stack cannot resolve.

**Why:** The supplied excerpts do not include the specific rule governing what happens to objects controlled by a player who leaves the game (this is covered by rule 800.4 in the Comprehensive Rules, which is not among the provided sources). However, the general principle is that a spell must remain on the stack to resolve; once it leaves the game, it is no longer a spell on the stack and has no further effect. The target (Alice) takes no damage.

If you'd like, I can look up the exact rule text for objects leaving the game when their controller does.

Review: **partial**. The conclusion is correct, but CR 800.4a was omitted from packed evidence. The answer itself admits the supplied excerpts lack the controlling rule and gives uncited rules claims; count as unsupported and citation-unsupported.
Reviewer: Codex

Missing reference groups: CR 800.4a

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 and 9 add together to 21, and you lose the game.

**Why:** The commander damage rule tracks damage dealt "by the same commander over the course of the game," not damage dealt by a specific controller [CR 903.10a]. The commander designation is an attribute of the card itself and persists regardless of who controls it [CR 903.3]. Since 21 or more combat damage from the same commander is the threshold, your total of 21 triggers the loss condition as a state-based action [CR 704.6c].

Review: **correct**. Correct; commander damage tracks damage from the same commander across controller changes.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may put your commander into the command zone instead of your hand, and it is a replacement effect.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand from anywhere, the owner may put it into the command zone instead, and it identifies this as a replacement effect [CR 903.9b]. The state-based action in rule 903.9a is a separate mechanism that applies when the commander is already in a graveyard or exile [CR 903.9a].

Review: **correct**. Correct; CR 903.9b directly establishes the command-zone replacement option for a hand destination.
Reviewer: Codex

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The possible totals are **10** (Torbran first, then Furnace) or **8** (Furnace first, then Torbran).

**Why:** When multiple replacement effects modify how much damage a source would deal, the player being dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace doubles that to 10. Applying Furnace first gives 3 × 2 = 6, then Torbran adds 2 for 8. Your opponent will choose the order that results in more damage (10).

Review: **partial**. Correct chooser and both possible totals, but the unsupported claim that the opponent will choose 10 contradicts the expected self-protective choice and is not established by the rules.
Reviewer: Codex

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library is not itself a losing condition. You only lose if you attempt to draw a card from a library that has no cards in it.

**Why:** The state-based action that causes a loss specifically requires that the player *attempted* to draw a card from an empty library since the last time state-based actions were checked [CR 704.5b]. The general rule similarly states that a player who "attempts to draw a card from a library with no cards in it" loses [CR 121.4]. Simply having zero cards in your library, without a draw attempt, does not trigger any loss condition.

Review: **correct**. Correct; an empty library alone is not a loss absent an attempted draw.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** If your attacking creature has trample, you must assign enough damage to the blocking creature(s) to be lethal (taking into account damage already marked on them and damage from other creatures assigned in the same combat damage step). Any damage beyond that lethal amount can be assigned to your opponent as you choose. If your creature does **not** have trample, all of its combat damage is assigned to the blocking creature(s) and none reaches your opponent.

**Why:** Trample modifies damage assignment so that excess beyond lethal damage to blockers may go through to the defending player [CR 702.19b]. Without trample, a blocked creature assigns its combat damage only to the creatures blocking it [CR 510.1c]. "Lethal damage" means damage equal to the blocker's toughness (minus any damage already marked on it), not necessarily damage that will actually kill it if an effect prevents or redirects the damage [CR 702.19b].

Review: **partial**. Both conditional branches are useful and correct, but strict frozen criterion 1 asks for missing stats/abilities; it remains false under the unchanged rubric and is product-aligned.
Reviewer: Codex

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No. A copy of a creature does not get the counters on the original, nor does it get the bonus from an enchantment attached to the original.

**Why:** Copying copies the object's *copiable values*—its inherent characteristics and any changes to those characteristics that are part of the object itself. Counters are not part of an object's characteristics, and continuous effects from other sources (like an Aura granting +1/+1) are not part of the copied object's copiable values either. The supplied excerpts reference "copiable values" throughout (e.g., [CR 707.9b], [CR 707.9d]) but do not include the specific rule that defines the boundary between copiable values and non-copiable things like counters and continuous effects. If you'd like, share the exact card text and I can confirm whether any exception applies.

Review: **incorrect**. The general answer is substantively right and product-aligned, but the packed evidence omitted CR 707.2 and the answer cites only adjacent rules that do not establish the counter/continuous-effect boundary. Both frozen criteria require specifics; citation support fails.
Reviewer: Codex

Missing reference groups: CR 707.2

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** You apply one replacement effect first, then re-evaluate and apply the second to the modified event. The final token count depends on what each effect does and which one you choose to apply first.

**Why:** When multiple replacement effects apply to the same event, the affected player chooses one to apply first (following the priority order in [CR 616.1a]–[CR 616.1e]), and once that effect has been applied, the process is repeated with the remaining applicable effects [CR 616.1f]. The second effect then modifies the already-modified event, so the order can change the final count. If you share the exact text of both effects, I can work out the specific result.

Review: **correct**. Correct; states order and re-evaluation, asks for exact effect text, and gives no hypothetical outcome.
Reviewer: Codex

Missing reference groups: none

