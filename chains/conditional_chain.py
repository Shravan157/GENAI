from langchain.chat_models import init_chat_model
from dotenv import load_dotenv 
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch
from typing import Annotated,Literal,Optional
from pydantic import BaseModel,Field


load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider='openrouter',
    temperature = 0.5
)

review = """
Product Name: Boat Rockerz 450 Bluetooth Headphones

Review:
I am disappointed with the Boat Rockerz 450 Bluetooth Headphones. The sound quality is average, and the bass is not as strong as expected. The ear cushions feel uncomfortable after long use, and the battery backup is lower than what was promised. For the price, I expected better comfort and performance.

Shravan

"""


class ReviewAnalysis(BaseModel):
    sentiment : Annotated[Literal['positive','negative'],Field(description='overall sentiment of the review as positive or negative')]
    company_name : Annotated[Optional[str],Field(default=None,description='name of the company whose product is mentioned in the review')]
    customer_name : Annotated[Optional[str],Field(default=None,description='name of the customer who wrote the review')]

review_template = ChatPromptTemplate([
    ('system','you are an customer service ai assistant'),
    ('human','classify the {review}.Consider the following\n {format_instructions}')
])

review_parser = PydanticOutputParser(pydantic_object=ReviewAnalysis)

sentiment_chain = review_template | model | review_parser



feedback_parser = StrOutputParser()

## positive feedback prompt
positive_feedback_template = ChatPromptTemplate([
    ('system','you are an customer service ai assistant and a creative writer'),
    ('human','Based on the {review} write a thankful message or response from the company to the customer')
])

negative_feedback_template = ChatPromptTemplate([
    ('system','you are an customer service ai assistant and a creative writer'),
    ('human','Based on the {review} write a apology message or response from the company to the customer')
])

neutral_feedback_template = ChatPromptTemplate([
    ('system','you are an customer service ai assistant and a creative writer'),
    ('human','Based on the {review} write a appropriate message or response from the company to the customer')
])

branching_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive',positive_feedback_template | model | feedback_parser),
    (lambda x:x.sentiment=='negative',positive_feedback_template | model | feedback_parser),
    neutral_feedback_template | model | feedback_parser
)

final_chain = sentiment_chain | branching_chain

response = final_chain.invoke({
    "review" : review,
    "format_instructions" : review_parser.get_format_instructions(),
}) 

print(response)
