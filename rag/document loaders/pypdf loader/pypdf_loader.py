from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\Shravan\Music\starting_genai\rag\document loaders\pypdf loader\Spring_vs_Spring_Boot.pdf')

result = loader.load()

print(result)
print('-'*50)
print(result[0].page_content)
print('-'*50)
print(result[0].metadata)