#!/bin/bash
echo "Starting run.sh..."
echo "Creating virtual environment..."
python3 -m venv ./env
echo "Activating environment..."
source ./env/bin/activate
# echo "Installing packages..."
# pip3 install -e .
echo "Running the project..."
python3 Driver.py
echo "Setting GitHub username..."
git config user.name "dalton-b"
echo "Staging changes..."
git add .
echo "Changes staged!"
