from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-20b", model_provider="groq", temperature=0.3, max_tokens=1000
)


template = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','explain summary about {topic}')
])

chain = template | model | StrOutputParser()

response = chain.invoke({
    "topic" : "Agentic Systems"
})

print(response)
print(chain.get_graph().print_ascii())