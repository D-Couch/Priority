# novel-v1 first baseline

This is the first inference run on the 20-case novel-v1 set, frozen before inference and separate from the regression suites. Seed 42, lexical retrieval, same local Qwen/LM Studio configuration. Result: 17/20 fully correct (85%) with one request error, two unsupported-claim answers, 82.5% expected-evidence recall, 8.21 s median latency, and 14.85 s p95. There were no truncated answers. These outcomes are exploratory because both scenarios and rubrics are AI-authored and have not been checked by an independent human Magic judge.

The errors identify targeted failures: n04-prototype-graveyard returned no final answer; n03-Saga and n04-prototype retrieval missed expected rule passages; n10 incorrectly described suspend as making a card’s mana cost zero; and n15 called mentor a replacement ability. The n03 evidence-label defect is documented in `benchmarks/novel-v1/REFERENCE-ADDENDUM.md`; the frozen labels and recorded evidence score are unchanged.

Review: Codex (AI-assisted manual review; no independent human judge). Each answer was graded against its frozen criteria and excerpts, including the request error.
