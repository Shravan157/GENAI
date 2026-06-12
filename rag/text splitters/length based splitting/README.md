# Length Based Splitting

## What is this?
This folder demonstrates CharacterTextSplitter on plain text and PDF content. It explains chunk size, overlap, and separators. In short: text is split by separator-aware chunk rules.

## Why does it exist?
- Use when you want simple chunking based on length and overlap.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Reference PDF | Stores study/reference material. | Use as source material for loaders or manual reading. |
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Text splitting | Breaks large text into smaller chunks. | Use before embeddings and retrieval. |

## Files in this Folder

### Files
- `Spring_vs_Spring_Boot.pdf`: Reference PDF in this folder.
- `length_based_splitting.py`: Demonstrates CharacterTextSplitter behavior with chunk size, overlap, and separator notes.
- `pypdf_character_text_splitter.py`: Loads a PDF page and splits it with CharacterTextSplitter.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Loading documents but not checking the extracted text and metadata.
- Creating chunks without checking whether chunk size and overlap preserve context.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder demonstrates CharacterTextSplitter on plain text and PDF content. It explains chunk size, overlap, and separators.

**Q2. When would you use this in a real project?**
Use when you want simple chunking based on length and overlap.
