from langchain_community.document_loaders import WebBaseLoader
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


url = "https://books.toscrape.com"
loader = WebBaseLoader(url)
docs = loader.load()

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-120b", model_provider="groq", temperature=0.2, max_tokens=1000
)

parser = StrOutputParser()

template = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','considering the {content} answer the {query}')
])

chain = template | model | parser

response = chain.invoke({
    "query" : 'Find the best books to read',
    "content" : docs[0].page_content
})

print(response)