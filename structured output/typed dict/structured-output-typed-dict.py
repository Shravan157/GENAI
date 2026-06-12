from typing import TypedDict
from langchain.chat_models import init_chat_model
from typing_extensions import Annotated,Literal,Optional
from dotenv import load_dotenv
import os 

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

model = init_chat_model(
    "llama-3.3-70b-versatile",
    model_provider = 'groq',   
)

review = """
I’ve been using this smartwatch for a few weeks now and honestly it’s been pretty good overall. The battery life surprised me the most because I only need to charge it every few days even with regular usage. The display looks clean and bright, especially outdoors, and the watch feels comfortable to wear throughout the day.

Fitness tracking seems accurate for steps and heart rate, and I liked how quickly it connected with my phone. Notifications work well most of the time, although sometimes there’s a small delay before messages appear on the watch. The sleep tracking is decent but not always fully accurate.

One thing I didn’t like much was the limited app support compared to more expensive smartwatches. Charging also takes a bit longer than expected. Still, for the price, it feels like a good value product and works well for daily fitness tracking and casual use.

Review by Shravan Parthe
24 Jan 2022
"""

class ReviewAnalysis(TypedDict):
    key_themes : Annotated[list[str],'Key themes discussed in the ']
    sentiment : Annotated[Literal['positive','negative'],'overall sentiment of the reviewer']
    summary : Annotated[str,'summary of the entire review in short']
    pros : Annotated[Optional[list[str]],'positives related to the product']
    cons : Annotated[Optional[list[str]],'negatives related to the product']
    name : Annotated[Optional[str],'Name of the reviewer']
    date : Annotated[Optional[str],'date when the review was made in dd/yy format']

structured_tempalte = model.with_structured_output(ReviewAnalysis)

response = structured_tempalte.invoke(review)
print(response)