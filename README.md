# Adobe Hackathon PDF Intelligence

Python and Docker solutions for Adobe Hackathon PDF-processing tasks.

## What This Repo Contains

- `adobe_round1a/`: extracts a structured heading outline from PDFs.
- `adobe_round1b/`: ranks document sections based on persona and task context.

## Problem Areas

### Round 1A: Heading Extraction

Given a PDF, identify the document title and extract a clean outline with heading levels such as `H1`, `H2`, and `H3`.

### Round 1B: Persona-Driven Ranking

Given a collection of PDFs plus a persona/task prompt, identify and rank the most relevant document sections.

## Tech Stack

- Python
- PyMuPDF
- Docker
- JSON output pipelines

## Structure

```text
adobe_round1a/
  Dockerfile
  main.py
  requirements.txt
  utils/

adobe_round1b/
  Dockerfile
  main.py
  requirements.txt
  utils/
```

## Run Round 1A

```bash
cd adobe_round1a
docker build -t adobe-round1a .
docker run --rm -v "$PWD/input:/app/input" -v "$PWD/output:/app/output" adobe-round1a
```

## Run Round 1B

```bash
cd adobe_round1b
docker build -t adobe-round1b .
docker run --rm -v "$PWD/input:/app/input" -v "$PWD/output:/app/output" adobe-round1b
```

## What I Learned

- Extracting layout and text signals from PDFs.
- Designing JSON outputs for downstream evaluation.
- Building Dockerized hackathon submissions.
- Ranking document content based on user intent.

## Status

Hackathon solution repo. The code is kept reproducible and readable for portfolio review.
