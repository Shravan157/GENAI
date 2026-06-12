from pydantic import BaseModel,Field
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from typing import Optional,Literal
import os

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = init_chat_model("openai/gpt-oss-20b", model_provider="groq", temperature=0.2)


review = """
I recently bought the iQOO Z10 and after using it for a few weeks, I can say that it has been a pretty good experience overall. The phone comes with a massive 7300mAh battery, which is easily one of its biggest highlights. Even with heavy usage including social media, video streaming, calls, and gaming, the battery comfortably lasts more than a day and sometimes even stretches close to two days.

Performance has been smooth thanks to the Qualcomm Snapdragon 7s Gen 3 processor. Everyday tasks such as multitasking, browsing, and app switching feel responsive, and the phone handles games quite well without noticeable lag. The device is available with up to 12GB RAM and 256GB storage, which is more than enough for most users.

The 6.77-inch AMOLED display with a 120Hz refresh rate looks vibrant and fluid. Watching videos and scrolling through apps feels smooth, while the brightness is good enough for outdoor usage. The dual rear camera setup, featuring a 50MP Sony IMX882 primary sensor with OIS and a 2MP depth sensor, captures decent photos in daylight. The 32MP front camera takes clear selfies and works well for video calls. Camera performance in low-light situations is acceptable, though not the strongest aspect of the phone.

Another feature I liked is the 90W FlashCharge support. Even with such a large battery, charging is relatively quick and convenient. The phone also includes an in-display fingerprint scanner, dual stereo speakers, IP65 dust and water resistance, and runs on Funtouch OS 15 based on Android 15.

Build quality feels solid, and despite the large battery, the phone remains comfortable to hold. Overall, the iQOO Z10 offers excellent battery life, reliable performance, a smooth AMOLED display, fast charging, and a capable camera system at a competitive price. While the cameras could be better in challenging lighting conditions, the overall package delivers great value for money and makes it a strong choice for users looking for a dependable daily driver.

"""


class Review(BaseModel):
    key_themes : list[str] = Field(description='key themes covered in the review')
    summary : str = Field(description='summary of the review in a short manner')
    sentiment : Literal['positive','negative','neutral'] = Field(description='overall sentiment of the customer')
    pros : Optional[list[str]] = Field(default = None,description='positive points about the review')
    cons : Optional[list[str]] = Field(default=None,description='negative points in the review')

structured_template = model.with_structured_output(Review)

response = structured_template.invoke(review)
print(response)

json_output = response.model_dump_json()
print(json_output)