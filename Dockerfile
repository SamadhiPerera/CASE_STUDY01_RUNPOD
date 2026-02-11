FROM runpod/base:0.4.0-cuda11.8.0

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install runpod

COPY handler.py .

CMD ["python3", "-u", "handler.py"]

# force rebuild 2026



