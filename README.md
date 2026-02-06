
OBJECTIVE

The goal is to establish a RunPod serverless GPU endpoint that can produce images based on a text prompt by utilizing the FLUX.1-dev image generation model provided by Black Forest Labs.
The endpoint shall accept a text prompt and generate an image return as a base64 encoded image.

Model: 

FLUX.1-dev from Black Forest Labs
User Guide for Hugging Face 
repository Id black-forest-labs/FLUX.1-dev.

The FLUX model has been pre-trained on converting text to an image, and it can be loaded using the Hugging Face Diffusers' pipeline.

This project has the following structure:

CASE_STUDY01/
├── handler.py          # Serves as a request handler for serverless processing
├── requirements.txt    # Contains all required Python libraries
├── Dockerfile          # Defines Docker image
└── README.md           # Documentation for the project


The handler located in the file handler.py will:

Load the FLUX model once the container is started
Receive text prompts through serverless requests
Use the GPU to generate images
Provide an output base64 PNG image

The handler has been developed using the RunPod serverless website.

The Docker image is created from a RunPod sight GPU-enabled PyTorch base image and includes:

Python runtime
Required ML libraries
Serverless handler logic

The following command will build the image.

To build image:
docker build -t /flux-runpod .

To push image:
docker push /flux-runpod