from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import tensorflow as tf


def ensure_results_dir(path: str = "results") -> Path:
    results = Path(path)
    results.mkdir(parents=True, exist_ok=True)
    return results


def compute_binary_metrics(y_true: np.ndarray, y_prob: np.ndarray) -> dict[str, float]:
    y_pred = (y_prob >= 0.5).astype(np.int32)
    y_true_i = y_true.astype(np.int32)

    tp = int(np.sum((y_pred == 1) & (y_true_i == 1)))
    fp = int(np.sum((y_pred == 1) & (y_true_i == 0)))
    fn = int(np.sum((y_pred == 0) & (y_true_i == 1)))

    accuracy = float(np.mean(y_pred == y_true_i))
    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)
    return {"accuracy": accuracy, "f1_score": float(f1)}


def evaluate_model(model: tf.keras.Model, val_ds: tf.data.Dataset) -> dict[str, dict[str, float]]:
    y_a_true, y_b_true = [], []
    y_a_prob, y_b_prob = [], []

    for x, (ya, yb) in val_ds:
        pa, pb = model(x, training=False)
        y_a_true.append(ya.numpy())
        y_b_true.append(yb.numpy())
        y_a_prob.append(pa.numpy().reshape(-1))
        y_b_prob.append(pb.numpy().reshape(-1))

    ya_t = np.concatenate(y_a_true)
    yb_t = np.concatenate(y_b_true)
    ya_p = np.concatenate(y_a_prob)
    yb_p = np.concatenate(y_b_prob)

    return {
        "task_a": compute_binary_metrics(ya_t, ya_p),
        "task_b": compute_binary_metrics(yb_t, yb_p),
    }


def write_final_metrics(
    baseline_metrics: dict[str, dict[str, float]],
    pcgrad_metrics: dict[str, dict[str, float]],
    results_dir: Path,
) -> None:
    payload = {
        "baseline": baseline_metrics,
        "pcgrad": pcgrad_metrics,
    }
    output_path = results_dir / "final_metrics.json"
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def non_none_or_zero(grads: list[tf.Tensor | None], vars_: list[tf.Variable]) -> list[tf.Tensor]:
    fixed: list[tf.Tensor] = []
    for g, v in zip(grads, vars_):
        if g is None:
            fixed.append(tf.zeros_like(v))
        else:
            fixed.append(g)
    return fixed


def flatten_grads(grads: list[tf.Tensor]) -> tf.Tensor:
    return tf.concat([tf.reshape(g, [-1]) for g in grads], axis=0)
