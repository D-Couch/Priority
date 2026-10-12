# Verification run — heldout-v1

This one-repetition seed-42 run used the existing local Qwen 3.8 27B Q4_K_M model, LM Studio settings, frozen corpus, and lexical retrieval. The benchmark's implementation hashes match the preceding implementation; the commit difference is provenance and benchmark-documentation cleanup.

The 32 answers and packed excerpts exactly match the preceding seed-42 held-out run. Its AI-assisted substantive grades were carried forward: 25/32 fully correct, with five answers flagged for unsupported or contradictory claims. This is not independent human validation. Expected-evidence recall was 78.125% (17/32 cases retrieved every authored evidence group); median latency was 10.30 seconds and p95 was 16.94 seconds. There were no request errors or truncated answers.

Compared with the previous held-out run, reviewed accuracy, evidence recall, citation-ID validity, errors, truncation, and correctness are unchanged. Median latency was 0.44 seconds lower and p95 was 0.27 seconds lower. One repetition is descriptive and does not establish a performance improvement. Semantic citation support remains unavailable where it was not previously reviewed.
