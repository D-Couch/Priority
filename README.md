# Priority — local Magic rules assistant

A React chat interface backed by Python and your existing LM Studio model. React and a frozen SQLite knowledge snapshot are included. Setup installs a Python client for local LM Studio tokenization. No Node, npm, account, or cloud inference is needed; inference and tokenization stay on your computer.

## Run

1. Open LM Studio, load `qwen/qwen3.8-27b`, and start its local server on port **1234**.
2. In this folder, run:

   ```bash
   ./setup.sh  # once; downloads Python dependencies
   ./start.sh
   ```

3. Open **http://127.0.0.1:8088** in your browser. Keep the terminal open; Ctrl+C stops the app.

To use another port, run `./start.sh --port 8090`.

## Ask a question

Describe the game state, whose turn it is, and what has already happened. Use **Attach cards** to search and select up to eight exact cards. You can also write `[[Lightning Bolt]]` in a question. Full multiword card names with matching capitalization are detected automatically; attach cards to avoid ambiguity.

The model streams a ruling and citations. Click a citation to read the actual retrieved rule, Oracle text, or card ruling. “Retrieved references” shows all supplied context, including material the model did not cite. A matching citation establishes that the source exists, not that the answer interpreted it correctly.

Conversations are saved in this browser's local storage. Reloading preserves them; deleting a conversation removes its local copy. LM Studio may independently retain logs according to its settings. Opening external source links uses the internet.

## Knowledge and updates

The included database contains the September 25, 2026 Comprehensive Rules and Scryfall card/ruling data dated October 11, 2026. The sidebar displays its versions. **Update knowledge** downloads the current official rules and Scryfall bulk files; updates are manual. The previous database remains usable if a download or validation fails. Normal chat and card search require no internet connection.

Sources:

- [Wizards Comprehensive Rules](https://magic.wizards.com/en/rules)
- [Scryfall bulk card data and rulings](https://scryfall.com/docs/api/bulk-data)
- [LM Studio chat API](https://lmstudio.ai/docs/developer/openai-compat/chat-completions)

Retrieval uses local SQLite full-text search, topic expansion, exact card matching, and related rule definitions. It does not currently use embeddings or fine-tuning. The included tests cover several common interactions; this is an initial working assistant, not a comprehensive rules engine. Complex layers and interacting replacement effects still need careful source checking. Tournament policy is outside scope.

## Configuration

Optional environment variables:

```bash
LM_STUDIO_MODEL='qwen/qwen3.8-27b' ./start.sh
LM_STUDIO_URL='http://127.0.0.1:1234/v1' ./start.sh
```

If LM Studio requires authentication, set `LM_STUDIO_API_KEY` in your environment. The app does not store it in the browser or source files. The model URL must use a loopback address. The app binds only to `127.0.0.1` and rejects nonlocal Host/Origin headers. Leave LM Studio's CORS setting off; the Python backend makes model requests.

The backend measures the formatted prompt using the loaded model tokenizer and reserves 3,500 output tokens plus a template margin. It keeps complete excerpts, prioritizes Oracle text and related rule clauses over dated rulings, and omits older turns when necessary (with a warning). An oversized latest question is rejected before generation. The current local SDK tokenization connection requires access to LM Studio’s SDK endpoint; HTTP-only gateways are not supported. The default reasoning effort is medium; set `MTG_REASONING_EFFORT` to `off`, `low`, `medium`, `high`, `xhigh`, or `on` to override it. The backend translates `off` to `none` and `on` to `xhigh` for LM Studio’s OpenAI-compatible API. The benchmark history records the tested quality and latency for each effort. The assistant displays final answer content and suppresses reasoning fields/tags.

## Development

- `static/app.js`, `static/style.css`: React interface, using HTM templates with no compilation step.
- `server.py`: loopback HTTP server and streaming LM Studio adapter.
- `knowledge.py`: atomic source downloads, parsing, and retrieval.
- `data/knowledge.sqlite`: current rules/card/ruling snapshot.
- `test_app.py`: parser and retrieval regression checks.

Run checks with `.venv/bin/python -m unittest -v`. Run inference benchmarks with `.venv/bin/python benchmark.py run ...`. Update the database from the terminal with `python3 knowledge.py`. Python 3.11+ with SQLite FTS5 support is required.

Frontend libraries: React/ReactDOM 18.3.1 and HTM 3.1.1, distributed under MIT licenses. Library license files are in `static/vendor/`. Magic content belongs to its respective rights holders. This is an unofficial personal project.

## Benchmark history

The project includes 20 gameplay scenarios, a frozen corpus, an end-to-end benchmark runner, and attributed answer reviews. See [benchmark instructions](benchmarks/README.md) and [performance history](benchmarks/HISTORY.md). Each report records the exact implementation commit, source/data hashes, model settings, retrieved passages, answers, quality grades, and latency. Future vector-search changes should have separate implementation and results commits.

The improved, still vector-free configuration scored **20/20 correct and complete at each of seeds 42 and 43** (40 answers on the same 20 scenarios), versus 12/20 in the original baseline. Median response times were 10.21 and 9.95 seconds; neither verification run contained an empty or truncated answer. Reviews are AI-assisted, not independently human-validated. One seed-42 answer uses plain rule numbers instead of clickable bracketed citations. This is a development-suite result, not an accuracy claim for unseen questions. See the [second-seed findings](benchmarks/results/atomic-sections-seed43/findings.md).

The original tags are preserved. `pre-vectorization-quality` marks this improved baseline; freeze unseen scenarios and paraphrases before evaluating vectorization against it. Restart an already-running backend with `./start.sh` to load the changes.

For a fresh Git clone, restore the included database before starting the app:

```bash
python3 benchmark.py restore-corpus --output data/knowledge.sqlite
```

Then run `./start.sh` as above. No model weights, API credentials, or personal chat history are included in the repository.
