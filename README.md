# Multi-Task Learning with Gradient Surgery (PCGrad)

This project implements a TensorFlow multi-task learning (MTL) system with a custom training loop and PCGrad-style gradient surgery to mitigate gradient conflicts between two competing tasks.

## What This Repository Includes
- `generate_model_summary.py`: prints and saves architecture summaries.
- `train_baseline.py`: trains baseline MTL with naive loss summation.
- `train_pcgrad.py`: trains MTL with PCGrad and logs gradient cosine similarity.
- `app.py`: Streamlit dashboard for conflict monitoring, performance comparison, and representation inspection.
- `mtl/`: reusable model, data generation, config, and utility functions.
- `results/`: generated outputs required by the rubric.
- `Dockerfile` and `docker-compose.yml`: containerized Streamlit service.
- `.env.example`: environment variable contract.

## Local Setup
```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

## Run Training and Artifact Generation
```bash
python generate_model_summary.py
python train_baseline.py
python train_pcgrad.py
```

Required outputs are generated in `results/`:
- `model_architecture.txt`
- `baseline_metrics.csv`
- `pcgrad_metrics.csv`
- `gradient_conflict.csv`
- `final_metrics.json`
- `analysis.md`
- `representation_projection.csv`

## Launch Dashboard Locally
```bash
streamlit run app.py --server.port 8501
```

## Dockerized Run (Single Command)
1. Copy env template once:
```bash
cp .env.example .env
```

2. Launch:
```bash
docker compose up --build
```

3. Open dashboard:
`http://localhost:8501`

## Streamlit Test IDs
The app includes required test hooks:
- `data-testid="gradient-conflict-monitor"`
- `data-testid="performance-dashboard"`
- `data-testid="representation-inspector"`
