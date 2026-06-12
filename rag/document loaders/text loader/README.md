# Text Loader

## What is this?
This folder loads a text file and sends the content into a summarization chain. In short: TextLoader converts text files into LangChain documents.

## Why does it exist?
- Use when working with `.txt` notes, stories, or simple documents.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Sample text data | Provides input text for an example. | Use with document loading or chat history examples. |
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Document loading | Turns files or web pages into documents. | Use before summarization or RAG. |

## Files in this Folder

### Files
- `file.txt`: Sample story text used by TextLoader.
- `text_loader.py`: Loads file.txt using TextLoader and summarizes the page content.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Loading documents but not checking the extracted text and metadata.
- Creating chunks without checking whether chunk size and overlap preserve context.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder loads a text file and sends the content into a summarization chain.

**Q2. When would you use this in a real project?**
Use when working with `.txt` notes, stories, or simple documents.
