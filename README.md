# Starting GenAI

A folder-by-folder GenAI learning repo with compact reference docs inside each topic folder. Open the folder you are studying and read its local `README.md` first.

## Folder Index
| Folder | What to read it for |
|---|---|
| [chains](chains/README.md) | Chains connect multiple steps, usually prompt, model, and parser, into one flow. |
| [genai](genai/README.md) | This folder introduces the basic building blocks of GenAI apps: chat models, chat history, embeddings, and similarity. |
| [output parsers](output%20parsers/README.md) | Output parsers convert raw model replies into useful Python data formats. |
| [prompts](prompts/README.md) | This folder focuses on reusable prompt design. |
| [rag](rag/README.md) | This folder covers the first steps of RAG: loading documents and splitting text into chunks. |
| [runnables](runnables/README.md) | Runnables are composable LangChain units that can run in sequence, parallel, branch, pass values through, or wrap Python functions. |
| [spring boot notes](spring%20boot%20notes/README.md) | This folder stores PDF notes about Spring Boot and related backend topics. |
| [structured output](structured%20output/README.md) | This folder teaches ways to make model output predictable. |

## Suggested Learning Order
1. `genai/` for model calls, chat history, and embeddings.
2. `prompts/` for prompt templates and chat prompts.
3. `output parsers/` and `structured output/` for predictable responses.
4. `chains/` and `runnables/` for workflows.
5. `rag/` for document loading and text splitting.

## Note
The old single long README has been replaced with this short index so each folder stays readable on its own.
