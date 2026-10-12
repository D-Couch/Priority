# Packing experiment: mixed result

The 32-case score remains 25/32; the original suite remains 20/20. Reserving context for relevant card rulings fixes h20 (crew with a newly controlled creature) by including C12. It also introduces a new unsupported counterfactual in h19: the model claims +10/+10 would not save a creature from three damage. This offsets the improvement. The new suite has four answers with factual contradictions both before and after.

Other failure classes: h07 incorrectly classifies damage results as replacement effects; h13 overgeneralizes timing/last-known information; h23 confuses damage marked with remaining toughness. h25 and h26 lack necessary rule evidence and abstain. h31 fails the explicit clarification rubric. h01 and h24 additionally have evidence-applicability gaps despite correct conclusions.

Next intervention is source-quoted explanations with a single application sentence, to reduce unsupported elaboration without changing retrieval, model or sampling. The packing change is not claimed as a standalone accuracy improvement. Later combined configurations must still be checked against the original baseline, not only this intermediate result.
