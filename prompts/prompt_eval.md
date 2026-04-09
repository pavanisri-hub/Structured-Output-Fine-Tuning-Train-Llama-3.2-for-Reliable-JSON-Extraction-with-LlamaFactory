# Prompt Evaluation on 3 Worst Baseline Docs

| Doc ID | Prompt v1 parse success | Prompt v2 parse success | Prompt v3 parse success | Notes |
|---|---:|---:|---:|---|
| E05 | 0 | 0 | 1 | v3 removed trailing explanation text |
| E11 | 0 | 1 | 1 | stronger schema instruction fixed missing key |
| E18 | 0 | 0 | 1 | explicit null handling improved validity |

Prompting helps, but improvements remained less stable than fine-tuning across all 20 held-out documents.
