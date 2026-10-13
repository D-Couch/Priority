# pre-answer-precision

Status: **complete** · implementation commit `9a635a80fb672bd199e3b0c2e8dec9cf334c5923`

Suite `novel-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 20/20 |
| Request errors | 0 |
| Truncated answers | 0 |
| Correct and normally completed | 19/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 82.5% |
| Cases retrieving every expected evidence group | 15/20 |
| Answers with citations | 20/20 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 1 |
| Reviewed citation-support failures | 1 |
| Reviewed fully correct | 19/20 reviewed |
| Reviewed accuracy | 95.0% |
| Mean reviewed rubric score | 95.0% |
| Median successful response | 6.36 s |
| p95 successful response | 9.85 s |
| Median first visible answer token | 5.15 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| n01-bestow-illegal-target (r1) | 100.0% | correct | 7.14 |
| n02-mutate-illegal-target (r1) | 50.0% | correct | 6.87 |
| n03-saga-final-chapter (r1) | 0.0% | correct | 6.89 |
| n04-prototype-graveyard (r1) | 0.0% | incorrect | 17.99 |
| n05-overload-hexproof (r1) | 100.0% | correct | 6.40 |
| n06-level-up (r1) | 100.0% | correct | 5.15 |
| n07-keyword-counter (r1) | 100.0% | correct | 6.33 |
| n08-adventure-exile (r1) | 50.0% | correct | 6.94 |
| n09-foretell-turn (r1) | 100.0% | correct | 6.00 |
| n10-suspend-last-counter (r1) | 100.0% | correct | 5.93 |
| n11-morph-special-action (r1) | 100.0% | correct | 5.16 |
| n12-dfc-returned (r1) | 100.0% | correct | 4.73 |
| n13-afterlife-exile (r1) | 100.0% | correct | 5.46 |
| n14-enlist-sickness (r1) | 100.0% | correct | 5.45 |
| n15-mentor-target (r1) | 100.0% | correct | 5.74 |
| n16-convoke-summoning-sickness (r1) | 50.0% | correct | 9.85 |
| n17-casualty-copy (r1) | 100.0% | correct | 7.54 |
| n18-myriad-tokens (r1) | 100.0% | correct | 4.42 |
| n19-totem-armor (r1) | 100.0% | correct | 8.14 |
| n20-bolster (r1) | 100.0% | correct | 6.39 |

## Answers and review notes

### n01-bestow-illegal-target / repetition 1

I cast a creature spell using its bestow cost, targeting my opponent’s creature. In response, that creature leaves the battlefield. Does my spell go to the graveyard or can it still resolve?

Ruling: Your spell does not go to the graveyard. It ceases to be bestowed, becomes a creature spell, and enters the battlefield as a creature under your control.

Why: When a bestowed Aura spell begins resolving and its target is illegal, it ceases to be bestowed and the effect making it an Aura spell ends; it continues resolving as a creature spell [CR 702.103e]. Rule 608.3b explicitly states that a bestowed Aura spell with an illegal target "becomes a creature spell and will resolve as described in rule 608.3a," which means it enters the battlefield under the controller's control [CR 608.3a].

Review: **correct**. Correct: CR 702.103e and 608.3b support ending bestowed status and resolving as a creature rather than putting the spell in the graveyard.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n02-mutate-illegal-target / repetition 1

I cast a mutating creature spell targeting a creature. Before it resolves, the target is removed. Is the mutating spell countered by the game, or does it resolve in another way?

Ruling: The mutating creature spell is not countered. It becomes a creature spell and enters the battlefield under the control of the spell's controller.

Why: Rule 608.3b explicitly carves out an exception for mutating creature spells (and bestowed Aura spells) with illegal targets: instead of failing to resolve and going to the graveyard, the spell "becomes a creature spell and will resolve as described in rule 608.3a." Rule 608.3a then states that an object resolving with no targets "becomes a permanent and enters the battlefield under the control of the spell's controller." [CR 608.3b] [CR 608.3a]

Review: **correct**. Correct: CR 608.3b and 608.3a support the illegal-target exception for mutating creature spells and their resolution as creatures.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 702.140b

### n03-saga-final-chapter / repetition 1

My Saga has just triggered its final chapter ability, which is still on the stack. Is the Saga sacrificed immediately because it has enough lore counters?

**Ruling:** No. The Saga is not sacrificed while its final chapter ability is still on the stack.

**Why:** Rule 704.5s explicitly excludes a Saga that "is the source of a chapter ability that has triggered but not yet left the stack" from the state-based action that sacrifices it [CR 704.5s]. The Saga will be sacrificed the next time state-based actions are checked after that ability leaves the stack (e.g., when it resolves or is countered), at which point the exclusion no longer applies [CR 117.5].

Review: **correct**. Correct: CR 704.5s defers the Saga sacrifice while its chapter ability remains on the stack; CR 117.5 supports the next state-based-action check after it leaves.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 714.4

### n04-prototype-graveyard / repetition 1

I cast an artifact creature as a 2/2 prototype, then it dies. In my graveyard, does it still have prototype power/toughness, or its normal characteristics?

Ruling: The card retains its prototype power/toughness in the graveyard.

Why: Prototype is a static ability [CR 702.160a]. When you choose to cast the card "prototyped," the alternative set of power, toughness, and mana cost characteristics are used — meaning they become the card's characteristics as an ongoing effect of that static ability. Since static abilities that modify characteristics apply to the object wherever it is, the card in your graveyard still has the prototype 2/2 characteristics rather than its normal ones. Note that the full details are in rule 718 ("Prototype Cards"), which is referenced but not included in the provided excerpts.

Review: **incorrect**. Incorrect and unsupported: claims prototype characteristics persist in the graveyard and extrapolates from static-ability behavior. The applicable Prototype Cards rules 718.3/718.4 were absent from the supplied context.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 718.3, CR 718.4

### n05-overload-hexproof / repetition 1

A spell says “deal 2 damage to target creature.” I cast it using overload, which changes “target” to “each.” Does it affect an opponent’s creature with hexproof?

**Ruling:** Yes. A spell cast with overload affects an opponent's creature with hexproof.

**Why:** Overload changes "target" to "each," and a spell cast this way doesn't require any targets [CR 702.96a]. Hexproof only prevents a permanent from being *the target* of an opponent's spell or ability [CR 702.11b]. Since the overloaded spell has no targets, hexproof provides no protection against it [CR 702.96b].

Review: **correct**. Correct: overload changes the target pattern to each, so the overloaded spell has no targets for hexproof to restrict.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n06-level-up / repetition 1

My leveler already has the maximum number of level counters shown on its card. Can I activate its level up ability again if I can pay?

Ruling: Yes. You may activate the level up ability regardless of how many level counters are already on the leveler, as long as you can pay the cost and it's a time you could cast a sorcery.

Why: Rule 711.4 explicitly states that "each leveler permanent has its level up ability at all times; it may be activated regardless of how many level counters are on that permanent." [CR 711.4] The ability simply adds another level counter to the permanent [CR 702.87a], even if that exceeds the maximum number shown in the level symbols.

Review: **correct**. Correct: CR 711.4 says level up can be activated regardless of current level counters; CR 702.87a supplies the sorcery timing and counter effect.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n07-keyword-counter / repetition 1

An effect puts a flying keyword counter on my creature. Does that counter give the creature flying, or is it only a marker?

Ruling: A flying keyword counter on a creature gives it the flying ability. It is not merely a marker.

Why: Rule 122.1b explicitly states that a keyword counter on a permanent causes that object to gain that keyword, and flying is listed among the keywords a keyword counter can grant [CR 122.1b]. These keyword counters are applied in Layer 6 of the layers system, alongside other ability-adding effects [CR 613.1f].

Review: **correct**. Correct: CR 122.1b says flying keyword counters grant flying, and CR 613.1f places the effect in layer 6.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n08-adventure-exile / repetition 1

I cast the Adventure half of a card and it resolves. The card is exiled instead of going to the graveyard. Can I later cast its creature half from exile, and can I cast the Adventure half again using that permission?

**Ruling:** Yes, you can cast the creature half from exile. No, you cannot cast the Adventure half again using that specific permission, though other effects that allow you to cast it may allow you to cast it as an Adventure.

**Why:** Rule 715.3d states that after an Adventure spell resolves, the card is exiled and "for as long as that card remains exiled, that player may play it," but explicitly adds "It can't be cast as an Adventure this way, although other effects that allow a player to cast it may allow a player to cast it as an Adventure." [CR 715.3d]

Review: **correct**. Correct: CR 715.3d distinguishes the permission to cast the creature face from the prohibited Adventure cast under that permission.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 715.4

### n09-foretell-turn / repetition 1

I foretell a card during my turn. Can I cast it later in that same turn by paying its foretell cost?

Ruling: No. You cannot cast a foretold card during the same turn you foretold it.

Why: The foretell ability explicitly states that the card may be cast "after the current turn has ended" [CR 702.143a]. Rule 702.143d reinforces this, specifying the card "may be cast for any foretell cost it has after the turn it became a foretold card has ended" [CR 702.143d].

Review: **correct**. Correct: the supplied foretell rules prevent casting until after the turn the card became foretold has ended.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n10-suspend-last-counter / repetition 1

The last time counter is removed from my suspended card during upkeep. Must I cast it, and do I pay its mana cost?

Ruling: No, you are not required to cast it, and no, you do not pay its mana cost.

Why: The suspend ability states that when the last time counter is removed, "you may play it without paying its mana cost if able," and "if you don't, it remains exiled" [CR 702.62a]. The word "may" makes the casting optional, and the text explicitly waives the mana cost.

Review: **correct**. Correct: CR 702.62a makes casting optional and allows play without paying its mana cost if able; it does not claim the card mana cost changes.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n11-morph-special-action / repetition 1

My opponent has an instant on the stack. I have priority and control a face-down creature with morph. May I pay its morph cost and turn it face up now, and does that use the stack?

**Ruling:** Yes. You may turn your face-down morph permanent face up any time you have priority, even while an opponent's instant is on the stack. It does not use the stack.

**Why:** Turning a face-down morph permanent face up is a special action that can be taken any time you have priority [CR 702.37e] [CR 117.1c]. The rule explicitly states it "doesn't use the stack" [CR 702.37e].

Review: **correct**. Correct: CR 702.37e and 117.1c support turning a face-down morph permanent face up as a special action while holding priority, without using the stack.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n12-dfc-returned / repetition 1

A double-faced card is returned directly from my graveyard to the battlefield by an effect. No instruction specifies a face. Which face enters?

Ruling: It enters the battlefield with its front face up.

Why: A double-faced card put onto the battlefield from a zone other than the stack enters with its front face up by default [CR 712.14]. Since the graveyard is a zone other than the stack and no effect specifies otherwise, the front face is the default.

Review: **correct**. Correct: CR 712.14 supports a double-faced card entering from a non-stack zone front-face up by default.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n13-afterlife-exile / repetition 1

A creature with afterlife 2 is exiled directly from the battlefield instead of dying. Do I create two Spirit tokens?

Ruling: No, you do not create two Spirit tokens.

Why: Afterlife 2 triggers only "when this permanent is put into a graveyard from the battlefield" [CR 702.135a]. If the creature is exiled directly from the battlefield, it is never put into a graveyard, so the trigger condition is never met and no tokens are created.

Review: **correct**. Correct: CR 702.135a requires the permanent to be put into a graveyard; direct exile does not satisfy that trigger condition.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n14-enlist-sickness / repetition 1

I just gained control of a creature without haste this turn. May I tap it to pay another attacker’s enlist cost as it attacks?

Ruling: No. You may not tap that creature to pay the enlist cost.

Why: Enlist's cost requires the tapped creature to either have haste or have been under your control continuously since the turn began [CR 702.154a]. Since you gained control of it this turn and it lacks haste, it satisfies neither condition and is not a legal choice for the cost.

Review: **correct**. Correct: CR 702.154a requires the enlisted creature to have haste or to have been controlled since the turn began; the stated creature meets neither condition.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n15-mentor-target / repetition 1

My 4/4 with mentor attacks alongside my 3/3. Can the mentor ability target that 3/3?

**Ruling:** Yes. The mentor ability can target the 3/3.

**Why:** Mentor means "put a +1/+1 counter on target attacking creature with power less than this creature's power" [CR 702.134a]. The 3/3 is an attacking creature and its power (3) is less than the 4/4's power (4), so it is a legal target.

Review: **correct**. Correct: CR 702.134a defines mentor as a trigger targeting an attacking creature with lower power; it does not misclassify the ability.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n16-convoke-summoning-sickness / repetition 1

I cast a creature this turn and it has no haste. May I tap it to help pay the convoke cost of another spell?

Ruling: Yes. You may tap a creature you cast this turn (even without haste) to pay a convoke cost.

Why: Convoke is a static ability that lets you "tap an untapped creature" as part of paying a spell's total cost [CR 702.51a]. It does not require the creature to have been under your control since your last turn began. Haste is only needed to use a creature's activated abilities with a tap or untap cost [CR 702.10c], which is a different mechanism from paying a convoke cost.

Review: **correct**. Correct: CR 702.51a permits tapping creatures to pay convoke; the cited haste restriction concerns activated abilities, not this cost payment.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### n17-casualty-copy / repetition 1

I cast a spell with casualty 2 and sacrifice a 2/2 as its additional cost. Does the spell get copied, and may the copy have a different target?

Ruling: Yes, the spell is copied, and if it has any targets, you may choose new targets for the copy.

Why: Casualty 2 means "As an additional cost to cast this spell, you may sacrifice a creature with power 2 or greater," and "When you cast this spell, if a casualty cost was paid for it, copy it. If the spell has any targets, you may choose new targets for the copy." [CR 702.153a] Since you sacrificed a 2/2 (power 2 or greater), the casualty cost was paid, triggering the copy. When choosing new targets for the copy, you may leave any number unchanged, but any new targets must be legal. [CR 707.10c]

Review: **correct**. Correct: CR 702.153a supports the casualty cost and copy; the 2/2 meets the power threshold and the target handling is supported by CR 707.10c.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n18-myriad-tokens / repetition 1

Myriad creates two attacking token copies in a four-player game. What happens to those tokens at end of combat?

**Ruling:** The Myriad tokens are exiled at end of combat.

**Why:** The rule text for Myriad explicitly states: "If one or more tokens are created this way, exile the tokens at end of combat." [CR 702.116a] This applies regardless of the number of players or tokens created.

Review: **correct**. Correct: CR 702.116a explicitly exiles tokens created by myriad at end of combat.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n19-totem-armor / repetition 1

A creature enchanted by an Aura with totem armor would be destroyed by lethal damage. Is the creature destroyed?

**Ruling:** No, the creature is not destroyed. The umbra armor (formerly "totem armor") replacement effect replaces the destruction event: instead, all damage marked on the creature is removed and the Aura is destroyed.

**Why:** Umbra armor is a replacement effect that reads "If enchanted permanent would be destroyed, instead remove all damage marked on it and destroy this Aura" [CR 702.89a]. Older cards printed with "totem armor" have been updated to refer to umbra armor [CR 702.89b]. Since the destruction event is replaced, the creature survives with no damage marked on it, and the Aura goes to its owner's graveyard.

Review: **correct**. Correct: the supplied umbra armor rule replaces destruction by removing damage and destroying the Aura, so the creature survives that destruction event.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n20-bolster / repetition 1

An effect tells me to bolster 2. I control two creatures tied for least toughness and one larger creature. How do I choose and place the counters?

**Ruling:** You may choose either of the two creatures tied for least toughness and put 2 +1/+1 counters on it. The larger creature is not a valid choice.

**Why:** "Bolster N" instructs you to "choose a creature you control with the least toughness or tied for least toughness among creatures you control" and then put N +1/+1 counters on that creature [CR 701.39a]. Since both of your smaller creatures are tied for least toughness, either one is a legal choice; the larger creature does not qualify.

Review: **correct**. Correct: CR 701.39a permits choosing any creature tied for least toughness, excluding the larger creature.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

