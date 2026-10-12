# Priority — local Magic rules assistant

A React chat interface backed by Python and your existing LM Studio model. Everything needed to run the app is included, including React and a local SQLite knowledge database. No Node, npm, pip, account, or cloud inference is needed.

## Run

1. Open LM Studio, load `qwen/qwen3.8-27b`, and start its local server on port **1234**.
2. In this folder, run:

   ```bash
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

If LM Studio reports a context-length error, increase its loaded context to 16K or higher and retry. Long attached card text/rulings can require a larger context. If responses are slow, reduce model reasoning in LM Studio. The assistant displays final answer content and suppresses reasoning fields/tags.

## Development

- `static/app.js`, `static/style.css`: React interface, using HTM templates with no compilation step.
- `server.py`: loopback HTTP server and streaming LM Studio adapter.
- `knowledge.py`: atomic source downloads, parsing, and retrieval.
- `data/knowledge.sqlite`: current rules/card/ruling snapshot.
- `test_app.py`: parser and retrieval regression checks.

Run checks with `python3 -m unittest -v`. Update the database from the terminal with `python3 knowledge.py`. Python 3.10+ with SQLite FTS5 support is required.

Frontend libraries: React/ReactDOM 18.3.1 and HTM 3.1.1, distributed under MIT licenses. Library license files are in `static/vendor/`. Magic content belongs to its respective rights holders. This is an unofficial personal project.
