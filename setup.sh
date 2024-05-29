#!/bin/bash

# Create a virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate

# Install required libraries
uv pip install qrcode[pil]
uv pip install qrcode[svg]

# Deactivate the virtual environment
deactivate

