# CSV Loader

## What is this?
This folder loads IPL match data from a CSV file. Each row becomes document content with metadata. In short: CSVLoader turns tabular rows into documents.

## Why does it exist?
- Use when structured CSV data should be searchable or summarized.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Dataset | Provides structured tabular data. | Use with CSV loading examples. |
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Document loading | Turns files or web pages into documents. | Use before summarization or RAG. |

## Files in this Folder

### Files
- `IPL_Matches_2008_2022.csv`: IPL match dataset used by the CSV loader example.
- `csv_loader.py`: Loads IPL_Matches_2008_2022.csv with CSVLoader.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Loading documents but not checking the extracted text and metadata.
- Creating chunks without checking whether chunk size and overlap preserve context.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder loads IPL match data from a CSV file. Each row becomes document content with metadata.

**Q2. When would you use this in a real project?**
Use when structured CSV data should be searchable or summarized.
