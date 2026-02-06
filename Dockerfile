FROM runpod/pytorch:2.1.0-cuda11.8

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY handler.py .

CMD ["python", "handler.py"]