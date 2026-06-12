# Prompts

## What is this?
This folder focuses on reusable prompt design. It covers PromptTemplate, ChatPromptTemplate, message objects, chat history placeholders, and saved prompt templates. In short: prompts define how you ask the model for useful output.

## Why does it exist?
- Use when you want reusable instructions, role-based prompts, or prompt files.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Python example script | Contains runnable learning code. | Use when studying the implementation. |
| Prompt templates | Reusable instructions with variables. | Use when the same prompt structure needs different inputs. |

## Files in this Folder

### Subfolders
- `customer support assistant/`: Open its README for the focused overview.
- `generate custom prompt templates/`: Open its README for the focused overview.

### Files
- `chat-prompt-template.py`: Uses ChatPromptTemplate with system and human roles.
- `messages.py`: Sends explicit SystemMessage and HumanMessage objects to a model.
- `prompt-template.py`: Builds a Streamlit study assistant with a long PromptTemplate.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Putting all instructions into one hard-coded string instead of using variables.
- Forgetting that chat prompts should separate system and human messages.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder focuses on reusable prompt design. It covers PromptTemplate, ChatPromptTemplate, message objects, chat history placeholders, and saved prompt templates.

**Q2. When would you use this in a real project?**
Use when you want reusable instructions, role-based prompts, or prompt files.
