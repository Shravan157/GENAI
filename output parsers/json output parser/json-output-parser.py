from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv 
import os 
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V4-Pro",
    task ='text-generation'
)

model = ChatHuggingFace(
    llm = llm
)

parser = JsonOutputParser()

template = ChatPromptTemplate([
    ('system','you are an helpful assistant'),
    ('human','Give me 5 facts about {topic}. consider the following \n {format_instructions} ')
])

chain = template | model | parser

response = chain.invoke({
    "topic" : "being unemployed",
    "format_instructions" : parser.get_format_instructions()  
})

print(response)