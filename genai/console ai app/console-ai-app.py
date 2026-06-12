from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.messages import AIMessage,SystemMessage,HumanMessage
import os 

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')


model = init_chat_model(
    "llama-3.1-8b-instant",
    model_provider = 'groq',
    temperature = 0.3
)


chat_history = [
    SystemMessage(content = 'you are an helpful assistant')
]

while True:
    user_input = input('YOU: ')
    chat_history.append(HumanMessage(content = user_input))
    
    if user_input == 'exit':
        break
    response = model.invoke(chat_history)
    print(f'AI: {response.content}')
    chat_history.append(AIMessage(content = response.content))

print(chat_history)
    