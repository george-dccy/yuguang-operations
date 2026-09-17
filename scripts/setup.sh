#!/usr/bin/env bash
set -e

echo "Setting up yuguang-operations environment"

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install browser-use pyyaml python-dotenv

echo "Environment ready"
