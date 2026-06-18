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
    ResponseSchema(name='name',type="string",description='name of a game'),
    ResponseSchema(name='total_players',type='integer',description='total number of players involved in game'),
    ResponseSchema(name="game_type",type="string",description="type of game physical,mental,indoor,outdoor"),
    ResponseSchema(name="game_duration",type="string",description="duration of the game"),
    ResponseSchema(name="game_legends",type="List[string]",description="name of great players to play that game")
]

parser = StructuredOutputParser(response_schemas=schema)

template = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','give me name,total players,type,duration of a random game played in {country}.Consider the following\n {format_instructions}')
])

chain = template | model | parser

response = chain.invoke({
    "country" : "India",
    "format_instructions" : parser.get_format_instructions()
})

print(response)
