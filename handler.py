import runpod
import torch
import base64
from io import BytesIO
from diffusers import FluxPipeline
import os

print("Starting container...")
print("HF_TOKEN exists:", "HF_TOKEN" in os.environ)
print("CUDA available:", torch.cuda.is_available())

pipe = None

def load_model():
    global pipe
    if pipe is None:
        print("Loading FLUX model...")
        pipe = FluxPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-schnell",  # safer for now
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True
        )
        pipe.enable_attention_slicing()
        pipe.to("cuda")
        print("Model loaded successfully")

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
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return {"image_base64": img_base64}

runpod.serverless.start({"handler": handler})
