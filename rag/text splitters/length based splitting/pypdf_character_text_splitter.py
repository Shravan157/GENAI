from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Spring_vs_Spring_Boot.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 80,
    separator= '\n'
)

print(docs[0].page_content)
print('-'*50)
chunks = splitter.split_text(docs[0].page_content)
print(len(chunks))
print('-'*50)
print(chunks)

