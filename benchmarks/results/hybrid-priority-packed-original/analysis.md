# Lexical-preserving hybrid: original-suite result

At seed 42, the original 20-case suite scored 20/20 fully correct, matching the lexical baseline. There were no unsupported claims, semantic citation failures, request errors, or truncated answers. Mean expected-evidence recall was 96.25%; median latency was 10.73 s versus 10.27 s lexical (+4.5%), and p95 was 16.82 s versus 17.03 s. The 0/0 edge case is now correct: CR 704.5f was present in the packed prompt and cited, explaining why indestructible does not stop the toughness-zero state-based action.

Together with the held-out result, the combined score is 48/52 versus lexical's 45/52, with no new unsupported answers and median latency within the 20% per-suite limit. The predeclared gate passes once, but default adoption requires a second matched seed on both suites. Reviews are AI-assisted, not independent human rulings.
