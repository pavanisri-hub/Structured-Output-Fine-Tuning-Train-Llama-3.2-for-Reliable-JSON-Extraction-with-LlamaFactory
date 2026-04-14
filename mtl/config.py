from dataclasses import dataclass


@dataclass
class TrainConfig:
    seed: int = 42
    batch_size: int = 64
    epochs: int = 8
    learning_rate: float = 1e-3
    hidden_dim: int = 64
    train_samples: int = 4096
    val_samples: int = 1024
    input_dim: int = 20
