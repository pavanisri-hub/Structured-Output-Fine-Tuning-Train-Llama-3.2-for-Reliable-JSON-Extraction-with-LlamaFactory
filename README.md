# Structured Output Fine-Tuning Artifacts

## Methodology
1. Curated 80 high-quality JSONL training samples (50 invoices, 30 purchase orders) with schema-consistent outputs.
2. Tracked candidate review decisions in a curation log (80 kept + 8 rejected).
3. Evaluated baseline and fine-tuned checkpoints on 20 held-out documents.
4. Compared prompt iterations against difficult baseline failures.
5. Documented failure analyses and training decisions.

## Repository Structure
- `data/` curated dataset and curation log.
- `eval/` response dumps, score CSVs, summary comparison, and failure deep-dives.
- `prompts/` prompt iteration history and prompt-level evaluation.
- `screenshots/` generated PNG placeholders for config and loss curve visuals.
- `scripts/validate_project.py` automated validator and JSONL schema normalizer.
- `api/server.py` lightweight local endpoint server for health and project status checks.
- `training_config.md` selected hyperparameters and two-run narrative.
- `report.md` project analysis, including Prompting vs. Fine-Tuning.

## Key Outcomes
- Baseline parse success: 11/20 (55%)
- Fine-tuned parse success: 19/20 (95%)
- Absolute parse-success gain: +40 percentage points
- Field-level quality also improved, with fewer schema-format failures.

## How To Validate Everything
Run from repository root:

```
".venv/Scripts/python.exe" scripts/validate_project.py
```

If you need to re-normalize `data/curated_train.jsonl` to the schema keys:

```
".venv/Scripts/python.exe" scripts/validate_project.py --fix-jsonl
```

## Local Endpoints
Start server:

```
".venv/Scripts/python.exe" api/server.py
```

Available endpoints:
- `GET /health`
- `GET /endpoints`
- `GET /project/status`

## Docker
Build and run with Docker Compose:

```bash
docker compose up --build
```

Then test:

```bash
curl http://127.0.0.1:8787/health
curl http://127.0.0.1:8787/project/status
```

Stop containers:

```bash
docker compose down
```

Run validation in a container (one-off):

```bash
docker build -t structured-output-finetuning .
docker run --rm structured-output-finetuning python scripts/validate_project.py
```
