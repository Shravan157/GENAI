from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-20b", model_provider="groq", temperature=0.3, max_tokens=1000
)

prompt1 = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','give a detailed report on {topic}')
])

prompt2 = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','generate summary on given {text}')
])

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)
response = chain.invoke({
    "topic" : "machine learning"
})

print(response)
