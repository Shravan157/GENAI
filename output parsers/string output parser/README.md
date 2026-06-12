# String Output Parser

## What is this?
This folder uses StrOutputParser to convert chat model responses into plain text. The parsed text can be printed or passed into another prompt. In short: it extracts the text content from model messages.

## Why does it exist?
- Use when the next step expects a simple string.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Output parsing | Converts raw LLM output into useful formats. | Use when code needs predictable output. |

## Files in this Folder

### Files
- `string-output-parser.py`: Uses StrOutputParser between two model calls for report generation and summarization.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Forgetting to include parser format instructions in the prompt.
- Expecting the model to always return valid structure without validation.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder uses StrOutputParser to convert chat model responses into plain text. The parsed text can be printed or passed into another prompt.

**Q2. When would you use this in a real project?**
Use when the next step expects a simple string.
