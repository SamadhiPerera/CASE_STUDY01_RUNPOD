import runpod
import torch
import base64
from io import BytesIO
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-dev",
    torch_dtype=torch.float16,
    use_auth_token=True  # <-- IMPORTANT
)
pipe.to("cuda")

def handler(event):
    prompt = event["input"].get("prompt", "A beautiful landscape")

    image = pipe(
        prompt=prompt,
        num_inference_steps=30,
        guidance_scale=7.5
    ).images[0]

    buffered = BytesIO()
    image.save(buffered, format="PNG")

    return {
        "image_base64": base64.b64encode(buffered.getvalue()).decode()
    }

runpod.serverless.start({"handler": handler})
