FROM python:3.10-slim

WORKDIR /app

# This project uses Python stdlib only for API + validation.
COPY api ./api
COPY data ./data
COPY eval ./eval
COPY scripts ./scripts
COPY schema ./schema
COPY prompts ./prompts
COPY README.md ./README.md
COPY training_config.md ./training_config.md
COPY report.md ./report.md

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HOST=0.0.0.0
ENV PORT=8787

EXPOSE 8787

CMD ["python", "api/server.py"]
