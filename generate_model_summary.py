from __future__ import annotations

import io
from contextlib import redirect_stdout

import tensorflow as tf

from mtl.config import TrainConfig
from mtl.model import MultiTaskModel
from mtl.utils import ensure_results_dir


def main() -> None:
    cfg = TrainConfig()
    model = MultiTaskModel(input_dim=cfg.input_dim, hidden_dim=cfg.hidden_dim)

    dummy = tf.zeros((1, cfg.input_dim), dtype=tf.float32)
    model(dummy, training=False)

    results_dir = ensure_results_dir("results")
    out_path = results_dir / "model_architecture.txt"

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        print("=== Shared Backbone Summary ===")
        model.backbone.summary()
        print("\n=== Full Multi-Task Model Summary ===")
        model.summary()

    content = buffer.getvalue()
    print(content)
    out_path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
