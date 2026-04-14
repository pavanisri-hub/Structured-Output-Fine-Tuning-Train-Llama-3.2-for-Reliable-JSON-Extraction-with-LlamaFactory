from __future__ import annotations

import tensorflow as tf


class MultiTaskModel(tf.keras.Model):
    def __init__(self, input_dim: int, hidden_dim: int) -> None:
        super().__init__()
        self.backbone = tf.keras.Sequential(
            [
                tf.keras.layers.Input(shape=(input_dim,)),
                tf.keras.layers.Dense(hidden_dim, activation="relu"),
                tf.keras.layers.Dense(hidden_dim, activation="relu"),
            ],
            name="shared_backbone",
        )
        self.head_a = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(hidden_dim // 2, activation="relu"),
                tf.keras.layers.Dense(1, activation="sigmoid"),
            ],
            name="task_a_head",
        )
        self.head_b = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(hidden_dim // 2, activation="relu"),
                tf.keras.layers.Dense(1, activation="sigmoid"),
            ],
            name="task_b_head",
        )

    def call(self, inputs, training: bool = False):
        shared = self.backbone(inputs, training=training)
        pred_a = self.head_a(shared, training=training)
        pred_b = self.head_b(shared, training=training)
        return pred_a, pred_b

    def get_shared_representation(self, inputs):
        return self.backbone(inputs, training=False)
