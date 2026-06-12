# Text Structure Based Splitting

## What is this?
This folder demonstrates RecursiveCharacterTextSplitter. It tries better separators first so chunks preserve natural text structure. In short: recursive splitting keeps text more readable.

## Why does it exist?
- Use when paragraphs and sentence boundaries matter.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Diagram image | Shows a visual explanation. | Use when understanding splitter behavior visually. |
| Text splitting | Breaks large text into smaller chunks. | Use before embeddings and retrieval. |
| Python example script | Contains runnable learning code. | Use when studying the implementation. |

## Files in this Folder

### Files
- `recursive-character-text-overlap.png`: Diagram image in this folder.
- `recursive-character-text-splitter.png`: Diagram image in this folder.
- `recursive_character_text_splitter.py`: Demonstrates RecursiveCharacterTextSplitter on paragraph text.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Loading documents but not checking the extracted text and metadata.
- Creating chunks without checking whether chunk size and overlap preserve context.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder demonstrates RecursiveCharacterTextSplitter. It tries better separators first so chunks preserve natural text structure.

**Q2. When would you use this in a real project?**
Use when paragraphs and sentence boundaries matter.
