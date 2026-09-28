# Project Explanation: Top-to-Bottom Workflow

This document provides a comprehensive walkthrough of the technical methodology and filename-level details of this project.

## 1. Project Objective
The goal was to solve the **Reliability Problem** in LLM-based data extraction. General LLMs (like the base Llama 3.2) often return prose, markdown fences, or inconsistent keys. Fine-tuning with LoRA converts these "formatting preferences" into "hard constraints".

## 2. Methodology: How We Did It All
We used **Supervised Fine-Tuning (SFT)**. By presenting the model with examples where the *only* correct behavior is responding with a specific JSON object, we trained the model to treat JSON as its native language for this task.

## 3. File-by-File Breakdown

### Core Infrastructure
- **`schema/invoice_schema.md` & `schema/po_schema.md`**: These define the "Ground Truth". Every training example and evaluation check was validated against these strict structures.
- **`data/curated_train.jsonl`**: The training set. It contains 80 input-output pairs where the input is raw text and the output is the cleaned JSON.
- **`data/curation_log.md`**: A detailed audit trail of how we selected and cleaned the training data.

### Training & Configuration
- **`docs/training_config.md`**: The technical "recipe". It explains why we chose **Rank 16** and **Alpha 32** for LoRA, and how we balanced learning speed vs. model stability.
- **`docs/plan.md`**: The original 5-phase execution strategy used to build this project from scratch.

### Deployment Guides
- **`docs/HOW_TO_FINE_TUNE.md`**: Instructions for running the LlamaFactory Web UI on a local machine with a GPU.
- **`docs/COLAB_TRAINING_GUIDE.md`**: A specialized guide for **Google Colab** that includes exact code cells for environment setup, data registration, and model uploading.

### Evaluation & Proof
- **`eval/summary.md`**: The final scorecard showing the jump from **0% to 100% success**.
- **`eval/baseline_responses.md`**: Logs showing the failures of the un-tuned model.
- **`eval/finetuned_responses.md`**: Logs showing the perfect, clean JSON outputs from our fine-tuned Llama 3.2.
- **`screenshots/loss_curve.png`**: Visual proof that the model successfully converged during training.
- **`screenshots/success_chat.png`**: A screenshot showing the model passing a real-time manual test.

### Final Reports
- **`README.md`**: The professional entry point and visual gallery of the project.
- **`report.md`**: A strategic analysis of the ROI (Return on Investment) of using Fine-Tuning versus simple Prompt Engineering.

## 4. Technical Flow
1. **Define Schema** -> 2. **Curate Data** -> 3. **Establish Baseline (Failure)** -> 4. **Fine-Tune (Llama 3.2 + LoRA)** -> 5. **Verify (Success)**.
