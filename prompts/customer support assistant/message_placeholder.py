from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os 
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.messages import AIMessage,HumanMessage,SystemMessage

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq",
    temperature=0.2,
)

chat_history = []

with open('chat_history.txt') as f:
    for line in f:
        line = line.strip()
        if line.startswith('HumanMessage'):
            content = line.split('content="')[1].split('"')[0]
            chat_history.append(HumanMessage(content = content))
        if line.startswith('AIMessage'):
            content = line.split('content="')[1].split('"')[0]
            chat_history.append(AIMessage(content=content))

template = ChatPromptTemplate([
    ('system','you are an helpful customer service assistant'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human','{query}')
])

prompt = template.invoke({
    "chat_history" : chat_history,
    "query" : 'Where is my refund'
})

response = model.invoke(prompt)
chat_history.append(AIMessage(content = response.content))
print(response.content)
print(chat_history)