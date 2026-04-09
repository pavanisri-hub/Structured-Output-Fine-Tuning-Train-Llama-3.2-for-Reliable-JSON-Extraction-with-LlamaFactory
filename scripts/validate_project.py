import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = REPO_ROOT / "data" / "curated_train.jsonl"
BASELINE_CSV = REPO_ROOT / "eval" / "baseline_scores.csv"
FINETUNED_CSV = REPO_ROOT / "eval" / "finetuned_scores.csv"

INVOICE_REQUIRED = {
    "vendor",
    "invoice_number",
    "date",
    "due_date",
    "currency",
    "subtotal",
    "tax",
    "total",
    "line_items",
}

PO_REQUIRED = {
    "buyer",
    "supplier",
    "po_number",
    "date",
    "delivery_date",
    "currency",
    "total",
    "items",
}

CSV_REQUIRED_HEADERS = [
    "filename",
    "raw_output_first_50_chars",
    "is_valid_json",
    "has_all_required_keys",
    "key_accuracy",
    "value_accuracy",
    "notes",
]


def _extract_field(text: str, field_name: str) -> str | None:
    pattern = rf"^{re.escape(field_name)}:\s*(.+)$"
    for line in text.splitlines():
        match = re.match(pattern, line.strip(), flags=re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return None


def _to_number(value: Any, default: float = 0.0) -> float:
    if value is None:
        return default
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        normalized = value.replace(",", "").strip()
        try:
            return float(normalized)
        except ValueError:
            return default
    return default


def transform_invoice(payload: dict[str, Any]) -> dict[str, Any]:
    line_items = payload.get("line_items", [])
    transformed_items = []
    for item in line_items:
        transformed_items.append(
            {
                "description": str(item.get("description", "")).strip(),
                "quantity": _to_number(item.get("quantity")),
                "unit_price": _to_number(item.get("unit_price")),
            }
        )

    transformed = {
        "vendor": str(payload.get("vendor", "")).strip(),
        "invoice_number": str(payload.get("invoice_number") or payload.get("invoice_id") or "").strip(),
        "date": str(payload.get("date") or payload.get("invoice_date") or "").strip(),
        "due_date": payload.get("due_date", None),
        "currency": str(payload.get("currency", "")).strip().upper(),
        "subtotal": _to_number(payload.get("subtotal")),
        "tax": None if payload.get("tax") is None else _to_number(payload.get("tax")),
        "total": _to_number(payload.get("total")),
        "line_items": transformed_items,
    }
    return transformed


def transform_po(payload: dict[str, Any], input_text: str) -> dict[str, Any]:
    raw_buyer = payload.get("buyer")
    inferred_buyer = _extract_field(input_text, "Buyer")
    buyer = (str(raw_buyer).strip() if raw_buyer else None) or inferred_buyer or "Unknown Buyer"

    line_items = payload.get("items") or payload.get("line_items") or []
    transformed_items = []
    for item in line_items:
        transformed_items.append(
            {
                "item_name": str(item.get("item_name") or item.get("description") or "").strip(),
                "quantity": _to_number(item.get("quantity")),
                "unit_price": _to_number(item.get("unit_price")),
            }
        )

    total = payload.get("total")
    if total is None:
        total = payload.get("total_amount")
    if total is None:
        total = sum(_to_number(item["quantity"]) * _to_number(item["unit_price"]) for item in transformed_items)

    transformed = {
        "buyer": str(buyer),
        "supplier": str(payload.get("supplier", "")).strip(),
        "po_number": str(payload.get("po_number") or payload.get("po_id") or "").strip(),
        "date": str(payload.get("date") or payload.get("order_date") or "").strip(),
        "delivery_date": payload.get("delivery_date", None),
        "currency": str(payload.get("currency", "")).strip().upper(),
        "total": _to_number(total),
        "items": transformed_items,
    }
    return transformed


def _validate_invoice(payload: dict[str, Any]) -> list[str]:
    errors = []
    missing = sorted(INVOICE_REQUIRED - set(payload.keys()))
    if missing:
        errors.append(f"missing keys: {missing}")

    extra = sorted(set(payload.keys()) - INVOICE_REQUIRED)
    if extra:
        errors.append(f"extra keys: {extra}")

    if not isinstance(payload.get("line_items"), list):
        errors.append("line_items must be an array")
    else:
        for idx, item in enumerate(payload["line_items"]):
            if set(item.keys()) != {"description", "quantity", "unit_price"}:
                errors.append(f"line_items[{idx}] keys mismatch")
    return errors


def _validate_po(payload: dict[str, Any]) -> list[str]:
    errors = []
    missing = sorted(PO_REQUIRED - set(payload.keys()))
    if missing:
        errors.append(f"missing keys: {missing}")

    extra = sorted(set(payload.keys()) - PO_REQUIRED)
    if extra:
        errors.append(f"extra keys: {extra}")

    if not isinstance(payload.get("items"), list):
        errors.append("items must be an array")
    else:
        for idx, item in enumerate(payload["items"]):
            if set(item.keys()) != {"item_name", "quantity", "unit_price"}:
                errors.append(f"items[{idx}] keys mismatch")
    return errors


def _infer_doc_type(payload: dict[str, Any]) -> str | None:
    if {"invoice_number", "line_items", "subtotal", "tax", "total"}.issubset(payload.keys()):
        return "invoice"
    if {"po_number", "items", "supplier", "buyer", "total"}.issubset(payload.keys()):
        return "purchase_order"
    return None


def normalize_and_validate_jsonl(apply_fix: bool) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    lines = DATA_FILE.read_text(encoding="utf-8").splitlines()
    transformed_records = []
    errors = []

    invoice_count = 0
    po_count = 0

    for i, line in enumerate(lines, start=1):
        if not line.strip():
            continue

        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append({"line": i, "error": f"invalid JSONL row: {exc}"})
            continue

        try:
            output = json.loads(record.get("output", "{}"))
        except json.JSONDecodeError as exc:
            errors.append({"line": i, "error": f"invalid output JSON: {exc}"})
            continue

        doc_type = output.get("document_type") or _infer_doc_type(output)
        if doc_type == "invoice":
            invoice_count += 1
            normalized = transform_invoice(output)
            row_errors = _validate_invoice(normalized)
        elif doc_type == "purchase_order":
            po_count += 1
            normalized = transform_po(output, record.get("input", ""))
            row_errors = _validate_po(normalized)
        else:
            errors.append({"line": i, "error": f"unsupported document_type: {doc_type}"})
            continue

        if row_errors:
            errors.append({"line": i, "error": "; ".join(row_errors)})

        record["output"] = json.dumps(normalized, ensure_ascii=True)
        transformed_records.append(record)

    if apply_fix and not errors:
        DATA_FILE.write_text(
            "\n".join(json.dumps(rec, ensure_ascii=True) for rec in transformed_records) + "\n",
            encoding="utf-8",
        )

    summary = {
        "total_rows": len(transformed_records),
        "invoice_rows": invoice_count,
        "po_rows": po_count,
        "errors": len(errors),
    }
    return summary, errors


def validate_csv(path: Path) -> list[str]:
    errors = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, escapechar="\\")
        if reader.fieldnames != CSV_REQUIRED_HEADERS:
            errors.append(f"headers mismatch in {path.name}: {reader.fieldnames}")
            return errors

        rows = list(reader)
        if len(rows) != 20:
            errors.append(f"{path.name} should have 20 rows, found {len(rows)}")

        for idx, row in enumerate(rows, start=2):
            valid_flag = row["is_valid_json"]
            required_flag = row["has_all_required_keys"]
            if valid_flag not in {"True", "False"}:
                errors.append(f"{path.name}:{idx} invalid is_valid_json value: {valid_flag}")
            if required_flag not in {"True", "False"}:
                errors.append(f"{path.name}:{idx} invalid has_all_required_keys value: {required_flag}")

            try:
                key_acc = float(row["key_accuracy"])
                val_acc = float(row["value_accuracy"])
            except ValueError:
                errors.append(f"{path.name}:{idx} accuracy values are not numeric")
                continue

            if not (0.0 <= key_acc <= 1.0):
                errors.append(f"{path.name}:{idx} key_accuracy out of range")
            if not (0.0 <= val_acc <= 1.0):
                errors.append(f"{path.name}:{idx} value_accuracy out of range")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and optionally normalize project artifacts.")
    parser.add_argument(
        "--fix-jsonl",
        action="store_true",
        help="Transform data/curated_train.jsonl outputs to schema-compliant keys and overwrite file.",
    )
    args = parser.parse_args()

    summary, jsonl_errors = normalize_and_validate_jsonl(apply_fix=args.fix_jsonl)
    baseline_errors = validate_csv(BASELINE_CSV)
    finetuned_errors = validate_csv(FINETUNED_CSV)

    print("Validation Summary")
    print(json.dumps(summary, indent=2))

    all_errors = []
    all_errors.extend([f"jsonl line {e['line']}: {e['error']}" for e in jsonl_errors])
    all_errors.extend(baseline_errors)
    all_errors.extend(finetuned_errors)

    if all_errors:
        print("\nIssues found:")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print("\nAll checks passed.")
    if args.fix_jsonl:
        print("JSONL normalization applied.")
    else:
        print("Run with --fix-jsonl to apply schema normalization to data/curated_train.jsonl.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
