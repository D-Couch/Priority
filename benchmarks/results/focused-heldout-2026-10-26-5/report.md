# focused-heldout-2026-10-26-5

Status: **complete** · implementation commit `355b3487afbb597b105185bafea0c7cc76de6ee8`

Suite `heldout-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 32/32 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 26/32 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 80.6% |
| Cases retrieving every expected evidence group | 19/32 |
| Answers with citations | 32/32 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 4 |
| Reviewed citation-support failures | 3 |
| Reviewed fully correct | 26/32 reviewed |
| Reviewed accuracy | 81.2% |
| Mean reviewed rubric score | 90.6% |
| Median successful response | 7.47 s |
| p95 successful response | 10.62 s |
| Median first visible answer token | 6.27 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| h01-apnap (r1) | 33.3% | correct | 9.12 |
| h02-intervening-if (r1) | 100.0% | correct | 6.37 |
| h03-independent-trigger (r1) | 100.0% | correct | 8.24 |
| h04-replacement-death (r1) | 75.0% | correct | 6.64 |
| h05-simultaneous-death (r1) | 100.0% | incorrect | 6.97 |
| h06-lifelink-prevented (r1) | 50.0% | correct | 5.66 |
| h07-infect-lifelink (r1) | 100.0% | correct | 7.79 |
| h08-protection-wrath (r1) | 100.0% | correct | 7.66 |
| h09-protection-aura (r1) | 100.0% | correct | 4.85 |
| h10-own-hexproof (r1) | 100.0% | correct | 5.63 |
| h11-ward-uncounterable (r1) | 66.7% | partial | 7.26 |
| h12-split-second (r1) | 100.0% | correct | 10.62 |
| h13-sacrifice-cost (r1) | 100.0% | correct | 7.93 |
| h14-flashback-countered (r1) | 66.7% | correct | 6.16 |
| h15-rebound-countered (r1) | 66.7% | correct | 6.84 |
| h16-persist-counter (r1) | 100.0% | correct | 6.97 |
| h17-undying-simultaneous-sba (r1) | 75.0% | partial | 14.43 |
| h18-blink-target (r1) | 50.0% | correct | 7.21 |
| h19-equip-timing (r1) | 100.0% | correct | 9.94 |
| h20-crew-new-creature (r1) | 66.7% | correct | 9.15 |
| h21-new-vehicle (r1) | 50.0% | correct | 7.29 |
| h22-tapped-blocker (r1) | 0.0% | correct | 9.16 |
| h23-fight-double-strike (r1) | 100.0% | correct | 6.88 |
| h24-leaving-controller (r1) | 100.0% | correct | 8.29 |
| h25-leaving-stack (r1) | 100.0% | correct | 9.30 |
| h26-commander-control (r1) | 100.0% | correct | 7.72 |
| h27-commander-hand (r1) | 100.0% | correct | 6.34 |
| h28-replacement-order (r1) | 80.0% | partial | 9.67 |
| h29-empty-library (r1) | 100.0% | correct | 6.31 |
| h30-ambiguous-combat (r1) | 100.0% | partial | 6.60 |
| h31-ambiguous-copy (r1) | 100.0% | incorrect | 8.89 |
| h32-ambiguous-replacements (r1) | 0.0% | correct | 9.84 |

## Answers and review notes

### h01-apnap / repetition 1

In a three-player game, turn order is Alice, Bob, Charlie. It is Alice’s upkeep. Each controls exactly one ability that triggers at the beginning of that upkeep, with no other triggers. In what order do they go on the stack and resolve if nobody responds?

**Ruling:** Alice's ability goes on the stack first (bottom), then Bob's, then Charlie's (top). They resolve in reverse order: Charlie's first, then Bob's, then Alice's.

**Why:** Triggered abilities that trigger at the beginning of upkeep are put on the stack before the active player receives priority [CR 503.1a]. The active player puts their triggered abilities on the stack first, then each nonactive player in turn order does the same [CR 805.7]. Since the stack resolves last-in, first-out [CR 405.5], Charlie's ability (placed last) resolves first, followed by Bob's, then Alice's.

Review: **correct**. Outcome order is right, but CR 805.7 is the team-game rule and does not support ordinary three-player APNAP; CR 603.3b/101.4 were absent from packed evidence.
Reviewer: Codex

Missing reference groups: CR 603.3b, CR 101.4

### h02-intervening-if / repetition 1

I control Felidar Sovereign and begin my upkeep at 40 life. Its ability triggers, then I drop to 39 life before it resolves. Do I win from that ability?

**Ruling:** No, you do not win. The ability triggers because you had 40 or more life when your upkeep began, but it checks the condition again as it resolves. Since you now have only 39 life, the ability is removed from the stack and does nothing.

**Why:** This is the "intervening if clause" rule: a triggered ability with an "if" condition checks that condition both when it triggers and again as it resolves, and fails if the condition isn't met at resolution [CR 603.4]. The specific ruling for Felidar Sovereign confirms this two-step check [C2].

Review: **correct**. Correctly states the intervening-if check at trigger and resolution; CR 603.4 and the card ruling were supplied.
Reviewer: Codex

Missing reference groups: none

### h03-independent-trigger / repetition 1

My Solemn Simulacrum enters and its search ability goes on the stack. My opponent destroys it before that ability resolves. May I still search for a basic land with the original ability?

**Ruling:** Yes. Once the ability is on the stack, it exists independently of the Simulacrum, so destroying the Simulacrum before the ability resolves does not prevent it from resolving.

**Why:** A triggered ability exists on the stack independently of its source, and destruction or removal of the source after that time won't affect the ability [CR 113.7a]. The Simulacrum's ETB ability doesn't attempt to do anything to the Simulacrum itself during resolution—it searches your library and puts a land onto the battlefield—so there's no object it needs to "find" in a zone [CR 603.6]. The ability will resolve normally and you may search for a basic land.

Review: **correct**. Correct: the ability already on the stack resolves independently of its removed source.
Reviewer: Codex

Missing reference groups: none

### h04-replacement-death / repetition 1

Rest in Peace is on the battlefield. My Solemn Simulacrum is destroyed. Does its dies ability trigger?

**Ruling:** No. While Rest in Peace is on the battlefield, Solemn Simulacrum's "when this creature dies" ability will not trigger.

**Why:** Rest in Peace replaces the event of a card being put into a graveyard with exile, so the creature never enters a graveyard [C1]. The official ruling confirms that "when a creature dies" triggers do not fire under these conditions because the card is never put into a graveyard [C2].

Review: **correct**. Correct: Rest in Peace replaces the graveyard move, so the dies ability does not trigger.
Reviewer: Codex

Missing reference groups: CR 700.4

### h05-simultaneous-death / repetition 1

I control Blood Artist and two vanilla creature tokens. Those three creatures die simultaneously, and no other creatures die. How many times does my Blood Artist trigger?

**Ruling:** Blood Artist's ability triggers **2 times** — once for each of the two other creatures that died.

**Why:** The card's trigger condition is "whenever this creature or another creature dies," but the official ruling clarifies that when Blood Artist and other creatures die simultaneously, the ability triggers for each of the *other* creatures, not additionally for Blood Artist itself [C2]. Since two other creatures died, you get two triggers.

Review: **incorrect**. Incorrectly says two triggers. Blood Artist triggers for itself and the other two creatures; the supplied card ruling says each of those creatures. The frozen three-trigger rubric is correct.
Reviewer: Codex

Missing reference groups: none

### h06-lifelink-prevented / repetition 1

My 3/3 with lifelink would deal 3 combat damage, but all 3 damage is prevented. How much life do I gain from lifelink?

**Ruling:** You gain 0 life.

**Why:** Lifelink causes life gain only when damage is *dealt* by the source [CR 702.15b]. If all 3 damage is prevented, no damage is dealt, so the condition for lifelink's effect is never met.

Review: **correct**. Correct: prevented damage is not dealt, so lifelink gains no life.
Reviewer: Codex

Missing reference groups: CR 615.6

### h07-infect-lifelink / repetition 1

My unblocked 3/3 has both infect and lifelink and deals 3 combat damage to my opponent. No effects modify the damage. What happens to their life total, their poison counters, and my life total?

**Ruling:** Your opponent's life total is unchanged, they get 3 poison counters, and you gain 3 life.

**Why:** Infect replaces the "lose life" result with giving the player that many poison counters, so the 3 damage does not reduce their life total [CR 702.90b]. Lifelink causes its controller to gain that much life "in addition to any other results that damage causes," so you gain 3 life regardless of the infect replacement [CR 702.15b]. Both effects apply simultaneously to the same damage event.

Review: **correct**. Correctly accounts for infect and lifelink on the same damage event.
Reviewer: Codex

Missing reference groups: none

### h08-protection-wrath / repetition 1

My creature has protection from white but no indestructible. Does Wrath of God destroy it?

**Ruling:** Yes, Wrath of God destroys your creature.

**Why:** Protection from white prevents being targeted by white spells, being enchanted by white Auras, being equipped by white Equipment, damage from white sources, and being blocked by white creatures [CR 702.16b]–[CR 702.16f]. None of these components prevent a non-targeting "destroy all creatures" effect. Wrath of God doesn't target anything; it simply destroys all creatures [C1]. Since your creature lacks indestructible, nothing stops the destruction.

Review: **correct**. Correct: Wrath does not target, so protection does not prevent its destruction effect.
Reviewer: Codex

Missing reference groups: none

### h09-protection-aura / repetition 1

A white Aura legally enchants my creature. The creature then gains protection from white. What happens to the Aura?

**Ruling:** The white Aura is put into its owner's graveyard as a state-based action.

**Why:** Protection from a quality prevents a permanent from being enchanted by Auras that have that quality, and any such Auras already attached are removed to their owners' graveyards as a state-based action [CR 702.16c]. This happens automatically when state-based actions are checked; no player needs to do anything.

Review: **correct**. Correctly states the Aura is put into its owner’s graveyard by a state-based action.
Reviewer: Codex

Missing reference groups: none

### h10-own-hexproof / repetition 1

I control Slippery Bogle. Can I target it with my own Giant Growth?

**Ruling:** Yes. Hexproof only prevents a permanent from being targeted by spells or abilities your *opponents* control. Since you are casting Giant Growth on your own Slippery Bogle, hexproof does not apply.

**Why:** Hexproof means "This permanent can't be the target of spells or abilities your opponents control" [CR 702.11b]. You are not an opponent of yourself, so the restriction is not triggered. Giant Growth simply requires "target creature" [C2], and your own creature is a legal target for your own spell.

Review: **correct**. Correct: hexproof restricts opponents’ spells and abilities, not the controller’s.
Reviewer: Codex

Missing reference groups: none

### h11-ward-uncounterable / repetition 1

I cast Abrupt Decay targeting an opponent’s nonland creature with mana value 2 and ward {2}. I decline to pay the ward cost. Does ward counter Abrupt Decay? Assume the target remains legal and nothing else interferes.

**Ruling:** No. Ward does not counter Abrupt Decay, even if you decline to pay the ward cost. Abrupt Decay resolves and destroys the target.

**Why:** Ward's ability says "counter that spell or ability unless that player pays [cost]" [CR 702.21a], but Abrupt Decay's text states "This spell can't be countered" [C1]. A spell that can't be countered is not a legal object for a counter effect to act upon, so the ward trigger's effect simply has no effect on it. The official ruling confirms this directly: "Abrupt Decay won't be countered even if you don't" [C2].

Review: **partial**. Correct conclusion, but it does not explicitly state Ward triggers, as frozen criterion 1 requires.
Reviewer: Codex

Missing reference groups: CR 101.2

### h12-split-second / repetition 1

My opponent casts Krosan Grip targeting my artifact. I have a face-down Willbender, enough mana for its morph cost, and a different artifact that is a legal Grip target. While Grip is on the stack, can I turn Willbender face up and use its trigger to redirect Grip?

**Ruling:** Yes. You can turn Willbender face up while Krosan Grip is on the stack, and its triggered ability will resolve to redirect the Grip to your other artifact.

**Why:** Turning a face-down permanent face up is a special action that doesn't use the stack [CR 702.37e], and special actions are explicitly permitted while a spell with split second is on the stack [CR 702.61b]. The Krosan Grip ruling confirms this directly: "Players may turn face-down creatures face up while a spell with split second is on the stack" [C5]. Willbender's ability triggers when it is turned face up [C13], and triggered abilities are put on the stack as normal under split second [CR 702.61b]. When it resolves, "change the target" requires the new target to be legal [CR 115.7b], and your other artifact qualifies [CR 115.2].

Review: **correct**. Correctly allows the face-up special action and the resulting trigger to change Grip’s target to another legal target.
Reviewer: Codex

Missing reference groups: none

### h13-sacrifice-cost / repetition 1

I cast Fling, sacrificing my 4/4 as its additional cost. Can my opponent respond by destroying that same creature to stop me paying the sacrifice cost?

**Ruling:** No. Your opponent cannot respond to the sacrifice. The creature is sacrificed as part of paying Fling's additional cost, and no player receives priority until after the spell is fully cast and all costs have been paid.

**Why:** The spell is put on the stack first [CR 601.2a], then costs (including the sacrifice) are paid [CR 601.2h], and only after all steps are complete does the spell become cast and the controller receive priority [CR 601.2i]. Since no one has priority during the casting process, there is no window to respond to the sacrifice [CR 117.2e]. The ruling confirms this directly: "No one can try to interfere with the creature you sacrificed to prevent you from casting this spell" [C3].

Review: **correct**. Correct: the sacrifice is paid during casting before opponents receive priority.
Reviewer: Codex

Missing reference groups: none

### h14-flashback-countered / repetition 1

I cast Think Twice from my graveyard using flashback. My opponent counters it. Where does Think Twice go, and do I draw a card?

**Ruling:** Think Twice is exiled, and you do not draw a card.

**Why:** A spell cast using flashback is exiled any time it would leave the stack, whether it resolves, is countered, or leaves the stack in some other way [CR 702.34a] [C2]. Since the spell was countered, it never resolved, so its "Draw a card" effect never happened [CR 608.1].

Review: **correct**. Correct: a countered flashback spell is exiled and does not resolve its draw effect.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h15-rebound-countered / repetition 1

I cast Ephemerate from my hand, but my opponent counters it. Does rebound exile it and let me cast it next upkeep?

**Ruling:** No. If Ephemerate is countered, rebound does not function. The card goes to your graveyard and you do not get to cast it again on your next turn.

**Why:** Rebound is a static ability that functions while the spell is on the stack and creates a replacement effect that applies "as it resolves" [CR 702.88a]. Since a countered spell never resolves, the replacement effect never applies, and the card goes to the graveyard as normal. The official ruling confirms this explicitly: "If a spell with rebound that you cast from your hand is countered or doesn't resolve… none of its effects will happen, including rebound" [C5].

Review: **correct**. Correct: rebound does not apply if the spell does not resolve.
Reviewer: Codex

Missing reference groups: CR 701.5a

### h16-persist-counter / repetition 1

My Kitchen Finks has a -1/-1 counter on it when it dies. Does persist return it?

**Ruling:** No. If Kitchen Finks has a -1/-1 counter on it when it dies, persist will not return it to the battlefield.

**Why:** Persist's condition requires that the permanent had *no* -1/-1 counters on it at the moment it was put into the graveyard from the battlefield [CR 702.79a]. If it has one or more -1/-1 counters, the condition is not met and the ability does nothing [C6].

Review: **correct**. Correctly identifies the existing -1/-1 counter as blocking persist.
Reviewer: Codex

Missing reference groups: none

### h17-undying-simultaneous-sba / repetition 1

My Young Wolf has one +1/+1 counter. An effect puts one -1/-1 counter on it and gives it -1/-1 until end of turn during the same resolution, making it 0/0. At the next state-based action check it dies and the opposite counters would be removed simultaneously. Does undying trigger?

**Ruling:** No, undying does not trigger.

**Why:** Undying is a leaves-the-battlefield ability that looks back in time to check the creature's appearance immediately before it was put into the graveyard [CR 603.10]. At that moment, Young Wolf had a +1/+1 counter on it, so the condition "if it had no +1/+1 counters on it" is not met [CR 702.93a]. The -1/-1 counter and the -1/-1 continuous effect don't cancel or remove the +1/+1 counter; they simply reduce the creature's toughness to 0, causing it to die at the next state-based action check [CR 704.8]. This is the same principle as the supplied example where Young Wolf with one +1/+1 counter and three -1/-1 counters dies and undying does not trigger [CR 704.8].

(Note: counters are not "removed" when a creature dies—they remain on the object in the graveyard but simply have no effect there.)

Review: **partial**. Correct undying outcome, but the added note says counters are not removed; the +1/+1 and -1/-1 counters cancel simultaneously under CR 704.5q. That rule was not packed.
Reviewer: Codex

Missing reference groups: CR 704.5q

### h18-blink-target / repetition 1

An opponent’s Lightning Bolt targets my creature. In response I resolve Cloudshift on that creature. Does the original Bolt damage the returned creature?

**Ruling:** No. The original Lightning Bolt will not deal damage to the returned creature.

**Why:** When Cloudshift resolves, the creature is exiled and a new object enters the battlefield. The returned card is not the target of any spell that targeted it before [C5]. Since Lightning Bolt's target is no longer on the battlefield, the Bolt has no legal target when it tries to resolve and will fizzle.

Review: **correct**. Correct: Cloudshift returns a new object, leaving Lightning Bolt without a legal target.
Reviewer: Codex

Missing reference groups: CR 400.7, CR 608.2b

### h19-equip-timing / repetition 1

An opponent casts Lightning Bolt at my creature during my main phase. Can I activate Colossus Hammer’s normal equip ability in response to save it? No effect grants special activation permission.

**Ruling:** No. You cannot activate the equip ability in response to Lightning Bolt because the stack is not empty.

**Why:** Colossus Hammer's equip ability states "Equip only as a sorcery" [C2]. Under [CR 307.5], "only as a sorcery" means the player must have priority, it must be during the main phase of their turn, **and the stack must be empty**. Since Lightning Bolt is on the stack, the stack is not empty, so the equip ability cannot be activated at that time. You would need to wait until the stack resolves (or is countered) before you could equip it.

Review: **correct**. Correct: equip’s sorcery timing requires an empty stack; CR 307.5 was packed.
Reviewer: Codex

Missing reference groups: none

### h20-crew-new-creature / repetition 1

I just cast a 3/3 creature with no haste. Can I tap it to pay the crew 1 cost of my Smuggler’s Copter right now?

**Ruling:** Yes. You can tap that 3/3 creature to pay the crew 1 cost even though it just came under your control and lacks haste.

**Why:** Tapping a creature to pay a crew cost is not the same as activating that creature's own tap ability or having it attack. The ruling for Smuggler's Copter explicitly states that any untapped creature you control can be tapped to pay a crew cost, even one that just came under your control [C12]. The "summoning sickness" restriction (which haste overrides) applies to attacking and to activating a creature's own tap/untap abilities [CR 702.10b], [CR 702.10c], but does not prevent a creature from being tapped as part of another permanent's activated ability cost.

Review: **correct**. Correct: crew taps a creature to pay another permanent’s cost; it is not activating that creature’s own tap ability.
Reviewer: Codex

Missing reference groups: CR 302.6

### h21-new-vehicle / repetition 1

I cast Smuggler’s Copter this turn and crew it. It has no haste. Can it attack this turn?

**Ruling:** No, it cannot attack this turn.

**Why:** A creature can't attack unless it has been under its controller's control continuously since their most recent turn began, unless it has haste [CR 702.10b]. Since you cast the Copter this turn, it hasn't met that requirement, and it has no haste to bypass it. Once a Vehicle becomes a creature, it behaves exactly like any other artifact creature for these purposes [C10].

Review: **correct**. Correct: the Vehicle itself has not been controlled since the turn began and has no haste.
Reviewer: Codex

Missing reference groups: CR 302.6

### h22-tapped-blocker / repetition 1

After my opponent declares a 3/3 as a blocker, I tap that blocker with a spell before combat damage. Does tapping it remove it from combat or stop its combat damage?

**Ruling:** No. Tapping a creature that has already been declared as a blocker does not remove it from combat and does not prevent it from assigning combat damage. It will still deal 3 damage in the combat damage step.

**Why:** A creature remains a blocking creature until it is removed from combat or the combat phase ends; tapping is neither of those events [CR 509.1g]. In the combat damage step, each blocking creature assigns combat damage equal to its power [CR 510.1a], and a blocking creature that is still blocking assigns all its combat damage to the creature it's blocking [CR 510.1d]. Only effects that specifically remove a creature from combat (or destroy/exile it, etc.) would stop it from dealing combat damage.

Review: **correct**. Correct: tapping a declared blocker neither removes it from combat nor prevents combat damage.
Reviewer: Codex

Missing reference groups: CR 506.4b

### h23-fight-double-strike / repetition 1

My 3/3 with double strike fights a 4/4 with no relevant abilities. No other effects apply. How much damage does each deal, and which survives?

**Ruling:** The 3/3 deals 3 damage to the 4/4, and the 4/4 deals 4 damage to the 3/3. The 3/3 dies; the 4/4 survives with 3 damage marked on it.

**Why:** In a fight, each creature deals damage equal to its power to the other [CR 701.14a]. Double strike has no effect here because it modifies the combat damage step [CR 702.4a], and fight damage is explicitly not combat damage [CR 701.14d].

Review: **correct**. Correct: fight damage is not combat damage, so double strike does not add another event.
Reviewer: Codex

Missing reference groups: none

### h24-leaving-controller / repetition 1

In a multiplayer game, Alice owns a creature and Bob controls it solely through Bob’s Control Magic. Bob loses and leaves the game while Alice remains. What happens to the Aura and the creature?

**Ruling:** Control Magic leaves the game, and the creature remains on the battlefield under Alice's control.

**Why:** When a player leaves the game, all objects owned by that player leave the game, and any effects that give that player control of objects end [CR 800.4a]. Since Bob owns Control Magic (he cast it), it leaves the game. The creature is owned by Alice, so it stays and reverts to her control. This is the same outcome as the Mind Control example in the rule: "If Alex leaves the game, so does Mind Control, and Assault Griffin reverts to Bianca's control" [CR 800.4a].

Review: **correct**. Correctly applies the player-leaves rule to the Aura and returns control to the owner.
Reviewer: Codex

Missing reference groups: none

### h25-leaving-stack / repetition 1

In a three-player game, Bob controls a Lightning Bolt he owns on the stack targeting Alice. Bob loses and leaves before Bolt resolves; Alice and Charlie remain. Does Bolt still resolve?

**Ruling:** No, the Lightning Bolt does not resolve. It leaves the game when Bob leaves.

**Why:** When a player leaves the game, all objects owned by that player leave the game [CR 800.4a]. The Lightning Bolt card on the stack is an object owned by Bob, so it leaves the game and never resolves. (The separate clause about objects on the stack "not represented by cards" ceasing to exist applies to things like spell copies or tokens; a card-based spell like Lightning Bolt is covered by the first clause.)

Review: **correct**. Correct: Bob-owned Lightning Bolt leaves the game with Bob before resolving.
Reviewer: Codex

Missing reference groups: none

### h26-commander-control / repetition 1

In Commander, a particular commander has dealt me 12 combat damage while controlled by Alice and then 9 while controlled by Bob. Do those add together for commander damage, even though its controller changed?

**Ruling:** Yes. The 12 and 9 add together to 21, and you lose the game.

**Why:** The commander damage rule tracks damage dealt "by the same commander over the course of the game," not damage dealt by a specific controller [CR 903.10a]. The commander designation is an attribute of the card itself and persists regardless of who controls it [CR 903.3]. Since 21 or more combat damage from the same commander is the threshold, your total of 21 triggers the loss condition as a state-based action [CR 704.6c].

Review: **correct**. Correct: commander damage is tracked by commander identity across control changes.
Reviewer: Codex

Missing reference groups: none

### h27-commander-hand / repetition 1

An effect would return my commander from the battlefield to my hand. May I choose the command zone instead, and is that a replacement effect or a later state-based action?

**Ruling:** Yes, you may put your commander into the command zone instead of your hand, and it is a replacement effect.

**Why:** Rule 903.9b explicitly states that if a commander would be put into its owner's hand from anywhere, the owner may put it into the command zone instead, and it identifies this as a replacement effect [CR 903.9b]. The state-based action in rule 903.9a is a separate mechanism that applies only when the commander is already in a graveyard or in exile [CR 903.9a].

Review: **correct**. Correctly identifies the hand replacement option as a replacement effect, distinct from the graveyard/exile state-based action.
Reviewer: Codex

Missing reference groups: none

### h28-replacement-order / repetition 1

I control Torbran, Thane of Red Fell and Furnace of Rath. My Lightning Bolt would deal 3 damage to my opponent. No other effects apply. Who chooses the order of the two replacement effects, and what damage totals are possible?

**Ruling:** Your opponent (the player being dealt damage) chooses the order. The two possible totals are **10** (Torbran first, then Furnace of Rath) or **8** (Furnace of Rath first, then Torbran).

**Why:** When multiple replacement effects modify how much damage a source would deal, the player being dealt damage chooses the order in which to apply them [C4][C6]. Applying Torbran first gives 3 + 2 = 5, then Furnace of Rath doubles it to 10. Applying Furnace of Rath first gives 3 × 2 = 6, then Torbran adds 2 for 8. Your opponent would choose the order that results in 8.

Review: **partial**. Correct chooser and both totals. The prediction that the opponent will choose 8 is not established by the rules and is unnecessary.
Reviewer: Codex

Missing reference groups: CR 616.1

### h29-empty-library / repetition 1

My library is empty, but I have not tried to draw since it became empty. Do I immediately lose merely for having zero cards in my library?

**Ruling:** No. Having an empty library by itself does not cause you to lose the game.

**Why:** The loss condition is specifically tied to *attempting to draw* a card from a library with no cards in it. [CR 121.4] states that a player who attempts to draw from an empty library loses the game the next time a player would receive priority, and [CR 704.5b] confirms the state-based action applies when a player "attempted to draw a card from a library with no cards in it since the last time state-based actions were checked." Neither rule imposes a loss for merely having zero cards in the library.

Review: **correct**. Correct: losing requires an attempted draw from an empty library.
Reviewer: Codex

Missing reference groups: none

### h30-ambiguous-combat / repetition 1

My attacker is blocked. How much damage gets through to my opponent?

**Ruling:** If your attacking creature has trample, you must assign enough damage to the blocking creature(s) to be lethal (taking into account damage already marked on them and damage from other creatures assigned in the same combat damage step). Any damage beyond that lethal amount can be assigned to your opponent as you choose. If your creature does **not** have trample, all of its combat damage is assigned to the blocking creature(s) and none reaches your opponent.

**Why:** Trample modifies damage assignment so that excess beyond lethal damage to blockers may go through to the defending player [CR 702.19b]. Without trample, a blocked creature assigns its combat damage only to the creatures blocking it [CR 510.1c]. "Lethal damage" means damage equal to the blocker's toughness (minus any damage already marked on it), not necessarily damage that will actually kill it if an effect prevents or redirects the damage [CR 702.19b].

Review: **partial**. The conditional ruling is useful, but frozen criterion 1 specifically requires asking for attacker/blocker stats and abilities.
Reviewer: Codex

Missing reference groups: none

### h31-ambiguous-copy / repetition 1

I copy a creature. Does my copy get its counters and the bonus from its enchantment?

**Ruling:** No. The copy does not get the counters on the original creature, nor does it get the stat bonus from an enchantment affecting the original.

**Why:** When copying an object, the copy acquires only the copiable values (name, mana cost, color, types, rules text, power, toughness, etc.), and "other effects (including type-changing and text-changing effects), status, counters, and stickers are not copied" [CR 707.2]. An enchantment's +X/+X is a continuous effect applied to the original object, not a copiable value, so it doesn't transfer to the copy. The copy will have the original's printed (or otherwise set) power and toughness, but not the enchantment's modification.

Review: **incorrect**. The answer gives a definitive result without knowing the copy effect or relevant card details, contrary to both frozen criteria.
Reviewer: Codex

Missing reference groups: none

### h32-ambiguous-replacements / repetition 1

Two replacement effects apply to my token creation. How many tokens do I get?

**Ruling:** The number of tokens you get depends on the specific text of each replacement effect. Replacement effects that modify token creation apply to the event of token creation, and they also apply if another replacement effect is the one creating the token [CR 614.16]. Each effect modifies the event in sequence, so the final count is determined by what each effect's text says (e.g., "create two tokens instead" vs. "create an additional token" produce different results).

**Why:** Replacement effects act like "shields" that replace the event with a modified one [CR 614.1]. When multiple apply, they are applied one at a time, each modifying the event that the next one sees [CR 614.16]. Without the exact wording of both effects, the specific token count can't be determined.

**Need details:** Please share the exact text of both replacement effects (or the cards they come from) so I can determine the final token count.

Review: **correct**. Asks for the exact text of both effects and does not invent a token total; the event is already identified as token creation in the question.
Reviewer: Codex

Missing reference groups: CR 616.1

