# Structured Output Parser

## What is this?
This folder uses ResponseSchema and StructuredOutputParser for simple named output fields. It is lighter than a full Pydantic model. In short: it asks the model to fill specific fields.

## Why does it exist?
- Use when you need a few simple structured fields from the model.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Output parsing | Converts raw LLM output into useful formats. | Use when code needs predictable output. |

## Files in this Folder

### Files
- `structured-output-parser.py`: Uses ResponseSchema fields with StructuredOutputParser.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Forgetting to include parser format instructions in the prompt.
- Expecting the model to always return valid structure without validation.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder uses ResponseSchema and StructuredOutputParser for simple named output fields. It is lighter than a full Pydantic model.

**Q2. When would you use this in a real project?**
Use when you need a few simple structured fields from the model.
