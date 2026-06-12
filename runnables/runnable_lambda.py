from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableSequence,
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-20b", model_provider="groq", temperature=0.3, max_tokens=1000
)

template = PromptTemplate(
    template = """
    write a joke about {topic}
    """
)

parser = StrOutputParser()

def word_counter(text):
    return len(text.split())

joke_chain = RunnableSequence(template|model|parser)

parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "word_count" : RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_chain,parallel_chain)

response = final_chain.invoke({
    "topic" : "machine learning"
})

print(response)

