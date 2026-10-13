# General rules questions v2

This frozen five-case suite tests whether Priority answers broad conceptual Magic rules questions directly and accurately. It covers paper randomization and legal random targets, copiable values, fight damage versus double strike, and replacement-effect order.

The scenarios, expected answers, criteria, and reference passages were fixed before inference. The questions intentionally omit exact card names where the general rule suffices. A useful conditional or general answer should not be graded as an abstention merely because it does not request more details. If exact text can change a result, the answer should give the general rule first and invite details only as a follow-up.

The suite and rubric are AI-authored and are not independent judge validation. It is a regression check for this product behavior, not an estimate of accuracy on unseen user queries. The MTR 3.9 excerpt is limited to game actions that use a die roll; it is not presented as a comprehensive rule for every random effect.

Run validation and inference from the repository root:

```bash
.venv/bin/python benchmark.py validate --suite benchmarks/general-questions-v2/scenarios.json
.venv/bin/python benchmark.py run --suite benchmarks/general-questions-v2/scenarios.json --label general-questions-v2-seed42 --output benchmarks/results/general-questions-v2-seed42
```
