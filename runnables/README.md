# LangChain Runnables

## What is this?
Runnables are composable LangChain units that can run in sequence, parallel, branch, pass values through, or wrap Python functions. In short: runnables are the building blocks behind modern LangChain workflows.

## Why does it exist?
- Use when you want more control than a simple prompt-model-parser chain.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Runnables | Composable LangChain execution units. | Use for sequence, parallel, branch, or custom flows. |

## Files in this Folder

### Files
- `runnable_branch.py`: Placeholder file; currently empty.
- `runnable_lambda.py`: Wraps a word-counting Python function with RunnableLambda.
- `runnable_parallel.py`: Creates separate social media outputs in parallel.
- `runnable_passthrough.py`: Keeps a generated joke while also explaining it.
- `runnable_sequence.py`: Builds a multi-step flow with RunnableSequence.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Losing track of what each step outputs and what the next step expects.
- Mixing plain strings, message objects, and parsed outputs without checking types.

## Interview Questions
**Q1. What is the main idea of this folder?**
Runnables are composable LangChain units that can run in sequence, parallel, branch, pass values through, or wrap Python functions.

**Q2. When would you use this in a real project?**
Use when you want more control than a simple prompt-model-parser chain.
