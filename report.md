# Project Report

## Overview
This repository demonstrates structured extraction for invoices and purchase orders using synthetic supervision and measurable offline evaluation.

## Prompting vs. Fine-Tuning
Prompt engineering improved output cleanliness in targeted cases, but its effect was uneven across varied document layouts. In our experiments, moving from a generic extraction prompt to stricter JSON-only instructions reduced common formatting errors such as markdown wrappers, trailing explanations, and accidental key renaming. This gave meaningful gains on a few difficult examples, especially where the model already identified entities correctly but failed schema compliance. However, prompt-only gains were fragile: small wording shifts or longer inputs caused regression, and success did not generalize consistently across all held-out samples.

Fine-tuning provided a larger and more reliable step change. By training on curated examples with explicit null behavior, mixed currency coverage, and multiple line-item structures, the model learned stronger priors about the target schema. The practical outcome was a major increase in parse success and better field-level completeness, including improved handling of optional fields. While one edge-case failure remained, the failure mode narrowed from widespread format instability to a specific date-normalization issue. That change matters operationally: downstream systems can recover from occasional field errors far more easily than from invalid JSON.

Cost and iteration speed still favor prompting during early exploration, especially for rapid diagnostics. Fine-tuning requires data preparation, quality checks, and training runs, but once evaluation criteria are stable, it produces better consistency under distribution shift. A pragmatic workflow is to prototype with prompts, log persistent error classes, and convert those errors into curated training examples. In this project, that strategy gave both quick wins and robust production-style behavior, with fine-tuning delivering the strongest improvements on reliability metrics.

## Conclusion
Combining prompt iteration with targeted fine-tuning produced high schema adherence and strong held-out performance.
