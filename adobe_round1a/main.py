import os
import json
from utils.extractor import extract_headings

INPUT_PATH = "/app/input"
OUTPUT_PATH = "/app/output"

def main():
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    for filename in os.listdir(INPUT_PATH):
        if filename.lower().endswith(".pdf"):
            input_pdf_path = os.path.join(INPUT_PATH, filename)
            result = extract_headings(input_pdf_path)
            output_file = filename.replace(".pdf", ".json")
            with open(os.path.join(OUTPUT_PATH, output_file), "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
