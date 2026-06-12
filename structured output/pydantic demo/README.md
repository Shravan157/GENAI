# Pydantic Structured Output

## What is this?
This folder first shows normal Pydantic validation, then uses a Pydantic model with an LLM. In short: Pydantic gives strict, typed model output.

## Why does it exist?
- Use when output fields need validation rules and typed access.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Pydantic validation | Validates fields and types. | Use when output must follow strict rules. |

## Files in this Folder

### Files
- `pydantic_demo.py`: Shows basic Pydantic validation for student data.
- `structured-output-pydantic.py`: Uses a Pydantic review schema with with_structured_output.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Forgetting to include parser format instructions in the prompt.
- Expecting the model to always return valid structure without validation.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder first shows normal Pydantic validation, then uses a Pydantic model with an LLM.

**Q2. When would you use this in a real project?**
Use when output fields need validation rules and typed access.
