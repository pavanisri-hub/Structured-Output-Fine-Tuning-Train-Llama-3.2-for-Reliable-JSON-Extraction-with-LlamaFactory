# Failure 01 - E05

## Source document text
Synthetic document E05 includes mixed date notation, subtotal lines, and footer comments.

## Expected JSON
```json
{"document_type":"invoice","id":"E05","currency":"USD","total":1234.56}
```

## Model actual output
```text
Here is the extracted JSON: {"document_type":"invoice","id":"E05"} Additional explanation...
```

## What went wrong
The response wrapped JSON with extra natural-language text and omitted one required numeric field.

## Why it likely failed
Training exposure to noisy OCR-like text was insufficient for this layout pattern.

## What training data change would fix it
Add more examples with footer chatter and strict JSON-only targets for ambiguous totals.
