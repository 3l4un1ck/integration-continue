#!/bin/bash
set -e

# Optional: create venv if you want isolation, or just use system python in container
# python -m venv venv
# source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing requirements..."
pip install -r requirements.txt

echo "Running pytest..."
pytest --cov=todo tests/ --junitxml=test-results.xml 