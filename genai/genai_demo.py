from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os 
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_ollama import OllamaEmbeddings

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv('HUGGINGFACEHUB_API_TOKEN')

## creating model using groq platform api key 

model_groq = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider='groq',
    temperature = 0.5
)

result = model_groq.invoke("what is the capital of India")
print(result.content)

print("-"*100)
## creating model using Huggingface endpoint and chat huggingface 

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V4-Pro",
    task = 'text-generation'
)

model_huggingface = ChatHuggingFace(
    llm = llm
)

response = model_huggingface.invoke('What is the capital of France')
print(response.content)

print("-"*100)
## creating a embedding model using ollama

embedding_model = OllamaEmbeddings(
    model = "nomic-embed-text:latest"
)

input_query = 'Balidan Parmo Dharma'

embeddings = embedding_model.embed_query(input_query)
print(embeddings)


## passing multiple documents for embedding
print("-"*100)

input_docs = [
    'New Delhi is the capital city of India',
    'Cristiano Ronaldo is a football player from portugal',
    'Java is programming language used in enterprise markets',
    'Python is most easiest language due to various layers of abstractions'
]

embedding_docs = embedding_model.embed_documents(input_docs)
print(embedding_docs)