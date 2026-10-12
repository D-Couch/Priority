# novel-v1-baseline

Status: **complete** · implementation commit `004746b3ff3813c7035f6a581e29ba059b7ea132`

Suite `novel-v1` · model `qwen/qwen3.8-27b` · 1 repetition(s) · seed(s) [42]

| Metric | Result |
| --- | --- |
| Completed requests | 19/20 |
| Request errors | 1 |
| Truncated answers | 0 |
| Correct and normally completed | 17/20 reviewed |
| Unknown finish reason | 0 |
| Mean expected-evidence recall | 82.5% |
| Cases retrieving every expected evidence group | 15/20 |
| Answers with citations | 19/19 |
| Citation ID validity (not semantic support) | 100.0% |
| Answers with unsupported/contradictory claims | 2 |
| Reviewed citation-support failures | 3 |
| Reviewed fully correct | 17/20 reviewed |
| Reviewed accuracy | 85.0% |
| Mean reviewed rubric score | 95.0% |
| Median successful response | 8.21 s |
| p95 successful response | 14.85 s |
| Median first visible answer token | 6.57 s |

Only the first heldout-v1 baseline is an unseen-case measurement; after inspection that suite becomes regression data. Rubrics are AI-authored, not independent human validation. Citation validity only checks source IDs. Evidence recall measures the authored reference groups, not all potentially relevant rules. Timings include retrieval and generation; failed requests are reported separately and excluded from latency percentiles.

| Scenario | Evidence recall | Reviewed result | Total s |
| --- | --- | --- | --- |
| n01-bestow-illegal-target (r1) | 100.0% | correct | 10.02 |
| n02-mutate-illegal-target (r1) | 50.0% | correct | 8.27 |
| n03-saga-final-chapter (r1) | 0.0% | correct | 8.16 |
| n04-prototype-graveyard (r1) | 0.0% | request error | 26.76 |
| n05-overload-hexproof (r1) | 100.0% | correct | 10.74 |
| n06-level-up (r1) | 100.0% | correct | 8.34 |
| n07-keyword-counter (r1) | 100.0% | correct | 8.21 |
| n08-adventure-exile (r1) | 50.0% | correct | 13.15 |
| n09-foretell-turn (r1) | 100.0% | correct | 7.27 |
| n10-suspend-last-counter (r1) | 100.0% | partial | 7.55 |
| n11-morph-special-action (r1) | 100.0% | correct | 7.86 |
| n12-dfc-returned (r1) | 100.0% | correct | 7.32 |
| n13-afterlife-exile (r1) | 100.0% | correct | 7.05 |
| n14-enlist-sickness (r1) | 100.0% | correct | 6.79 |
| n15-mentor-target (r1) | 100.0% | partial | 7.87 |
| n16-convoke-summoning-sickness (r1) | 50.0% | correct | 14.85 |
| n17-casualty-copy (r1) | 100.0% | correct | 9.58 |
| n18-myriad-tokens (r1) | 100.0% | correct | 9.07 |
| n19-totem-armor (r1) | 100.0% | correct | 9.77 |
| n20-bolster (r1) | 100.0% | correct | 7.74 |

## Answers and review notes

### n01-bestow-illegal-target / repetition 1

I cast a creature spell using its bestow cost, targeting my opponent’s creature. In response, that creature leaves the battlefield. Does my spell go to the graveyard or can it still resolve?

Ruling: Your spell does **not** go to the graveyard. It ceases to be bestowed, the Aura effect ends, and it resolves as a creature spell, entering the battlefield under your control.

Why: When a bestowed Aura spell begins resolving and its target is no longer legal, it ceases to be bestowed and continues resolving as a creature spell [CR 702.103e]. Rule 608.3b explicitly carves out this case: a bestowed Aura spell with an illegal target "becomes a creature spell and will resolve as described in rule 608.3a," which means it enters the battlefield under your control [CR 608.3a]. This is a specific exception to the general rule that a spell with all illegal targets is put into its owner's graveyard [CR 608.2b].

Review: **correct**. Correctly says an illegal target ends bestowed status and the spell resolves as a creature; 702.103e and 608.3b support the outcome.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n02-mutate-illegal-target / repetition 1

I cast a mutating creature spell targeting a creature. Before it resolves, the target is removed. Is the mutating spell countered by the game, or does it resolve in another way?

Ruling: The mutating creature spell is not countered. It becomes a creature spell (losing its target) and resolves by entering the battlefield as a new creature under your control.

