from __future__ import annotations

import numpy as np
import tensorflow as tf


AUTOTUNE = tf.data.AUTOTUNE


def make_synthetic_split(samples: int, input_dim: int, seed: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    x = rng.normal(0.0, 1.0, size=(samples, input_dim)).astype(np.float32)

    # Two related but partially competing tasks with noisy boundaries.
    noise_a = rng.normal(0.0, 0.6, size=(samples,)).astype(np.float32)
    noise_b = rng.normal(0.0, 0.6, size=(samples,)).astype(np.float32)

    score_a = 0.9 * x[:, 0] + 0.8 * x[:, 1] - 0.4 * x[:, 2] + noise_a
    score_b = -0.9 * x[:, 0] + 0.8 * x[:, 1] + 0.4 * x[:, 3] + noise_b

    y_a = (score_a > 0).astype(np.float32)
    y_b = (score_b > 0).astype(np.float32)
    return x, y_a, y_b


def make_dataset(
    x: np.ndarray,
    y_a: np.ndarray,
    y_b: np.ndarray,
    batch_size: int,
    shuffle: bool,
    seed: int,
) -> tf.data.Dataset:
    ds = tf.data.Dataset.from_tensor_slices((x, (y_a, y_b)))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(x), seed=seed, reshuffle_each_iteration=True)
    ds = ds.batch(batch_size).prefetch(AUTOTUNE)
    return ds
