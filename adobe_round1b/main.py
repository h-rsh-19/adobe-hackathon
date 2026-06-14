import os
import json
from pathlib import Path
from utils.extractor import extract_sections
from utils.ranker import rank_sections_by_persona

INPUT_DIR = "input"
OUTPUT_DIR = "output"
INPUT_JSON = os.path.join(INPUT_DIR, "challenge1b_input.json")
OUTPUT_JSON = os.path.join(OUTPUT_DIR, "output.json")

def main():
    # Load input config JSON
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    persona = data["persona"]
    pdfs = [doc["filename"] for doc in data.get("documents", [])]

    all_sections = []

    for pdf_filename in pdfs:
        pdf_path = os.path.join(INPUT_DIR, pdf_filename)

        # ✅ Fixed line here
        sections = extract_sections(pdf_path)
        for section in sections:
            section["source_pdf"] = pdf_filename
        all_sections.extend(sections)

    # Rank sections by relevance to persona
    ranked_sections = rank_sections_by_persona(all_sections, persona)

    # Ensure output directory exists
    Path(OUTPUT_DIR).mkdir(exist_ok=True)

    # Write output
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(ranked_sections, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()

# import os
# import json
# from utils.extractor import extract_sections
# from utils.ranker import rank_sections_by_persona

# INPUT_DIR = "input"
# OUTPUT_DIR = "output"

# def load_persona():
#     with open(os.path.join(INPUT_DIR, "challenge1b_input.json"), "r") as f:
#         return json.load(f)

# def process_pdfs(persona):
#     results = []
#     for file in os.listdir(INPUT_DIR):
#         if file.endswith(".pdf"):
#             path = os.path.join(INPUT_DIR, file)
#             sections = extract_sections(path)
#             for section in sections:
#                 section["source_pdf"] = file
#             results.extend(sections)
#     return results

# if __name__ == "__main__":
#     persona = load_persona()
#     all_sections = process_pdfs(persona)
#     ranked = rank_sections_by_persona(all_sections, persona)
#     os.makedirs(OUTPUT_DIR, exist_ok=True)
#     with open(os.path.join(OUTPUT_DIR, "ranked_sections.json"), "w") as f:
#         json.dump(ranked, f, indent=2)
