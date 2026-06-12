# Pydantic Output Parser

## What is this?
This folder validates model output against a Pydantic schema. The schema describes fields and rules for the generated object. In short: use it when structured output needs validation.

## Why does it exist?
- Use when model output must match strict fields like name, age, or city.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Output parsing | Converts raw LLM output into useful formats. | Use when code needs predictable output. |
| Pydantic validation | Validates fields and types. | Use when output must follow strict rules. |

## Files in this Folder

### Files
- `pydantic-output-parser.py`: Uses PydanticOutputParser to parse a generated person object.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Forgetting to include parser format instructions in the prompt.
- Expecting the model to always return valid structure without validation.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder validates model output against a Pydantic schema. The schema describes fields and rules for the generated object.

**Q2. When would you use this in a real project?**
Use when model output must match strict fields like name, age, or city.
