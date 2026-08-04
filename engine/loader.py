from diffusers import StableDiffusionXLPipeline
import torch


class ModelLoader:
    def __init__(self):
        self.pipeline = None

    def load(self, model_id):
        self.pipeline = StableDiffusionXLPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
        )

        if torch.cuda.is_available():
            self.pipeline.to("cuda")
        else:
            self.pipeline.to("cpu")

        return self.pipeline
