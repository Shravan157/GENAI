from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
import os 
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()
os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv('HUGGINGFACEHUB_API_TOKEN')

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V4-Pro",
    task ='text-generation'
)

model = ChatHuggingFace(
    llm = llm
)

class Person(BaseModel):
    name : str = Field(description='name of a person')
    age : int = Field(gt=5,le=100,description = 'age of a person')
    city : str = Field(description = 'name of the city')


template = PromptTemplate(
    template = """
    Give me a fictional name age and city of a 
    person from {country}.Follow the following \n
    {format_instructions}
    """
)

parser = PydanticOutputParser(pydantic_object=Person)

chain = template | model | parser

response = chain.invoke({
    "country" : "India",
    "format_instructions": parser.get_format_instructions()
})

print(response)

