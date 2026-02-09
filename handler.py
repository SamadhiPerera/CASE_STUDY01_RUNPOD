import runpod
import torch
import base64
from io import BytesIO
from diffusers import FluxPipeline
import os

pipe = None

def load_model():
    global pipe
    if pipe is None:
        pipe = FluxPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-dev",
            torch_dtype=torch.bfloat16,
            token=os.environ.get("HF_TOKEN")
        )
        pipe.to("cuda")

def handler(event):
    load_model()

    prompt = event["input"].get("prompt", "A beautiful landscape")

    image = pipe(
        prompt=prompt,
        num_inference_steps=30,
        guidance_scale=7.5
    ).images[0]

    buffered = BytesIO()
    image.save(buffered, format="PNG")

    return {
        "image_base64": base64.b64encode(
            buffered.getvalue()
        ).decode("utf-8")
    }

runpod.serverless.start({"handler": handler})
