from dataclasses import dataclass


@dataclass
class ModelConfig:
    model_id: str
    width: int = 1024
    height: int = 1024
    steps: int = 25
    guidance: float = 7.5
