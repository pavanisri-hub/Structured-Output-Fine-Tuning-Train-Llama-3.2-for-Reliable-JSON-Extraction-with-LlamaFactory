from __future__ import annotations

import csv
import random

import numpy as np
import tensorflow as tf

from mtl.config import TrainConfig
from mtl.data import make_dataset, make_synthetic_split
from mtl.model import MultiTaskModel
from mtl.utils import ensure_results_dir, evaluate_model


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)


def main() -> None:
    cfg = TrainConfig()
    set_seed(cfg.seed)
    results_dir = ensure_results_dir("results")

    x_train, y_a_train, y_b_train = make_synthetic_split(cfg.train_samples, cfg.input_dim, cfg.seed)
    x_val, y_a_val, y_b_val = make_synthetic_split(cfg.val_samples, cfg.input_dim, cfg.seed + 1)

    train_ds = make_dataset(x_train, y_a_train, y_b_train, cfg.batch_size, shuffle=True, seed=cfg.seed)
    val_ds = make_dataset(x_val, y_a_val, y_b_val, cfg.batch_size, shuffle=False, seed=cfg.seed)

    model = MultiTaskModel(input_dim=cfg.input_dim, hidden_dim=cfg.hidden_dim)
    _ = model(tf.zeros((1, cfg.input_dim), dtype=tf.float32), training=False)

    loss_fn = tf.keras.losses.BinaryCrossentropy()
    optimizer = tf.keras.optimizers.Adam(learning_rate=cfg.learning_rate)

    out_csv = results_dir / "baseline_metrics.csv"
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "epoch",
                "train_loss_a",
                "train_loss_b",
                "val_task_a_accuracy",
                "val_task_a_f1_score",
                "val_task_b_accuracy",
                "val_task_b_f1_score",
            ]
        )

        for epoch in range(1, cfg.epochs + 1):
            running_a, running_b, steps = 0.0, 0.0, 0
            for x, (ya, yb) in train_ds:
                ya = tf.reshape(ya, (-1, 1))
                yb = tf.reshape(yb, (-1, 1))

                with tf.GradientTape() as tape:
                    pa, pb = model(x, training=True)
                    loss_a = loss_fn(ya, pa)
                    loss_b = loss_fn(yb, pb)
                    total_loss = loss_a + loss_b

                grads = tape.gradient(total_loss, model.trainable_variables)
                optimizer.apply_gradients(zip(grads, model.trainable_variables))

                running_a += float(loss_a.numpy())
                running_b += float(loss_b.numpy())
                steps += 1

            val_metrics = evaluate_model(model, val_ds)
            writer.writerow(
                [
                    epoch,
                    running_a / max(1, steps),
                    running_b / max(1, steps),
                    val_metrics["task_a"]["accuracy"],
                    val_metrics["task_a"]["f1_score"],
                    val_metrics["task_b"]["accuracy"],
                    val_metrics["task_b"]["f1_score"],
                ]
            )

    print(f"Saved baseline metrics to {out_csv}")


if __name__ == "__main__":
    main()
