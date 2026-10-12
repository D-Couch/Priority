# Structural retrieval: more evidence, insufficient output space

The frozen rubric improves from 16/20 to 18/20, but this is **not** a release-quality 18/20. Cases 08, 10, and 11 exhaust the loaded 8,192-token context and end mid-answer. Cases 10 and 11 satisfy both substantive rubric criteria before truncation; only **16/20 are both rubric-correct and normally completed**. Historical rubric grades are preserved rather than silently redefined.

Retrieval recall rises from 63.33% to 96.25%, with all reference groups present in 18 cases. Priority, zero toughness, and token blink are repaired. The commander response regresses because evidence crowds out generation. The underspecified protection answer still adds an overbroad claim about non-targeted effects.

Next isolated changes: reserve the configured output budget using actual model tokenization; measure evidence after packing rather than before; distinguish truncated answers from normal completion; then make missing-detail responses concise and conditional. Run all 20 cases for each behavior change. These are development-suite results: structural candidate choices were explored against this suite, so an unseen suite is still required before generalization claims.
