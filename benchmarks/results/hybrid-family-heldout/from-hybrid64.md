# hybrid-heldout → hybrid-family-heldout

Implementation `2df6e9b3a650df2d3ac378ca0d7ad3bee538bf5e` → `d55b40a747a4382d9e8aebb4d41c65db85575948`

- `retrieval`: {'mode': 'hybrid', 'model': 'text-embedding-nomic-embed-text-v1.5', 'index_sha256': '75f64df4ff56260946df760cca833ce64e83d6bab54dd1977f2e76ad16d74535', 'index_metadata': {'format': 1, 'model': 'text-embedding-nomic-embed-text-v1.5', 'model_identity': {'key': 'text-embedding-nomic-embed-text-v1.5', 'quantization': {'name': 'Q4_K_M', 'bits_per_weight': 4}, 'size_bytes': 84106624, 'format': 'gguf', 'max_context_length': 2048}, 'rules_sha256': '312e45147b0d2d1a5fa2e1388635230a5394f354c042e73b5cdb0d8cc2eda38a', 'dimensions': 768, 'chunks': 3353, 'rules': 3312, 'build_seconds': 11.376, 'document_prefix': 'search_document: ', 'query_prefix': 'search_query: ', 'chunk_characters': 1200, 'overlap_characters': 200}, 'fusion': 'rrf', 'rrf_k': 60, 'semantic_limit': 24, 'query_characters': 1200} → {'mode': 'hybrid', 'model': 'text-embedding-nomic-embed-text-v1.5', 'index_sha256': '75f64df4ff56260946df760cca833ce64e83d6bab54dd1977f2e76ad16d74535', 'index_metadata': {'format': 1, 'model': 'text-embedding-nomic-embed-text-v1.5', 'model_identity': {'key': 'text-embedding-nomic-embed-text-v1.5', 'quantization': {'name': 'Q4_K_M', 'bits_per_weight': 4}, 'size_bytes': 84106624, 'format': 'gguf', 'max_context_length': 2048}, 'rules_sha256': '312e45147b0d2d1a5fa2e1388635230a5394f354c042e73b5cdb0d8cc2eda38a', 'dimensions': 768, 'chunks': 3353, 'rules': 3312, 'build_seconds': 11.376, 'document_prefix': 'search_document: ', 'query_prefix': 'search_query: ', 'chunk_characters': 1200, 'overlap_characters': 200}, 'fusion': 'rrf', 'rrf_k': 60, 'semantic_limit': 24, 'query_characters': 1200, 'rule_neighborhood': 'same-parent-lettered-family-up-to-32-else-immediate-siblings', 'primary_candidate_limit': 64, 'candidate_limit': 96}
Declared experimental variables: retrieval. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 90.6% | 87.5% | -3.1 percentage points · regressed |
| Expected-evidence recall | 81.0% | 77.9% | -3.1 percentage points · regressed |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 10.69 | 11.11 | +0.42 · regressed |
| p95 latency (s) | 18.44 | 20.92 | +2.48 · regressed |
| Answers with unsupported claims | 2 | 3 | +1.00 · regressed |
| Citation-support failures | 6 | 6 | +0.00 · unchanged |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 29 | 28 | -1.00 · regressed |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| h01-apnap / r1 | correct | correct | unchanged |
| h02-intervening-if / r1 | correct | correct | unchanged |
| h03-independent-trigger / r1 | correct | correct | unchanged |
| h04-replacement-death / r1 | correct | correct | unchanged |
| h05-simultaneous-death / r1 | correct | correct | unchanged |
| h06-lifelink-prevented / r1 | correct | correct | unchanged |
| h07-infect-lifelink / r1 | correct | correct | unchanged |
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
| h20-crew-new-creature / r1 | correct | correct | unchanged |
| h21-new-vehicle / r1 | correct | correct | unchanged |
| h22-tapped-blocker / r1 | correct | correct | unchanged |
| h23-fight-double-strike / r1 | correct | incorrect | correct → incorrect |
| h24-leaving-controller / r1 | correct | correct | unchanged |
| h25-leaving-stack / r1 | abstained | abstained | unchanged |
| h26-commander-control / r1 | correct | correct | unchanged |
| h27-commander-hand / r1 | correct | correct | unchanged |
| h28-replacement-order / r1 | correct | correct | unchanged |
| h29-empty-library / r1 | correct | correct | unchanged |
| h30-ambiguous-combat / r1 | correct | correct | unchanged |
| h31-ambiguous-copy / r1 | incorrect | incorrect | unchanged |
| h32-ambiguous-replacements / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
