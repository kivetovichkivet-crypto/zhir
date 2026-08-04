class ImageGenerator:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def generate(
        self,
        prompt,
        width=1024,
        height=1024,
        steps=25,
        guidance=7.5,
    ):
        image = self.pipeline(
            prompt=prompt,
            width=width,
            height=height,
            num_inference_steps=steps,
            guidance_scale=guidance,
        ).images[0]

        return image
