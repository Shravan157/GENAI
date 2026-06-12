# Customer Support Assistant Prompt

## What is this?
This folder shows how to load old customer chat history and inject it into a new prompt. It uses MessagesPlaceholder to keep the current query connected to previous turns. In short: it demonstrates prompt-based conversation memory.

## Why does it exist?
- Use when building support bots that need context from earlier messages.
- Use this README when you open this folder and want a quick overview before reading code.

## Concepts Covered
| Concept | What it does | When to use it |
|---|---|---|
| Sample text data | Provides input text for an example. | Use with document loading or chat history examples. |
| Python example script | Contains runnable learning code. | Use when studying the implementation. |

## Files in this Folder

### Files
- `chat_history.txt`: Sample saved conversation used by the customer support assistant.
- `message_placeholder.py`: Loads saved chat history and inserts it with MessagesPlaceholder.

## How to Read This Folder
1. Start with the smallest Python file in this folder.
2. Identify the LangChain object being demonstrated.
3. Follow the data flow from input, to prompt/loader, to model/parser, to printed output.

## Common Mistakes / Gotchas
- Putting all instructions into one hard-coded string instead of using variables.
- Forgetting that chat prompts should separate system and human messages.

## Interview Questions
**Q1. What is the main idea of this folder?**
This folder shows how to load old customer chat history and inject it into a new prompt. It uses MessagesPlaceholder to keep the current query connected to previous turns.

**Q2. When would you use this in a real project?**
Use when building support bots that need context from earlier messages.