Why: Rule 608.3b specifically carves out mutating creature spells: if the target is illegal, the spell "becomes a creature spell and will resolve as described in rule 608.3a" rather than being removed to the graveyard [CR 608.3b]. Rule 608.3a then states that an object resolving with no targets "becomes a permanent and enters the battlefield under the control of the spell's controller" [CR 608.3a]. So the creature simply enters the battlefield as a new permanent without merging with anything.

Review: **correct**. Correct conclusion and entry as a creature spell are directly supported by 608.3b/608.3a, even though the specifically expected 702.140b excerpt was not retrieved.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 702.140b

### n03-saga-final-chapter / repetition 1

My Saga has just triggered its final chapter ability, which is still on the stack. Is the Saga sacrificed immediately because it has enough lore counters?

Ruling: No. While the final chapter ability is still on the stack, the Saga is not sacrificed. The state-based action that sacrifices it is explicitly suspended until that ability leaves the stack.

Why: Rule 704.5s requires two conditions for the sacrifice: the lore-counter threshold is met **and** the Saga "isn't the source of a chapter ability that has triggered but not yet left the stack." Because your final chapter ability is still on the stack, the second condition is not satisfied, so the state-based action does not apply [CR 704.5s]. Once that ability resolves and is removed from the stack [CR 608.2n], the next time state-based actions are checked the Saga will be sacrificed [CR 704.5s].

Review: **correct**. Correctly says the Saga is not sacrificed while its chapter ability remains on the stack and identifies the SBA. It quotes 704.5s, which directly states this rule, although the rubric expected 714.4; this is an evidence-label omission documented in the addendum.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 714.4

### n04-prototype-graveyard / repetition 1

I cast an artifact creature as a 2/2 prototype, then it dies. In my graveyard, does it still have prototype power/toughness, or its normal characteristics?

(No answer.)

Request error: No final answer returned

Review: **error**. Request failed with “No final answer returned”; no substantive ruling was available to grade.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 718.3, CR 718.4

### n05-overload-hexproof / repetition 1

A spell says “deal 2 damage to target creature.” I cast it using overload, which changes “target” to “each.” Does it affect an opponent’s creature with hexproof?

Ruling: Yes. When you cast the spell using overload, it deals 2 damage to the opponent's hexproof creature.

Why: Overload replaces every instance of "target" with "each," so the spell reads "deal 2 damage to each creature" and no longer requires any targets [CR 702.96a]. A spell cast with its overload cost paid "won't require any targets" and "may affect objects that couldn't be chosen as legal targets" [CR 702.96b]. Hexproof only prevents a permanent from being *targeted* by an opponent's spell [CR 702.11b]; since the overloaded spell targets nothing, hexproof has no effect on it.

Review: **correct**. Correct: overload changes target to each, removing target requirements, so the hexproof creature can be affected.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n06-level-up / repetition 1

My leveler already has the maximum number of level counters shown on its card. Can I activate its level up ability again if I can pay?

Ruling: Yes. You may activate the level up ability even if the leveler already has the maximum number of level counters indicated by its level symbols, as long as you can pay the cost and it's your main phase (sorcery timing).

Why: The level up ability is defined simply as "Put a level counter on this permanent. Activate only as a sorcery" [CR 702.87a], with no restriction based on existing level counters. Rule 711.4 explicitly confirms that "each leveler permanent has its level up ability at all times; it may be activated regardless of how many level counters are on that permanent" [CR 711.4]. The level symbols (e.g., {LEVEL 1-4}, {LEVEL 5+}) only determine which P/T and abilities apply based on the counter count [CR 711.2a][CR 711.2b]; they do not gate the activation of the level up ability itself.

Review: **correct**. Correctly says level up may be activated regardless of current level-counter count and mentions sorcery timing.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n07-keyword-counter / repetition 1

An effect puts a flying keyword counter on my creature. Does that counter give the creature flying, or is it only a marker?

Ruling: A flying keyword counter on a creature causes that creature to gain the flying ability. It is not merely an inert marker.

Why: Rule 122.1b explicitly states that a keyword counter on a permanent "causes that object to gain that keyword," and lists flying among the valid keywords for such counters [CR 122.1b]. While a counter is technically a marker that modifies characteristics [CR 122.1], in this case the modification is the granting of the flying ability itself, so the creature can't be blocked except by creatures with flying and/or reach [CR 702.9b].

Review: **correct**. Correctly explains that a flying keyword counter grants flying.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n08-adventure-exile / repetition 1

I cast the Adventure half of a card and it resolves. The card is exiled instead of going to the graveyard. Can I later cast its creature half from exile, and can I cast the Adventure half again using that permission?

Ruling: Yes, you may cast the creature half from exile using the permission granted by the Adventure's resolution. No, you may not cast the Adventure half again using that same permission, though a separate effect that allows you to cast it could let you do so.

