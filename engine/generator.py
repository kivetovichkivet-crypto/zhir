import torch
from diffusers import StableDiffusionPipeline


class ImageGenerator:
    def __init__(self):
        self.pipe = None
        self.model_name = "runwayml/stable-diffusion-v1-5"


    def load_model(self):
        if self.pipe is not None:
            return

        print("Загрузка модели...")

        self.pipe = StableDiffusionPipeline.from_pretrained(
            self.model_name,
            torch_dtype=torch.float32
        )

        self.pipe.to("cpu")

        print("Модель загружена")


    def generate(
        self,
        prompt,
        negative_prompt="",
        width=512,
        height=512,
        steps=20,
        cfg=7.5
    ):
        self.load_model()

        result = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            num_inference_steps=steps,
            guidance_scale=cfg
        )

        return result.images[0]
