# Verification run — gameplay-v1

This one-repetition seed-42 run used the existing local Qwen 3.8 27B Q4_K_M model, LM Studio settings, frozen corpus, and lexical retrieval. The benchmark's implementation hashes match the preceding implementation; the commit difference is provenance and benchmark-documentation cleanup.

Codex's AI-assisted rubric review found 20/20 fully correct answers and no unsupported claims. This is not independent human validation. Expected-evidence recall was 96.25% (18/20 cases retrieved every authored evidence group); median latency was 11.27 seconds and p95 was 19.03 seconds. There were no request errors or truncated answers.

Compared with the previous seed-42 gameplay run, the reviewed score, evidence recall, citation-ID validity, error count, and truncation count are unchanged. Median latency increased by 0.32 seconds and p95 by 0.88 seconds. The generated wording changed in all 20 cases despite the same seed, so each answer was reviewed against the frozen criteria. Semantic citation support was not independently rescored.
