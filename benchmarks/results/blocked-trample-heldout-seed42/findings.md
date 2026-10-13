# Blocked-attacker trample retrieval findings

## Hypothesis

The heldout h30 answer treated a blocked attacker as if it could never deal damage to the defending player. The retrieved context included CR 510.1c but omitted the trample rule, CR 702.19b. Promoting that rule for blocked-attacker damage questions should make the missing condition visible to the model and support an appropriate clarification.

## Result

The target answer now asks whether the attacker has trample and requests the attacker’s power and blocker toughness instead of asserting a damage total. In the full heldout-v1 run, reviewed results changed from 29/32 to 30/32 and expected-evidence recall rose from 82.0% to 83.6%. No other scenario’s reviewed status changed. Median latency was 0.02 seconds higher and p95 was 0.41 seconds higher in this single run; these differences are descriptive and do not establish a latency regression.

The retrieval test verifies that CR 702.19b is selected and survives context packing for the h30 query. The rules retrieval change is useful for other blocked-attacker questions as well, but this one run is not enough to establish a general accuracy gain.

## Remaining question

h31 remains marked incorrect because its frozen rubric requires a clarifying question about the copy effect and enchantment. The answer gives the general rule that counters and other effects are not copied. Whether the rubric should require clarification for that wording needs independent Magic judge review; this run does not alter or weaken the frozen rubric.

## Review limits

The suite and review are AI-authored or AI-assisted, not independently validated by a Magic judge. Treat the 30/32 result as a development regression measurement, not an accuracy estimate for normal gameplay questions.
