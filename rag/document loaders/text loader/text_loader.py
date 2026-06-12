from langchain_community.document_loaders import TextLoader
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

loader = TextLoader('file.txt',encoding='utf-8')

response = loader.load()
print(response)
print('-'*100)
print(len(response))
print(response[0].metadata)
print(response[0].page_content)

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq",
    temperature=0.9,
    max_tokens=200
)

template = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','summarize the {topic}')
])

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({
    "topic" : response[0].page_content
})

print(result)