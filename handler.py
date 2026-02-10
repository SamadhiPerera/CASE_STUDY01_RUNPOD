import runpod
import torch

pipe = None  # global cache

def load_model():
    global pipe
    if pipe is None:
        print("🔄 Loading model...")
        from diffusers import FluxPipeline
        pipe = FluxPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-dev",
            torch_dtype=torch.float16
        ).to("cuda")
        print("✅ Model loaded")

def handler(event):
    load_model()

    prompt = event["input"].get("prompt", "a beautiful landscape")
    image = pipe(prompt).images[0]

    image.save("/tmp/output.png")

    return {
        "status": "success",
        "message": "Image generated"
    }

runpod.serverless.start({
    "handler": handler
})
