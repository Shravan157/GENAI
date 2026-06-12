# JSON Output Parser

## What is this?
This folder demonstrates asking a model for JSON and parsing it with JsonOutputParser. The parser provides format instructions that are inserted into the prompt. In short: use it when output should be valid JSON.

## Why does it exist?
- Use when another program or API needs the model response as JSON.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Output parsing | Converts raw LLM output into useful formats. | Use when code needs predictable output. |
| JSON schema/output | Defines language-neutral structured output. | Use when data should be JSON-compatible. |

## Files in this Folder

### Files
- `json-output-parser.py`: Uses JsonOutputParser and parser format instructions to request JSON facts.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Forgetting to include parser format instructions in the prompt.
- Expecting the model to always return valid structure without validation.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder demonstrates asking a model for JSON and parsing it with JsonOutputParser. The parser provides format instructions that are inserted into the prompt.

**Q2. When would you use this in a real project?**
Use when another program or API needs the model response as JSON.
