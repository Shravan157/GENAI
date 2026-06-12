# PyPDF Loader

## What is this?
This folder loads a PDF and prints its extracted page content and metadata. In short: PyPDFLoader turns PDF pages into documents.

## Why does it exist?
- Use when RAG needs content from PDFs.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Reference PDF | Stores study/reference material. | Use as source material for loaders or manual reading. |
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Document loading | Turns files or web pages into documents. | Use before summarization or RAG. |

## Files in this Folder

### Files
- `Spring_vs_Spring_Boot.pdf`: Reference PDF in this folder.
- `pypdf_loader.py`: Loads a PDF with PyPDFLoader and prints page content plus metadata.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Loading documents but not checking the extracted text and metadata.
- Creating chunks without checking whether chunk size and overlap preserve context.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder loads a PDF and prints its extracted page content and metadata.

**Q2. When would you use this in a real project?**
Use when RAG needs content from PDFs.
