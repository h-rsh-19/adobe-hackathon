# Adobe Hackathon 2025 – Round 1B  
## Persona-Driven Section Extractor

This solution is designed for **Round 1B** of the **Adobe India Hackathon 2025**, focusing on extracting and ranking relevant PDF sections based on a given persona and job-to-be-done.

---

## 🧠 Problem Statement

Given:
- A set of PDF documents.
- A `challenge1b_input.json` file with a `persona` and associated `job_to_be_done`.

**Objective:**
1. Extract meaningful sections from each PDF.
2. Rank the most relevant sections across all PDFs based on persona alignment.
3. Output a ranked list of top 10 sections in `output.json`.

---

## 📂 Folder Structure

```
.
├── input/
│   ├── challenge1b_input.json   # Input config with persona and documents
│   └── *.pdf                    # PDF documents to be processed
├── output/
│   └── output.json              # Final ranked section output
├── utils/
│   ├── extractor.py             # PDF section extraction logic
│   └── ranker.py                # Persona-based ranking logic
├── main.py                      # Main script for running the pipeline
├── Dockerfile                   # For containerized offline execution
└── README.md
```

---

## ⚙️ How It Works

### 1. **Extraction** (`extractor.py`)
- Uses `PyMuPDF` (`fitz`) to read PDFs.
- Extracts text blocks longer than 30 characters.
- Stores each section with page number and source file reference.

### 2. **Ranking** (`ranker.py`)
- Cleans and tokenizes the persona and job description.
- Measures intersection of keywords between persona and section text.
- Returns top 10 most relevant sections.

---

## 🧪 Input Format (`challenge1b_input.json`)
```json
{
  "persona": {
    "persona": "Content Strategist",
    "job_to_be_done": "Understand trends in Gen Z marketing",
    "task": "Find insights from recent reports"
  },
  "documents": [
    { "filename": "report1.pdf" },
    { "filename": "report2.pdf" }
  ]
}
```

---

## ✅ Output Format (`output/output.json`)
Top 10 sections in ranked order:
```json
[
  {
    "text": "The Gen Z audience engages most with ...",
    "page": 5,
    "source_pdf": "report1.pdf"
  },
  ...
]
```

---

## 🐳 Docker Instructions (Offline Inference)

```bash
docker build -t round1b .
docker run --rm -v ${PWD}/input:/app/input -v ${PWD}/output:/app/output round1b
```

> 💡 Ensure `input/` and `output/` folders exist with proper files before running.

---

## 📝 Dependencies

- Python 3.8+
- PyMuPDF (`fitz`)
- Docker (for containerized run)

Install manually (optional):

```bash
pip install pymupdf
```

---

## 👥 Authors

- Harsha Vardhan K, N Nikheth Kumar, E E S Vineeth Reddy  
- Under the guidance of Dr. V. B. Narasimha  
- University College of Engineering (A), Osmania University

---

## 📌 Notes

- Runs completely **offline** in ≤60 seconds on CPU-only.
- Output size and model kept under the 1GB constraint.
- Designed with modular, extensible code for future persona/task expansion.

---