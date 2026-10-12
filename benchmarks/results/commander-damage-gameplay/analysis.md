# Gameplay regression check — Commander damage retrieval

This 20-case gameplay-v1 rerun checks the targeted Commander-topic routing change. It used the same local Qwen 3.8 27B Q4_K_M model, LM Studio configuration, frozen corpus, lexical mode, and seed 42 as the 2026-10-12 verification run.

The reviewed result remains 20/20 fully correct under the AI-assisted rubric, with 96.25% expected-evidence recall (18/20 cases retrieving all authored evidence), no errors, no truncations, and no unsupported-claim flags. Two Commander responses changed in wording/source set; both were checked against their rubrics and the frozen Comprehensive Rules and remained correct. The other 18 answers and packed excerpts matched byte-for-byte, so their previous AI-assisted grades were carried forward. This is not independent human judge validation.

Median latency was 10.87s versus 11.27s in the previous one-run measurement; p95 was 19.58s versus 19.03s. A single seeded run is descriptive and does not establish a performance change.
