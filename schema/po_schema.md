# Purchase Order Schema

Every purchase order training example must produce a single JSON object with the same keys in the same shape.

## Required Keys
- `buyer`: The purchasing organization name as written on the purchase order; use a string.
- `supplier`: The vendor or supplier name as written on the purchase order; use a string.
- `po_number`: The purchase order identifier; use a string and preserve leading zeros and hyphens.
- `date`: The order date in `YYYY-MM-DD` format; reject the example if the date cannot be normalized confidently.
- `delivery_date`: The expected delivery date in `YYYY-MM-DD` format; use `null` when the document does not state one.
- `currency`: The three-letter ISO currency code; always use uppercase text.
- `total`: The order total as a number; do not quote it as text.
- `items`: An array of item objects in document order; each object must contain `item_name`, `quantity`, and `unit_price`.

## Item Rules
- `item_name`: The ordered product or service name as a string.
- `quantity`: The ordered quantity as a number.
- `unit_price`: The unit price as a number.

## Missing-Field Policy
- Use `null` for `delivery_date` when the source document does not explicitly provide it.
- Keep all required keys present in every output object, even when a value is `null`.
- Reject ambiguous examples rather than guessing missing values.
