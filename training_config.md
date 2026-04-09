# Training Configuration

## Chosen Hyperparameters
- Base model: Llama 3.2 (instruction variant)
- Method: LoRA fine-tuning
- Learning rate: 2e-4
- Batch size: 8
- Gradient accumulation: 4
- Epochs: 3
- Max sequence length: 2048
- LoRA rank: 16
- LoRA alpha: 32
- LoRA dropout: 0.05
- Warmup ratio: 0.03
- Scheduler: cosine
- Weight decay: 0.01

## Run Log and Loss-Curve Narrative
### Run A
- Setup: LR 3e-4, LoRA dropout 0.1
- Observation: Fast initial loss drop, then oscillation after ~35% of steps.
- Result: Better than baseline but unstable validation parse success.

### Run B (selected)
- Setup: LR 2e-4, LoRA dropout 0.05, same effective batch.
- Observation: Smoother monotonic training loss and improved validation consistency.
- Result: Selected checkpoint due to higher parse success and fewer schema violations.

Across both runs, the final selected configuration traded slightly slower convergence for markedly better output validity on held-out documents.
