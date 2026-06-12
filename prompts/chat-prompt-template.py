from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os 


load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq",
    temperature=0.9,
)

template = ChatPromptTemplate([
    ('system','you are an helpful {domain} assistant'),
    ('human','Explain me about {topic}')
])

prompt = template.invoke({
    "domain" : 'football',
    "topic" : 'offside rule'
})

response = model.invoke(prompt)
print(response.content)