# Second-seed verification

Seeds 42 and 43 each score **20/20 rubric-correct and normally completed**, for 40/40 reviewed answers across two runs of the same 20 development scenarios. Neither run contains a truncated or empty answer. Median completed-request latency is 10.21 seconds for seed 42 and 9.95 seconds for seed 43.

Verified identical implementation-file hashes, frozen corpus/reference/suite hashes, model configuration, supplied source lists, and prompt hashes. Sampling differs only in seed. This is a variability check, not a new implementation comparison; the comparison guard was not bypassed to compare mismatched seeds.

Reviews are AI-assisted, not independent human validation. These are not 40 unique scenarios and not a held-out accuracy claim. One seed-42 answer uses plain rule numbers instead of clickable bracketed citations; the corresponding seed-43 answer uses the expected format. Citation formatting and substantive correctness remain separate metrics.

Before vectorization, freeze additional unseen scenarios and paraphrases so improvement is not hidden by the current suite's ceiling. Preserve both these runs as the improved vector-free reference point and the original pre-vectorization tag as the original baseline.
