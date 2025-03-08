#!/bin/bash

# Directory containing the YAML files
DATA_DIR="/Users/mtm/pdev/taylormonacelli/bubblybutterfly/data"

# Create a directory for batches if it doesn't exist
mkdir -p batches

# Find all YAML files and split into batches of 8
find "$DATA_DIR" -name "*.yaml" | split -l 8 - batches/batch_

# Rename the split files to add .txt extension
for file in batches/batch_*; do
    mv "$file" "$file.txt"
done

echo "Files have been split into batches in the 'batches' directory."
