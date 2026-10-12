# Held-out baseline and retrieval experiment

The 32 questions, criteria, expected answers and 69 supporting passages were authored by Codex before running the answering model. They use the existing frozen 20260925 Comprehensive Rules and card corpus. No expected answers or rubric fields are passed to inference. This is an AI-authored evaluation, not independent human validation. Once baseline answers are inspected, these cases become regression data; later scores must not be described as held-out accuracy.

Baseline: existing vector-free implementation, seed 42, Qwen 3.8 27B Q4_K_M, medium reasoning, temperature 0.1, output limit 3500, loaded context 8192. Preserve all answers, sources, failures and review notes. Review each criterion and unsupported claims manually with AI assistance against the frozen passages. Citation support is a separate reviewed field: all cited claims must be supported by the cited excerpts; clarification-only responses need no citations. Appropriate clarification is not abstention.

After baseline, classify failures as retrieval, packing, reasoning, clarification or presentation. Make each substantive fix a separate implementation commit, followed by both suite runs and a results commit. Do not change criteria after seeing answers. Any discovered rubric defect needs an explicit addendum rather than silently changing historical grades.

Vector experiment: keep generation settings and corpus fixed. Embed rule passages locally using the installed Nomic Embed Text v1.5; preserve exact Oracle attachment lookup. Compare hybrid lexical/semantic retrieval with the latest lexical configuration on BOTH suites at seed 42. Store model/index identity and measure index size/build time, retrieval time, end-to-end latency, correctness, unsupported claims and citation support. No benchmark labels are used to build the index.

Adoption gate: hybrid must improve correct-and-complete answers on the 52-case combined set, introduce no new unsupported answers, and keep median end-to-end latency within 20% of lexical on each suite. A passing result requires another matched seed before enabling it by default. If it fails, retain the experimental option with lexical as default and document the tradeoff. Single runs are descriptive, not statistical proof. Do not tune embeddings to these labels during this experiment.

## Reviewed prompt experiment

The source-quotation response contract was committed and measured on both frozen suites. It remained 25/32 on held-out and 20/20 on original, improved citation-support reviews 10→9, but produced new unsupported details and increased held-out p95 from 18.79s to 28.99s. It was reverted; artifacts and comparison are retained under `results/source-quotes-*`.
