from langchain_classic.output_parsers.structured import (
    StructuredOutputParser,
    ResponseSchema,
)
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq",
    temperature=0.2
)

schema = [
    ResponseSchema(name='name',description='name of the game',type='string'),
    ResponseSchema(name='number of players',description='number of players playing the game',type='string'),
    ResponseSchema(name='type of game',description='jphysical sport , logical sport or some other kind',type='string'),
    ResponseSchema(name="duration of the game",description="duration of the game",type='string')
]

parser = StructuredOutputParser(response_schemas=schema)

template = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','give the name , number of players , type of game and duration of game played in {country},consider the following\n {format_instructions}')
])

chain = template | model | parser

response = chain.invoke({
    "country" : "Finland",
    "format_instructions" : parser.get_format_instructions()
})

print(response)