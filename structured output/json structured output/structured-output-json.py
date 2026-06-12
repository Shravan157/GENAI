from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os


load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

model = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider = 'groq',   
)

# json format is used when we are working with multiple languages and we need a universal data format like json 

review = """
I’ve been using this smartwatch for a few weeks now and honestly it’s been pretty good overall. The battery life surprised me the most because I only need to charge it every few days even with regular usage. The display looks clean and bright, especially outdoors, and the watch feels comfortable to wear throughout the day.

Fitness tracking seems accurate for steps and heart rate, and I liked how quickly it connected with my phone. Notifications work well most of the time, although sometimes there’s a small delay before messages appear on the watch. The sleep tracking is decent but not always fully accurate.

One thing I didn’t like much was the limited app support compared to more expensive smartwatches. Charging also takes a bit longer than expected. Still, for the price, it feels like a good value product and works well for daily fitness tracking and casual use. Review by Shravan Parthe
"""


review_json = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "write down all the key themes dicussed in the review"
    },
    "summary": {
      "type": "string",
      "description": "Short summary about the product in the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["positive", "neutral", "negative"],
      "description": "Sentiment of the review pos , neg or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "positive points of the product",
      "default": None
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "negative points of the product",
      "default": None
    },
    "name": {
      "type": ["string", "null"],
      "description": "Name of the reviewwer",
      "default": None
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

structured_template = model.with_structured_output(review_json)
response = structured_template.invoke(review)
print(response)