# Source-quotation prompt experiment: not adopted

The source-quotation contract is a separate committed experiment. Against the preceding relevant-rulings configuration, the held-out result stayed at 25/32 correct and complete; the original suite stayed at 20/20. Citation-support failures fell from 10 to 9, with no change in citation-ID validity or evidence recall. Held-out median latency changed from 10.26s to 10.25s, while p95 rose from 18.79s to 28.99s in these single runs.

The change fixed several explanations (h01 uses an applicable general APNAP/stack rule; h07 stops calling infect/lifelink replacement effects; h19 drops an inaccurate damage counterfactual). It also added unsupported timing or state claims in h05 and h24, and did not repair h13 cost sequencing or h23 damage-marked-versus-toughness error. AI-assisted manual review, not independent human validation.

Since the correctness score did not increase and new factual claims appeared, the prompt modification was reverted in its own commit. The measured run and its code commit remain available for review. The next stage uses the retained keyword/ruling-packing configuration as the matched hybrid-retrieval baseline.
