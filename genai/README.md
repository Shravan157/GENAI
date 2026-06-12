# GenAI Basics

## What is this?
This folder introduces the basic building blocks of GenAI apps: chat models, chat history, embeddings, and similarity. It shows how different providers can be called through LangChain-style interfaces. In short: this is the starter area for model calls and embeddings.

## Why does it exist?
- Use when you want to understand model invocation, chatbot loops, or semantic similarity.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |

## Files in this Folder

### Subfolders
- `console ai app/`: Open its README for the focused overview.
- `cosine-similarity-app/`: Open its README for the focused overview.

### Files
- `genai_demo.py`: Calls Groq and Hugging Face chat models, then creates query and document embeddings with Ollama.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Running scripts before setting required API keys.
- Reading only the final print output instead of tracing how the input changes step by step.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder introduces the basic building blocks of GenAI apps: chat models, chat history, embeddings, and similarity. It shows how different providers can be called through LangChain-style interfaces.

**Q2. When would you use this in a real project?**
Use when you want to understand model invocation, chatbot loops, or semantic similarity.