Why: Rule 715.3d states that after an Adventure spell resolves, the card is exiled and "for as long as that card remains exiled, that player may play it," but explicitly adds "It can't be cast as an Adventure this way, although other effects that allow a player to cast it may allow a player to cast it as an Adventure" [CR 715.3d]. "Playing" a non-land card means casting it as a spell [CR 601.1a], and when you play an adventurer card you choose whether to play it normally or as an Adventure [CR 715.3]. The 715.3d permission therefore lets you cast the creature half but specifically excludes the Adventure half under that permission.

Review: **correct**. Correctly distinguishes the permission to play the exiled card from permission to cast it as an Adventure.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 715.4

### n09-foretell-turn / repetition 1

I foretell a card during my turn. Can I cast it later in that same turn by paying its foretell cost?

Ruling: No. You cannot cast a foretold card later in the same turn you foretold it. You may only cast it after the current turn has ended.

Why: Rule 702.143a explicitly states that the foretelling player "may cast that card after the current turn has ended by paying any foretell cost it has rather than paying that spell's mana cost." Rule 702.143d reinforces this, specifying the card "may be cast for any foretell cost it has after the turn it became a foretold card has ended." [CR 702.143a] [CR 702.143d]

Review: **correct**. Correct: the card may be cast after the turn it was foretold ends, not during that turn.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n10-suspend-last-counter / repetition 1

The last time counter is removed from my suspended card during upkeep. Must I cast it, and do I pay its mana cost?

Ruling: No, you are not required to cast it, and no, you do not pay its mana cost.

Why: The suspend ability says "you **may** play it without paying its mana cost if able. If you don't, it remains exiled," making the cast optional and the mana cost zero [CR 702.62a]. Casting in this way follows the rules for paying alternative costs [CR 702.62d], so the spell's normal mana cost is replaced rather than reduced.

Review: **partial**. Correctly says casting is optional and without paying its mana cost if able, but then incorrectly says the card’s mana cost becomes zero; suspend waives payment and does not change the card’s mana cost.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n11-morph-special-action / repetition 1

My opponent has an instant on the stack. I have priority and control a face-down creature with morph. May I pay its morph cost and turn it face up now, and does that use the stack?

Ruling: Yes. Because you have priority, you may pay the morph cost and turn your face-down creature face up right now, even with your opponent's instant on the stack. Turning a morph permanent face up is a special action and does not use the stack.

Why: Rule 702.37e explicitly states that "any time you have priority, you may turn a face-down permanent you control with a morph ability face up" and that "this is a special action; it doesn't use the stack." [CR 702.37e] Rule 117.1c confirms that a player may take special actions any time they have priority. [CR 117.1c]

Review: **correct**. Correctly identifies turning a morph permanent face up as a special action available with priority and not using the stack.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n12-dfc-returned / repetition 1

A double-faced card is returned directly from my graveyard to the battlefield by an effect. No instruction specifies a face. Which face enters?

Ruling: The double-faced card enters the battlefield with its front face up.

Why: A double-faced card put onto the battlefield from a zone other than the stack (such as the graveyard) enters with its front face up by default [CR 712.14]. Since no effect specifies "transformed" or "converted," the default applies [CR 712.14a].

Review: **correct**. Correctly says a double-faced card entering from a non-stack zone enters front face up by default.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n13-afterlife-exile / repetition 1

A creature with afterlife 2 is exiled directly from the battlefield instead of dying. Do I create two Spirit tokens?

Ruling: No. You do not create the Spirit tokens.

Why: Afterlife 2 triggers only "when this permanent is put into a graveyard from the battlefield" [CR 702.135a]. Being exiled from the battlefield is a different zone change; the permanent is never put into a graveyard, so the trigger condition is never met and no tokens are created.

Review: **correct**. Correctly says direct exile does not satisfy afterlife’s battlefield-to-graveyard trigger condition.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n14-enlist-sickness / repetition 1

I just gained control of a creature without haste this turn. May I tap it to pay another attacker’s enlist cost as it attacks?

Ruling: No. You may not tap that creature to pay the enlist cost.

Why: Enlist's optional cost requires the tapped creature to either have haste or to have been under your control continuously since the turn began [CR 702.154a]. A creature you just gained control of this turn satisfies neither condition, so it is not a legal choice for the cost [CR 508.1g].

Review: **correct**. Correctly applies enlist’s haste-or-continuous-control requirement to the creature tapped for the optional attack cost.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n15-mentor-target / repetition 1

My 4/4 with mentor attacks alongside my 3/3. Can the mentor ability target that 3/3?

