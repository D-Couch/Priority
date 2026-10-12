# heldout-baseline → hybrid-family-heldout

Implementation `e184b2efaf1b5dc10398fb50c678fc24e49309f0` → `d55b40a747a4382d9e8aebb4d41c65db85575948`

- `retrieval`: {'mode': 'lexical'} → {'mode': 'hybrid', 'model': 'text-embedding-nomic-embed-text-v1.5', 'index_sha256': '75f64df4ff56260946df760cca833ce64e83d6bab54dd1977f2e76ad16d74535', 'index_metadata': {'format': 1, 'model': 'text-embedding-nomic-embed-text-v1.5', 'model_identity': {'key': 'text-embedding-nomic-embed-text-v1.5', 'quantization': {'name': 'Q4_K_M', 'bits_per_weight': 4}, 'size_bytes': 84106624, 'format': 'gguf', 'max_context_length': 2048}, 'rules_sha256': '312e45147b0d2d1a5fa2e1388635230a5394f354c042e73b5cdb0d8cc2eda38a', 'dimensions': 768, 'chunks': 3353, 'rules': 3312, 'build_seconds': 11.376, 'document_prefix': 'search_document: ', 'query_prefix': 'search_query: ', 'chunk_characters': 1200, 'overlap_characters': 200}, 'fusion': 'rrf', 'rrf_k': 60, 'semantic_limit': 24, 'query_characters': 1200, 'rule_neighborhood': 'same-parent-lettered-family-up-to-32-else-immediate-siblings', 'primary_candidate_limit': 64, 'candidate_limit': 96}
Declared experimental variables: retrieval. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 78.1% | 87.5% | +9.4 percentage points · improved |
| Expected-evidence recall | 75.5% | 77.9% | +2.3 percentage points · improved |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 10.91 | 11.11 | +0.20 · regressed |
| p95 latency (s) | 21.88 | 20.92 | -0.96 · improved |
| Answers with unsupported claims | 5 | 3 | -2.00 · improved |
| Citation-support failures | 10 | 6 | -4.00 · improved |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 25 | 28 | +3.00 · improved |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| h01-apnap / r1 | correct | correct | unchanged |
| h02-intervening-if / r1 | correct | correct | unchanged |
| h03-independent-trigger / r1 | correct | correct | unchanged |
| h04-replacement-death / r1 | correct | correct | unchanged |
| h05-simultaneous-death / r1 | correct | correct | unchanged |
| h06-lifelink-prevented / r1 | correct | correct | unchanged |
| h07-infect-lifelink / r1 | partial | correct | partial → correct |
| h08-protection-wrath / r1 | correct | correct | unchanged |
| h09-protection-aura / r1 | correct | correct | unchanged |
| h10-own-hexproof / r1 | correct | correct | unchanged |
| h11-ward-uncounterable / r1 | correct | correct | unchanged |
| h12-split-second / r1 | correct | correct | unchanged |
| h13-sacrifice-cost / r1 | partial | partial | unchanged |
| h14-flashback-countered / r1 | correct | correct | unchanged |
| h15-rebound-countered / r1 | correct | correct | unchanged |
| h16-persist-counter / r1 | correct | correct | unchanged |
| h17-undying-simultaneous-sba / r1 | correct | correct | unchanged |
| h18-blink-target / r1 | correct | correct | unchanged |
| h19-equip-timing / r1 | correct | correct | unchanged |
| h20-crew-new-creature / r1 | incorrect | correct | incorrect → correct |
| h21-new-vehicle / r1 | correct | correct | unchanged |
| h22-tapped-blocker / r1 | correct | correct | unchanged |
| h23-fight-double-strike / r1 | partial | incorrect | partial → incorrect |
| h24-leaving-controller / r1 | correct | correct | unchanged |
| h25-leaving-stack / r1 | abstained | abstained | unchanged |
| h26-commander-control / r1 | abstained | correct | abstained → correct |
| h27-commander-hand / r1 | correct | correct | unchanged |
| h28-replacement-order / r1 | correct | correct | unchanged |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | correct | correct | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
