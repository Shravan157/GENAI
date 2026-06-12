from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel

load_dotenv()

model = init_chat_model(
    "llama-3.1-8b-instant", model_provider="groq", temperature=0.3, max_tokens=1000
)

template1 = ChatPromptTemplate([
    ('system','you are an creative assistant'),
    ('human','write a dark humour about {topic}')
])

template2 = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','explain the {topic}')
])

parser = StrOutputParser()

chain1 = RunnableSequence(template1,model,parser)

parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "explanation": RunnableSequence(template2,model,parser)
})

final_chain = RunnableSequence(chain1,parallel_chain)

response = final_chain.invoke({
    "topic" : 'being unemployed'
})

print(response)
final_chain.get_graph().print_ascii()