Ruling: Yes. The 3/3 is a legal target for the Mentor ability.

Why: Mentor's replacement text requires the target to be "an attacking creature with power less than this creature's power" [CR 702.134a]. Your 3/3 is declared as an attacker alongside the 4/4, and its power (3) is less than the 4/4's power (4), so it satisfies both conditions. The target is chosen when the triggered ability is put on the stack [CR 115.1d], at which point the 3/3 is still an attacking creature.

Review: **partial**. The target ruling is correct, but it calls mentor’s triggered ability “replacement text,” incorrectly classifying the mechanic; 702.134a defines mentor as a triggered ability.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n16-convoke-summoning-sickness / repetition 1

I cast a creature this turn and it has no haste. May I tap it to help pay the convoke cost of another spell?

Ruling: Yes. You may tap a creature you cast this turn (even without haste) to pay the convoke cost of another spell, provided it is untapped and you control it.

Why: Convoke is a static ability that lets you "tap an untapped creature you control" in place of mana [CR 702.51a]. It does not require the creature to have been under your control since the beginning of your turn, nor does it require haste. The "summoning sickness" restriction on tap actions applies to attacking [CR 702.10b] and to activating tap abilities [CR 702.10c], but convoke is neither an attack nor an activated ability—it is part of the cost-payment process [CR 702.51b].

Review: **correct**. Correctly says a newly controlled creature can be tapped for convoke and distinguishes that cost from activating its own tap ability.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: CR 302.6

### n17-casualty-copy / repetition 1

I cast a spell with casualty 2 and sacrifice a 2/2 as its additional cost. Does the spell get copied, and may the copy have a different target?

Ruling: Yes. Sacrificing a 2/2 creature satisfies the Casualty 2 additional cost (power 2 ≥ 2), so the triggered "copy it" ability fires. If the spell has any targets, you may choose new targets for the copy.

Why: Casualty N's second ability reads, "When you cast this spell, if a casualty cost was paid for it, copy it. If the spell has any targets, you may choose new targets for the copy." [CR 702.153a] The copy is placed on the stack with whatever targets you select; any targets you change must be legal, while targets you leave unchanged may even be illegal. [CR 707.10c]

Review: **correct**. Correctly applies Casualty 2 and explains that the copy may use new targets.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n18-myriad-tokens / repetition 1

Myriad creates two attacking token copies in a four-player game. What happens to those tokens at end of combat?

Ruling: The two Myriad tokens are exiled at end of combat.

Why: Myriad's text explicitly states, "If one or more tokens are created this way, exile the tokens at end of combat." [CR 702.116a] This is a delayed triggered ability that triggers at the end of combat, causing all tokens created by that Myriad instance to be exiled. The number of tokens (two in a four-player game, one for each opponent other than the defending player) does not change the outcome; all of them are exiled together. [CR 702.116a]

Review: **correct**. Correctly says the two Myriad tokens are exiled at end of combat.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n19-totem-armor / repetition 1

A creature enchanted by an Aura with totem armor would be destroyed by lethal damage. Is the creature destroyed?

Ruling: No, the creature is not destroyed. The umbra armor (formerly "totem armor") replacement effect intervenes: instead of the creature being destroyed, all damage marked on it is removed and the Aura is destroyed.

Why: Lethal damage causes a creature to be destroyed as a state-based action [CR 704.5g]. Umbra armor is a static ability that reads "If enchanted permanent would be destroyed, instead remove all damage marked on it and destroy this Aura" [CR 702.89a], and older cards printed with "totem armor" use this same Oracle text [CR 702.89b]. Because the destruction event is replaced, the creature survives with no damage marked on it, while the Aura goes to its owner's graveyard.

Review: **correct**. Correctly explains that totem/umbra armor replaces destruction, removes marked damage, and destroys the Aura instead.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

### n20-bolster / repetition 1

An effect tells me to bolster 2. I control two creatures tied for least toughness and one larger creature. How do I choose and place the counters?

Ruling: You must choose one of the two creatures tied for least toughness (you cannot choose the larger creature), and you put all 2 +1/+1 counters on that single chosen creature.

Why: "Bolster N" instructs you to "Choose a creature you control with the least toughness or tied for least toughness among creatures you control. Put N +1/+1 counters on that creature." [CR 701.39a] The choice is limited to creatures with the least toughness (including those tied for it), and all N counters are placed on the one creature you selected.

Review: **correct**. Correctly chooses one creature tied for least toughness and places both counters on that creature.
Reviewer: Codex (AI-assisted manual review; no independent human judge)

Missing reference groups: none

