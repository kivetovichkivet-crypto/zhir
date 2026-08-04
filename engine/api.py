from abc import ABC, abstractmethod


class ImageBackend(ABC):
    @abstractmethod
    def generate(
        self,
        prompt: str,
        negative_prompt: str = "",
        width: int = 1024,
        height: int = 1024,
        steps: int = 25,
        guidance: float = 7.5,
        seed: int | None = None,
    ):
        """Генерация изображения."""
        raise NotImplementedError
