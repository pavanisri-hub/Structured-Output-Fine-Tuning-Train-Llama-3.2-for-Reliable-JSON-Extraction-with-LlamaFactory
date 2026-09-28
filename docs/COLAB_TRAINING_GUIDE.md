# Google Colab Fine-Tuning Guide (Fastest)

This guide provides a copy-paste workflow for fine-tuning **Llama 3.2 3B** using the provided dataset on a free Google Colab GPU.

## Step 1: Open Google Colab
1. Go to [colab.google](https://colab.google).
2. Create a new notebook.
3. Go to **Runtime > Change runtime type** and select **T4 GPU**.

## Step 2: Environment Setup
Paste and run this in the first cell:
```bash
%cd /content/
# 1. Clone LlamaFactory
!git clone https://github.com/hiyouga/LLaMA-Factory.git
%cd LLaMA-Factory
!pip install -e ".[torch,metrics]"

# 2. Clone YOUR repository to get the data
%cd /content/
!git clone https://github.com/Surya2004-janardhan/Structured-Output-Fine-Tuning-Train-Llama-3.2-for-Reliable-JSON-Extraction-with-LlamaFactory.git
```

## Step 3: Register Your Data
Paste and run this in the second cell:
```python
import json
import os

# 1. Copy our curated data into the LlamaFactory folder
!cp /content/Structured-Output-Fine-Tuning-Train-Llama-3.2-for-Reliable-JSON-Extraction-with-LlamaFactory/data/curated_train.jsonl /content/LLaMA-Factory/data/curated_train.jsonl

# 2. Add the dataset entry to LlamaFactory's registry
info_path = "/content/LLaMA-Factory/data/dataset_info.json"

with open(info_path, "r") as f:
    df_info = json.load(f)

df_info["invoice_po_curated"] = {
    "file_name": "curated_train.jsonl",
    "columns": {
        "prompt": "instruction",
        "query": "input",
        "response": "output"
    }
}

with open(info_path, "w") as f:
    json.dump(df_info, f, indent=2)

print("Dataset 'invoice_po_curated' successfully registered!")
```

## Step 4: Start the Web UI
Paste and run this in the third cell:
```bash
%cd /content/LLaMA-Factory/
!llamafactory-cli webui --share
```
1. Click the **"Public URL"** (ending in `.gradio.live`) that appears in the output.
2. In the Web UI:
## Step 1.5: Authenticate (Compulsory for Llama 3.2)
Since Llama 3.2 is a gated model, you **MUST** provide your Hugging Face token.
1. Run this in a new cell:
   ```python
   from huggingface_hub import login
   login()
   ```
2. Paste your token (with "Gated Repository Read" permissions) when prompted.

   - **Model Name**: Select `Llama-3.2-3B-Instruct`.
   - **Dataset**: Check `invoice_po_curated`.
   - **Adapter**: Set LoRA (Rank 16, Alpha 32).
   - **Training**: Click "Start".

## Step 5: Save Your Weights
Once training hits 100%, go to the **"Export"** tab in the Web UI:
1. Export the model to `/content/finetuned_llama`.
2. Zip and download it to your local machine:
   ```bash
   !zip -r finetuned_llama.zip /content/finetuned_llama
   ```

---
**Why not push LLaMA-Factory to Git?**
- **Size**: LlamaFactory is a massive repository with large dependencies.
- **Workflow**: It is standard practice to `git clone` the tool and then "inject" your data into it (as shown above). Pushing the whole tool would make your repo slow and cluttered.
