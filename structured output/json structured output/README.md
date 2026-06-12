# JSON Structured Output

## What is this?
This folder uses a JSON schema with `with_structured_output`. It defines required fields, types, and allowed sentiment values. In short: JSON schema guides the model response shape.

## Why does it exist?
- Use when structured output should stay language-neutral.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| JSON schema/output | Defines language-neutral structured output. | Use when data should be JSON-compatible. |

## Files in this Folder

### Files
- `structured-output-json.py`: Uses JSON schema with with_structured_output for review analysis.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Forgetting to include parser format instructions in the prompt.
- Expecting the model to always return valid structure without validation.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder uses a JSON schema with `with_structured_output`. It defines required fields, types, and allowed sentiment values.

**Q2. When would you use this in a real project?**
Use when structured output should stay language-neutral.
