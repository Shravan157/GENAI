from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = init_chat_model(
    "openai/gpt-oss-20b", model_provider="groq", temperature=0.3, max_tokens=1000
)


text = """
Here's a solid chunk of text you can use to test both:

The French Revolution (1789–1799) was a period of radical political and societal transformation in France. It began with the financial crisis of the French monarchy, worsened by France's involvement in the American Revolution and years of poor harvests that led to food shortages. The common people, known as the Third Estate, were heavily taxed while the nobility and clergy were largely exempt.
In 1789, King Louis XVI convened the Estates-General to address the financial crisis. The Third Estate, frustrated by unequal representation, broke away and formed the National Assembly, declaring themselves the true representatives of the French people. This act is considered the beginning of the Revolution.
On July 14, 1789, a Paris mob stormed the Bastille, a royal fortress and prison, marking a turning point in the Revolution. The Declaration of the Rights of Man and Citizen was adopted in August 1789, proclaiming liberty, equality, and popular sovereignty as fundamental principles.
The Revolution entered its most radical phase during the Reign of Terror (1793–1794), led by Maximilien Robespierre and the Committee of Public Safety. Thousands were executed by guillotine, including King Louis XVI and Marie Antoinette. Robespierre himself was eventually arrested and executed in 1794.
The Revolution ended with Napoleon Bonaparte seizing power in 1799 through a coup, establishing the Consulate and later the French Empire. The Revolution's ideals of liberty, equality, and fraternity had a lasting impact on modern democracy and political thought worldwide.
"""


model2 = ChatOllama(model="mistral:latest", temperature=0.1, format="json")


class QuizQuestion(BaseModel):
    question: str = Field(description="question related to the topic")
    options: list[str] = Field(
        min_length=4,
        max_length=4,
        description="exactly four separate options related to the question"
    )
    correct_option: str = Field(description="correct answer from the options")


class Quiz(BaseModel):
    questions: list[QuizQuestion] = Field(description="list of quiz questions")


quiz_parser = PydanticOutputParser(pydantic_object=Quiz)
notes_parser = StrOutputParser()

notes_template = ChatPromptTemplate([
    ('system', 'you are an helpful notes taking assistant'),
    ('human', 'Generate precise and concise notes on {topic}')
])

quiz_template = ChatPromptTemplate([
    ('system', 'you are an helpful quiz generating assistant. Return only valid JSON.'),
    ('human', '''
generate a quiz based on {topic} make sure the number of questions are {questions}.

Rules:
- Return only valid JSON.
- The root object must contain the key "questions".
- "questions" must be a list.
- Each question must contain "question", "options", and "correct_option".
- "options" must be a list of exactly 4 separate strings.
- Do not put all options in one string.
- correct_option must exactly match one option from options.

consider the following:
{format_instructions}
''')
])

chain = RunnableParallel({
    "notes": notes_template | model1 | notes_parser,
    "quiz": quiz_template | model2 | quiz_parser
})

response = chain.invoke({
    "topic": text,
    "questions": 5,
    "format_instructions": quiz_parser.get_format_instructions()
})

print(response)
chain.get_graph().print_ascii()