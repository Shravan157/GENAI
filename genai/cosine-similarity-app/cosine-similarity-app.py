from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os 
from sklearn.metrics.pairwise import cosine_similarity


load_dotenv()
os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv('HUGGINGFACEHUB_API_TOKEN')

embedding_model = HuggingFaceEndpointEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2"
)

input_query = 'Java is an programming language'

input_docs = [
    'India lies in the Asian subcontinent',
    'Virat Kohli is a cricket player',
    'I am learning python and langchain',
    'Apple a day keeps doctor away'
]

input_query_embeddings = embedding_model.embed_query(input_query)
input_docs_embeddings = embedding_model.embed_documents(input_docs)

scores = cosine_similarity([input_query_embeddings],input_docs_embeddings)[0]

index , score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(input_query)
print(input_docs[index])
print(f'similarity score is {score}')
