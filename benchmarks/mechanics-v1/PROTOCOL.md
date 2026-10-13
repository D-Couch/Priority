# Mechanics-v1 evaluation protocol

This 20-case suite covers mechanics not directly tested by gameplay-v1, heldout-v1, or novel-v1, including mana value, loyalty abilities, Battles, monarch, initiative, phasing, regeneration, and spell copies. Scenarios and criteria were frozen before the first inference run. The answering model receives only the user query and card selections, never expected answers, rubric criteria, or reference labels.

The cases and rubrics are AI-authored from the frozen September 25, 2026 Comprehensive Rules snapshot. Their reference passages are hash-checked against the corpus. No Magic judge independently reviewed the scenarios or labels. Scores are exploratory and must not be presented as independently validated accuracy.

Run from the project root with the normal local LM Studio model loaded:

    python3 benchmark.py validate --suite benchmarks/mechanics-v1/scenarios.json
    python3 benchmark.py run --suite benchmarks/mechanics-v1/scenarios.json --label mechanics-v1-seed42 --seed 42 --output benchmarks/results/mechanics-v1-seed42

Review every answer against the scenario criteria and the cited rule text. Record the reviewer and method as AI-assisted. Preserve the first run, including failures and errors. Once answers are inspected, this suite is regression data; create and freeze another untouched suite before using results to support broad claims.
