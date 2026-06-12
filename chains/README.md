# LangChain Chains

## What is this?
Chains connect multiple steps, usually prompt, model, and parser, into one flow. They help you build workflows where one output can become the next input. In short: chains are pipelines for LLM tasks.

## Why does it exist?
- Use when you want to summarize, classify, branch, or produce multiple outputs from a single input.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Chains | Connects prompt, model, and parser steps. | Use for multi-step LLM workflows. |

## Files in this Folder

### Files
- `conditional_chain.py`: Classifies a product review, then uses RunnableBranch to generate the right company response.
- `parallel_chain.py`: Generates notes and a quiz in parallel from the same topic text.
- `sequential_chain.py`: Creates a detailed report, then sends that output into a summary prompt.
- `simple_chain.py`: Shows the basic LCEL flow: prompt | model | StrOutputParser.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Losing track of what each step outputs and what the next step expects.
- Mixing plain strings, message objects, and parsed outputs without checking types.

## Interview Questions
**Q1. What is the main idea of this folder?**
Chains connect multiple steps, usually prompt, model, and parser, into one flow. They help you build workflows where one output can become the next input.

**Q2. When would you use this in a real project?**
Use when you want to summarize, classify, branch, or produce multiple outputs from a single input.
