from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from typing import Annotated,List
from pydantic import BaseModel,Field
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = init_chat_model(
    "nvidia/nemotron-3-ultra-550b-a55b:free",
    model_provider='openrouter',
    temperature = 0.5
)

text = """
The French Revolution (1789–1799) was a period of radical political and societal transformation in France. It began with the financial crisis of the French monarchy, worsened by France's involvement in the American Revolution and years of poor harvests that led to food shortages. The common people, known as the Third Estate, were heavily taxed while the nobility and clergy were largely exempt.
In 1789, King Louis XVI convened the Estates-General to address the financial crisis. The Third Estate, frustrated by unequal representation, broke away and formed the National Assembly, declaring themselves the true representatives of the French people. This act is considered the beginning of the Revolution.
On July 14, 1789, a Paris mob stormed the Bastille, a royal fortress and prison, marking a turning point in the Revolution. The Declaration of the Rights of Man and Citizen was adopted in August 1789, proclaiming liberty, equality, and popular sovereignty as fundamental principles.
The Revolution entered its most radical phase during the Reign of Terror (1793–1794), led by Maximilien Robespierre and the Committee of Public Safety. Thousands were executed by guillotine, including King Louis XVI and Marie Antoinette. Robespierre himself was eventually arrested and executed in 1794.
The Revolution ended with Napoleon Bonaparte seizing power in 1799 through a coup, establishing the Consulate and later the French Empire. The Revolution's ideals of liberty, equality, and fraternity had a lasting impact on modern democracy and political thought worldwide.
"""

class Question(BaseModel):
    question: Annotated[str, Field(description='question text')]
    options: Annotated[List[str], Field(description='4 answer options', min_length=4, max_length=4)]
    correct_option_index: Annotated[int, Field(description='0-indexed position of the correct answer', ge=0, le=3)]

class Quiz(BaseModel):
    questions: Annotated[List[Question], Field(description='list of quiz questions', min_length=1)]

notes_template = ChatPromptTemplate([
    ('system','you are an helpful study assistant'),
    ('human','Help me take concise and simple notes from the {text}')
])

quiz_template = ChatPromptTemplate([
    ('system','give a quiz from the {text} and the total number of questions must be {num_questions}. Consider the following\n {format_instructions}')
])


notes_parser = StrOutputParser()

quiz_parser = PydanticOutputParser(pydantic_object=Quiz)

chain = RunnableParallel({
    "notes" : notes_template | model | notes_parser,
    "quiz" : quiz_template | model | quiz_parser
})

response = chain.invoke({
    'text' : text,
    'format_instructions' : quiz_parser.get_format_instructions(),
    'num_questions' : 5
})

print(response)
chain.get_graph().print_ascii()
