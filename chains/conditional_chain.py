from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal, Optional
from langchain_core.runnables import RunnableBranch

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-20b", model_provider="groq", temperature=0.3, max_tokens=1000
)

review = """

Product Name: Boat Rockerz 450 Bluetooth Headphones

Review:
I am disappointed with the Boat Rockerz 450 Bluetooth Headphones. The sound quality is average, and the bass is not as strong as expected. The ear cushions feel uncomfortable after long use, and the battery backup is lower than what was promised. For the price, I expected better comfort and performance.

Shravan

"""


class ReviewOutcome(BaseModel):
    sentiment: Literal["positive", "negative"] = (
        Field(description="classify the review in positive or negative")
    )
    company_name: Optional[str] = Field(
        description="get the company name of the product", default=None
    )
    customer_name: Optional[str] = Field(
        description="get the name of the customer", default=None
    )


review_outcome_template = ChatPromptTemplate(
    [
        ("system", "you are an helpful customer service ai assistant"),
        (
            "human",
            "classify the {review}. consider the following \n {format_instructions}",
        ),
    ]
)

outcome_parser = PydanticOutputParser(pydantic_object=ReviewOutcome)
feedback_parser = StrOutputParser()

sentiment_chain = review_outcome_template | model | outcome_parser

positive_feeback_template = ChatPromptTemplate(
    [
        ("system", "you are an helpful customer service ai assistant"),
        (
            "human",
            "Write a short and concise thankful response from a company to a customer.\n\nMessage:\n{review}\n\nRules:\n- Make it sound like an official company response.\n- Thank the customer politely on behalf of the company.\n- Acknowledge their positive feedback.\n- Keep it short and professional.\n- Do not over-explain.\n- Do not sound casual or personal.If possible fetch the company name from the review to sound like the company is responding to the review given",
        ),
    ]
)

negative_feeback_template = ChatPromptTemplate(
    [
        ("system", "you are an helpful customer service ai assistant"),
        (
            "human",
            "Write a short and concise apology response from a company to a customer.\n\nIssue:\n{review}\n\nRules:\n- Make it sound like an official company response.\n- Apologize politely on behalf of the company.\n- Acknowledge the customer's problem.\n- Keep it short and professional.\n- Do not over-explain.\n- Do not sound casual or personal.If possible fetch the company name from the review to sound like the company is responding to the review given",
        ),
    ]
)

default_feeback_template = ChatPromptTemplate(
    [
        ("system", "you are an helpful customer service ai assistant"),
        ("human", "write a appropriate feedback based on the {review}"),
    ]
)

branch_chain = RunnableBranch(
    (
        lambda x: x.sentiment == "positive",
        positive_feeback_template | model | feedback_parser,
    ),
    (
        lambda x: x.sentiment == "negative",
        negative_feeback_template | model | feedback_parser,
    ),
    default_feeback_template | model | feedback_parser,
)

final_chain = sentiment_chain | branch_chain

response = final_chain.invoke(
    {"review": review, "format_instructions": outcome_parser.get_format_instructions()}
)

print(response)
final_chain.get_graph().print_ascii()
