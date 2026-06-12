# Web Based Loader

## What is this?
This folder loads content from a website and uses it as context for a model answer. In short: WebBaseLoader brings webpage text into a chain.

## Why does it exist?
- Use when your app needs to answer from website content.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Document loading | Turns files or web pages into documents. | Use before summarization or RAG. |

## Files in this Folder

### Files
- `web_based_loader.py`: Loads books.toscrape.com with WebBaseLoader and asks a model a question about it.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Loading documents but not checking the extracted text and metadata.
- Creating chunks without checking whether chunk size and overlap preserve context.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder loads content from a website and uses it as context for a model answer.

**Q2. When would you use this in a real project?**
Use when your app needs to answer from website content.
