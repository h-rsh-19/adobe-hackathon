import fitz  # PyMuPDF

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    possible_title = None
    title_font_size = 0

    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                if not spans:
                    continue

                span = spans[0]
                text = " ".join([s["text"] for s in spans]).strip()
                font_size = span["size"]
                font_name = span["font"]
                y = line["bbox"][1]
                is_bold = "Bold" in font_name or "bold" in font_name.lower()

                # Step 1: Detect title from page 1 (big, top-center bold)
                if i == 0 and font_size > title_font_size and y < 150 and is_bold:
                    possible_title = text
                    title_font_size = font_size

                # Step 2: Heading classification
                level = None
                if font_size >= 16:
                    level = "H1"
                elif font_size >= 14:
                    level = "H2"
                elif font_size >= 12:
                    level = "H3"

                if level:
                    outline.append({
                        "level": level,
                        "text": text,
                        "page": i + 1
                    })

    return {
        "title": possible_title or "Untitled Document",
        "outline": outline
    }
