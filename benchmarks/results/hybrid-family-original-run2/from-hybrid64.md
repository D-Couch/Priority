# hybrid-original → hybrid-family-original

Implementation `2df6e9b3a650df2d3ac378ca0d7ad3bee538bf5e` → `d55b40a747a4382d9e8aebb4d41c65db85575948`

- `retrieval`: {'mode': 'hybrid', 'model': 'text-embedding-nomic-embed-text-v1.5', 'index_sha256': '75f64df4ff56260946df760cca833ce64e83d6bab54dd1977f2e76ad16d74535', 'index_metadata': {'format': 1, 'model': 'text-embedding-nomic-embed-text-v1.5', 'model_identity': {'key': 'text-embedding-nomic-embed-text-v1.5', 'quantization': {'name': 'Q4_K_M', 'bits_per_weight': 4}, 'size_bytes': 84106624, 'format': 'gguf', 'max_context_length': 2048}, 'rules_sha256': '312e45147b0d2d1a5fa2e1388635230a5394f354c042e73b5cdb0d8cc2eda38a', 'dimensions': 768, 'chunks': 3353, 'rules': 3312, 'build_seconds': 11.376, 'document_prefix': 'search_document: ', 'query_prefix': 'search_query: ', 'chunk_characters': 1200, 'overlap_characters': 200}, 'fusion': 'rrf', 'rrf_k': 60, 'semantic_limit': 24, 'query_characters': 1200} → {'mode': 'hybrid', 'model': 'text-embedding-nomic-embed-text-v1.5', 'index_sha256': '75f64df4ff56260946df760cca833ce64e83d6bab54dd1977f2e76ad16d74535', 'index_metadata': {'format': 1, 'model': 'text-embedding-nomic-embed-text-v1.5', 'model_identity': {'key': 'text-embedding-nomic-embed-text-v1.5', 'quantization': {'name': 'Q4_K_M', 'bits_per_weight': 4}, 'size_bytes': 84106624, 'format': 'gguf', 'max_context_length': 2048}, 'rules_sha256': '312e45147b0d2d1a5fa2e1388635230a5394f354c042e73b5cdb0d8cc2eda38a', 'dimensions': 768, 'chunks': 3353, 'rules': 3312, 'build_seconds': 11.376, 'document_prefix': 'search_document: ', 'query_prefix': 'search_query: ', 'chunk_characters': 1200, 'overlap_characters': 200}, 'fusion': 'rrf', 'rrf_k': 60, 'semantic_limit': 24, 'query_characters': 1200, 'rule_neighborhood': 'same-parent-lettered-family-up-to-32-else-immediate-siblings', 'primary_candidate_limit': 64, 'candidate_limit': 96}
Declared experimental variables: retrieval. All other checked settings remain matched.

| Metric | Before | After | Change |
| --- | --- | --- | --- |
| Reviewed accuracy | 95.0% | 95.0% | +0.0 percentage points · unchanged |
| Expected-evidence recall | 93.8% | 89.6% | -4.2 percentage points · regressed |
| Citation ID validity | 100.0% | 100.0% | +0.0 percentage points · unchanged |
| Median latency (s) | 10.62 | 11.73 | +1.10 · regressed |
| p95 latency (s) | 18.95 | 17.70 | -1.24 · improved |
| Answers with unsupported claims | 1 | 1 | +0.00 · unchanged |
| Citation-support failures | 1 | 1 | +0.00 · unchanged |
| Request errors | 0 | 0 | +0.00 · unchanged |
| Truncated answers | 0 | 0 | +0.00 · unchanged |
| Correct and normally completed | 19 | 19 | +0.00 · unchanged |

| Scenario | Before | After | Change |
| --- | --- | --- | --- |
| 01-mana / r1 | correct | correct | unchanged |
| 02-hold-priority / r1 | correct | correct | unchanged |
| 03-illegal-target / r1 | correct | correct | unchanged |
| 04-partial-targets / r1 | correct | correct | unchanged |
| 05-trample-indestructible / r1 | correct | correct | unchanged |
| 06-deathtouch-trample / r1 | correct | correct | unchanged |
| 07-zero-toughness / r1 | incorrect | incorrect | unchanged |
| 08-commander-dies / r1 | correct | correct | unchanged |
| 09-commander-tax / r1 | correct | correct | unchanged |
| 10-rest-in-peace / r1 | correct | correct | unchanged |
| 11-token-doublers / r1 | correct | correct | unchanged |
| 12-replacement-choice / r1 | correct | correct | unchanged |
| 13-apnap / r1 | correct | correct | unchanged |
| 14-humility-anthem / r1 | correct | correct | unchanged |
| 15-own-hexproof / r1 | correct | correct | unchanged |
| 16-first-strike-blocker / r1 | correct | correct | unchanged |
| 17-token-blink / r1 | correct | correct | unchanged |
| 18-summoning-sacrifice / r1 | correct | correct | unchanged |
| 19-legend-response / r1 | correct | correct | unchanged |
| 20-clarify-interaction / r1 | correct | correct | unchanged |

A single repetition is descriptive, not statistically significant. Use repeated runs on the same machine with no competing inference. Review changed answers and source passages before attributing quality changes to retrieval.
