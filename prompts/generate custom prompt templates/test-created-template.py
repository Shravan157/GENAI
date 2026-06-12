from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os 
from langchain_core.prompts import load_prompt
import os

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq",
    temperature=0.9,
)

template = load_prompt('medical_prompt_template.json')

prompt = template.invoke({
    "assistant_name": "NiramayaAI",
    "specialty": "general medicine",
    "region": "India",
    "audience": "general public",
    "input": "I have had a headache for 3 days, what should I do?"
})

response = model.invoke(prompt)
print(response.content)
