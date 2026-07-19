from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="machine_learning_overview.pdf"
)

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap=100, # keep the chunk overlap 10-20 percent of the chunk-size
    separator = "\n\n"
)

result = splitter.split_documents(docs)

print(result[0].page_content)
print(result[1].page_content)
print(len(result))
