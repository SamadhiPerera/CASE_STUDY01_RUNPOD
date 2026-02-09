import runpod
import time

print("🔥 Container started")

def handler(event):
    print("📥 Event received:", event)
    return {"status": "ok"}

runpod.serverless.start({"handler": handler})

print("✅ RunPod server started")

# KEEP PROCESS ALIVE (important test)
while True:
    time.sleep(60)
