import fitz  # PyMuPDF

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []

    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                text = " ".join(span["text"] for span in line["spans"]).strip()
                if len(text) > 30:
                    sections.append({
                        "text": text,
                        "page": page_num + 1
                    })

    return sections
