from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = init_chat_model(
    "openai/gpt-oss-20b", model_provider="groq", temperature=0.10, max_tokens=1000
)

model2 = ChatOllama(model="mistral:latest")

parser = StrOutputParser()

template1 = ChatPromptTemplate(
    [
        ("system", "you are an creative writer and social media head"),
        ("human", "generate a linkdln post on {topic}"),
    ]
)

template2 = ChatPromptTemplate(
    [
        ("system", "you are an creative head and writer on social media"),
        ("human", "ceate a tweet on {topic}"),
    ]
)

parallel_chain = RunnableParallel(
    {
        "post": RunnableSequence(template1, model1, parser),
        "tweet": RunnableSequence(template2, model2, parser),
    }
)

response = parallel_chain.invoke({
    "topic" : 'cybersecurity'
})

print(response)
parallel_chain.get_graph().print_ascii()