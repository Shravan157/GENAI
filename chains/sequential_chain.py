from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-20b", model_provider="groq", temperature=0.3, max_tokens=1000
)

template1 = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','give a detailed report on {topic}')
])

template2 = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','give a summary on {text}')
])

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

response = chain.invoke({
    "topic" : "artificial neural network",
})
print(response)
(chain.get_graph().print_ascii())