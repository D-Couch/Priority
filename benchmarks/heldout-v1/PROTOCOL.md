# Held-out baseline and retrieval experiment

The 32 questions, criteria, expected answers and 69 supporting passages were authored by Codex before running the answering model. They use the existing frozen 20260925 Comprehensive Rules and card corpus. No expected answers or rubric fields are passed to inference. This is an AI-authored evaluation, not independent human validation. Once baseline answers are inspected, these cases become regression data; later scores must not be described as held-out accuracy.

Baseline: existing vector-free implementation, seed 42, Qwen 3.8 27B Q4_K_M, medium reasoning, temperature 0.1, output limit 3500, loaded context 8192. Preserve all answers, sources, failures and review notes. Review each criterion and unsupported claims manually with AI assistance against the frozen passages. Citation support is a separate reviewed field: all cited claims must be supported by the cited excerpts; clarification-only responses need no citations. Appropriate clarification is not abstention.

After baseline, classify failures as retrieval, packing, reasoning, clarification or presentation. Make each substantive fix a separate implementation commit, followed by both suite runs and a results commit. Do not change criteria after seeing answers. Any discovered rubric defect needs an explicit addendum rather than silently changing historical grades.

Vector experiment: keep generation settings and corpus fixed. Embed rule passages locally using the installed Nomic Embed Text v1.5; preserve exact Oracle attachment lookup. Compare hybrid lexical/semantic retrieval with the latest lexical configuration on BOTH suites at seed 42. Store model/index identity and measure index size/build time, retrieval time, end-to-end latency, correctness, unsupported claims and citation support. No benchmark labels are used to build the index.

Adoption gate: hybrid must improve correct-and-complete answers on the 52-case combined set, introduce no new unsupported answers, and keep median end-to-end latency within 20% of lexical on each suite. A passing result requires another matched seed before enabling it by default. If it fails, retain the experimental option with lexical as default and document the tradeoff. Single runs are descriptive, not statistical proof. Do not tune embeddings to these labels during this experiment.

## Reviewed prompt experiment

The source-quotation response contract was committed and measured on both frozen suites. It remained 25/32 on held-out and 20/20 on original, improved citation-support reviews 10→9, but produced new unsupported details and increased held-out p95 from 18.79s to 28.99s. It was reverted; artifacts and comparison are retained under `results/source-quotes-*`.

## First hybrid result and targeted follow-up

The first hybrid run (RRF k=60, 24 semantic candidates, 64-rule cap) improved the held-out set to 29/32 but regressed the original suite to 19/20. In both suites it newly claimed a 0/0 indestructible creature with no damage survives. Candidate sources contained CR 704.5g but omitted adjacent CR 704.5f, which governs zero toughness. The run therefore fails the no-new-unsupported-answers gate and hybrid is not enabled by default. A separately committed retrieval fix will keep adjacent lettered subrules with a selected subrule, then repeat both suites against the unchanged frozen baselines. Historical first-run artifacts remain immutable.

A second hybrid iteration placed immediate siblings directly into the ranked list before applying the 64-candidate cap. It reduced held-out accuracy 29/32→28/32 and displaced CR 701.14 from the fight question, causing a new double-strike/fight error. The original remained 19/20 with the zero-toughness error. This iteration is also rejected. A further committed implementation will retain the original top-ranked candidate set intact, append related clauses afterward, and retest both frozen suites.
