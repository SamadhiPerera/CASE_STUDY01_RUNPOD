import runpod
import time

print("🔥 Container booted successfully")

def handler(event):
    return {"status": "healthy"}

runpod.serverless.start({"handler": handler})

while True:
    time.sleep(60)
