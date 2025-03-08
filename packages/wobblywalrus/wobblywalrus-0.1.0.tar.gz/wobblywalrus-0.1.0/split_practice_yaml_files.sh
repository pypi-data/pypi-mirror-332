#!/bin/bash

# Directory containing the YAML files
DATA_DIR="/Users/mtm/pdev/taylormonacelli/bubblybutterfly/data"

# Create a directory for batches if it doesn't exist
mkdir -p batches

# Find YAML files with 'type: practice' and split into batches of 8
rg -l 'type: practice' --glob='*.yaml' "$DATA_DIR" | split -l 10 - batches/batch_

# Rename the split files to add .txt extension
for file in batches/batch_*; do
    mv "$file" "$file.txt"
done

echo "Practice YAML files have been split into batches in the 'batches' directory."
