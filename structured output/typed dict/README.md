# TypedDict Structured Output

## What is this?
This folder starts with a basic TypedDict and then uses TypedDict for LLM structured output. In short: TypedDict is a lightweight schema option.

## Why does it exist?
- Use when you want simple dictionary-shaped output without Pydantic validation.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| TypedDict schema | Defines lightweight dictionary shapes. | Use for simple structured outputs. |

## Files in this Folder

### Files
- `structured-output-typed-dict.py`: Uses TypedDict with with_structured_output for review analysis.
- `typed-dict-demo.py`: Shows a basic Python TypedDict example.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Forgetting to include parser format instructions in the prompt.
- Expecting the model to always return valid structure without validation.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder starts with a basic TypedDict and then uses TypedDict for LLM structured output.

**Q2. When would you use this in a real project?**
Use when you want simple dictionary-shaped output without Pydantic validation.
