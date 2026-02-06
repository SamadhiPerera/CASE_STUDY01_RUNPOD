import runpod
import torch
import base64
from io import BytesIO
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-dev",
    torch_dtype=torch.float16
)
pipe.to("cuda")

def handler(event):
    """
    Expected input:
    {
        "prompt": "A futuristic city at sunset"
    }
    """

    prompt = event["input"].get("prompt", "A beautiful landscape")

    image = pipe(
        prompt=prompt,
        num_inference_steps=30,
        guidance_scale=7.5
    ).images[0]

    # Convert image to base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return {
        "image_base64": img_base64
    }

runpod.serverless.start({"handler": handler})