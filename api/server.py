import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _read_jsonl_health() -> dict:
    data_file = PROJECT_ROOT / "data" / "curated_train.jsonl"
    total = 0
    invoices = 0
    pos = 0

    for line in data_file.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        total += 1
        try:
            row = json.loads(line)
            payload = json.loads(row.get("output", "{}"))
            if "invoice_number" in payload and "line_items" in payload:
                invoices += 1
            elif "po_number" in payload and "items" in payload:
                pos += 1
        except Exception:
            pass

    return {
        "dataset_rows": total,
        "invoice_rows": invoices,
        "po_rows": pos,
    }


class Handler(BaseHTTPRequestHandler):
    def _json_response(self, status: int, payload: dict):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        route = urlparse(self.path).path

        if route == "/health":
            self._json_response(200, {"status": "ok"})
            return

        if route == "/endpoints":
            self._json_response(
                200,
                {
                    "available_endpoints": [
                        "GET /health",
                        "GET /endpoints",
                        "GET /project/status",
                    ]
                },
            )
            return

        if route == "/project/status":
            self._json_response(
                200,
                {
                    "project": "structured-output-finetuning",
                    "checks": _read_jsonl_health(),
                },
            )
            return

        self._json_response(404, {"error": "not found"})


def run() -> None:
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8787"))
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"Server running on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
