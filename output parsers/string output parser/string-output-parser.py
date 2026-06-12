from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash", task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

template1 = ChatPromptTemplate(
    [
        ("system", "you are an helpful assistant"),
        ("human", "Generate a detailed report on {topic}"),
    ]
)

template2 = ChatPromptTemplate(
    [
        ("system", "you are an helpful assistant"),
        ("human", "Generate a short summary on {text}"),
    ]
)

chain = template1 | model | parser | template2 | model | parser

response = chain.invoke({"topic": "Fine tuning in AI"})

print(response)
