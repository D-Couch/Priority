# CR 800.4a topic-retrieval experiment

Implementation under test: `faa875bda30d5d5965bdcb0cf630872b89625778` (`fix: retrieve multiplayer leaving-game rule`). The rule-topic pattern matched “leaves the game” and related forms, but the frozen h25 wording is “Bob loses and leaves before Bolt resolves.” The pattern did not match, so CR 800.4a was absent from both candidate and packed evidence. The answer remained an unnecessary abstention with an unsupported section suggestion. This implementation change did not fix the target failure.

The complete 32-case inference run had no request errors or truncations. Accuracy and unsupported-claim totals remain unreviewed; history correctly shows them as pending. Evidence recall was 77.1%, median latency 10.17 s, p95 17.38 s. These descriptive measurements are not an accuracy comparison.

Reviewer: Codex, inspected the h25 answer and evidence only; no independent human judge. Full answer-set review remains pending.
