from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableSequence, RunnableLambda
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field, EmailStr
from typing import Literal, Annotated, Optional

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-20b", model_provider="groq", temperature=0.3, max_tokens=1000
)

email = """
Subject: Refund Request – Boat Airdopes 141 (Order #BT4487213)

Dear Boat Customer Support,

I purchased the Boat Airdopes 141 on June 20, 2026 (Order #BT4487213) and received it on June 24, 2026. One of the earbuds is not charging at all, and I've already tried the troubleshooting steps listed on your website with no success.

Given that the product is still under warranty, I would like to request a full refund instead of a replacement, as I no longer wish to continue with this product.

Please process the refund at the earliest and let me know once it's initiated.

Regards,
Priya Menon
+91 98XXXXXXXX
priya.menon@gmail.com
"""


class Query(BaseModel):
    product_id: Annotated[Optional[str], Field(description="Product ID mentioned in the email, if any")]
    product_name: Annotated[Optional[str], Field(description="Name of the product the complaint/query is about")]
    issue_description: Annotated[str, Field(description="Detailed description of the issue or query raised by the sender")]
    order_id: Annotated[Optional[str], Field(description="Order/reference number mentioned in the email, if any")]


class EmailClassification(BaseModel):
    email_type: Annotated[
        Literal['complaint_email', 'refund_request_email', 'general_query_email'],
        Field(description="Analyze the email and classify it as complaint, refund or general email")
    ]
    email_subject: Annotated[str, Field(description='Query mentioned in the email')]
    email_sender: Annotated[str, Field(description='Name of the person who sent the email')]
    email_address: Annotated[EmailStr, Field(description='email address of the person who sent the email')]
    query: Annotated[Query, Field(description="Structured details of the product/order and issue extracted from the email")]


emailType_parser = PydanticOutputParser(pydantic_object=EmailClassification)

email_analysis_template = ChatPromptTemplate([
    ('system', "You are a customer support assistant'kriti' for company Boat"),
    ('human', 'Analyze the email {email} and classify it on the basis of its tone and sentiment. Consider the following\n{format_instructions}')
])

email_data_chain = RunnableSequence(email_analysis_template, model, emailType_parser)


complaint_template = ChatPromptTemplate([
    ("system", "You are a customer support assistant('kriti') for Boat. Write a short, professional email acknowledging the customer's complaint, confirming it has been received, and assuring them it will be resolved soon."),
    ("human", "Sender: {email_sender}\nEmail: {email_address}\nSubject: {email_subject}\nProduct ID: {product_id}\nIssue: {issue_description}\n\nWrite the complaint acknowledgment email.")
])

refund_template = ChatPromptTemplate([
    ("system", "You are a customer support assistant('kriti') for Boat. Write a short, professional email acknowledging the customer's refund request, confirming it is being processed, and mentioning the expected timeline for resolution."),
    ("human", "Sender: {email_sender}\nEmail: {email_address}\nSubject: {email_subject}\nProduct ID: {product_id}\nOrder ID: {order_id}\nIssue: {issue_description}\n\nWrite the refund acknowledgment email.")
])

general_query_template = ChatPromptTemplate([
    ("system", "You are a customer support assistant('kriti') for Boat. Write a short, polite email answering the customer's general query and directing them to further help if needed."),
    ("human", "Sender: {email_sender}\nEmail: {email_address}\nSubject: {email_subject}\nQuery: {issue_description}\n\nWrite the reply email.")
])


def flatten_classification(classification: EmailClassification) -> dict:
    return {
        "email_type": classification.email_type,
        "email_sender": classification.email_sender,
        "email_address": classification.email_address,
        "email_subject": classification.email_subject,
        "product_id": classification.query.product_id,
        "order_id": classification.query.order_id,
        "issue_description": classification.query.issue_description,
    }


branching_chain = RunnableBranch(
    (lambda x: x['email_type'] == 'complaint_email', RunnableSequence(complaint_template, model, StrOutputParser())),
    (lambda x: x['email_type'] == 'refund_request_email', RunnableSequence(refund_template, model, StrOutputParser())),
    RunnableSequence(general_query_template, model, StrOutputParser()),
)

final_chain = RunnableSequence(email_data_chain, RunnableLambda(flatten_classification), branching_chain)

response = final_chain.invoke({
    "email": email,
    "format_instructions": emailType_parser.get_format_instructions(),
})

print(response)
