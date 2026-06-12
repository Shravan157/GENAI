from langchain.messages import SystemMessage,AIMessage,HumanMessage
from dotenv import load_dotenv
import os 
from langchain.chat_models import init_chat_model

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

model = init_chat_model(
    "openai/gpt-oss-20b", model_provider="groq", temperature=0.3, max_tokens=1000
)

chat_history = [
    SystemMessage(content = 'you are an helpful assistant'),
    HumanMessage(content='what is the capital of India')
]

response = model.invoke(chat_history)
chat_history.append(AIMessage(content=response.content))
print(chat_history)