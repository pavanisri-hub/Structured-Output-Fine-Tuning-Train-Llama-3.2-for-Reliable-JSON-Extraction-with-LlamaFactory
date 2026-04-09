# Invoice Schema

Every invoice training example must produce a single JSON object with the same keys in the same shape.

## Required Keys
- `vendor`: The legal vendor or supplier name as it appears on the source document; use a string, and use an empty string only if the source document is unreadable enough that the example should be rejected.
- `invoice_number`: The invoice identifier or billing reference; use a string, preserving leading zeros and punctuation.
- `date`: The invoice issue date in `YYYY-MM-DD` format; if the source only gives a partial or ambiguous date, reject the example instead of guessing.
- `due_date`: The payment due date in `YYYY-MM-DD` format; use `null` when the document does not state a due date.
- `currency`: The three-letter ISO currency code such as `USD`, `EUR`, `GBP`, `INR`, or `JPY`; always use uppercase text.
- `subtotal`: The pre-tax subtotal as a number; do not store it as a string.
- `tax`: The tax amount as a number; use `null` when tax is absent or not explicitly stated.
- `total`: The final payable amount as a number; do not invent discounts or freight unless they are explicitly present in the document.
- `line_items`: An array of line-item objects in document order; each object must contain `description`, `quantity`, and `unit_price`.

## Line-Item Rules
- `description`: The item description as a string; preserve the wording from the document.
- `quantity`: The quantity as a number; use a numeric type rather than a string.
- `unit_price`: The unit price as a number; use a numeric type rather than a string.

## Missing-Field Policy
- Use `null` for `due_date` and `tax` when the source document does not explicitly provide them.
- Keep all required keys present in every output object, even when a value is `null`.
- Reject ambiguous examples rather than guessing missing values.
