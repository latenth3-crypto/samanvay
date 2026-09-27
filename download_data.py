# -*- coding: utf-8 -*-
"""
SIH 26099: Phase 1 Data Acquisition Script
Downloads the required extracted item datasets from Hugging Face into data/raw/huggingface/
"""

import os
import requests

BASE_URL = "https://huggingface.co/datasets/Prasenjeet25/sih26099-cpse-material-codes/resolve/main/data/processed/extracted_items/"
TARGET_DIR = os.path.join("data", "raw", "huggingface")

FILES = [
    "material_description_corpus.csv",
    "ntpc_material_items.csv",
    "iocl_procurement_plan_items.csv"
]

def download_file(filename: str, target_dir: str):
    url = BASE_URL + filename
    dest_path = os.path.join(target_dir, filename)
    print(f"Downloading: {filename} from {url}...")
    
    resp = requests.get(url, stream=True, timeout=60)
    resp.raise_for_status()
    
    with open(dest_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=65536):
            if chunk:
                f.write(chunk)
                
    size = os.path.getsize(dest_path)
    print(f"  -> Saved to {dest_path} ({size:,} bytes)")

def main():
    os.makedirs(TARGET_DIR, exist_ok=True)
    print(f"Acquiring datasets into: {TARGET_DIR}")
    for fname in FILES:
        download_file(fname, TARGET_DIR)
    print("All downloads completed successfully.")

if __name__ == "__main__":
    main()
