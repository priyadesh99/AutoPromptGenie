#!/bin/bash
# Script to fetch and save the WritingPrompts dataset
# Need to do to make sure this runs: chmod +x scripts/run_data_collection.sh


echo "Running data collection script..."
python3 src/data_collection.py
echo "Data collection complete. Raw dataset saved in data/raw/"
