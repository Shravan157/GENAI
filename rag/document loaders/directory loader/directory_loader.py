from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# 1. Initialize the directory loader pointing to your folder
# Pass PyPDFLoader explicitly to handle .pdf files
loader = DirectoryLoader(
    path="./your_pdf_folder",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# 2. Trigger the generator using lazy_load()
pdf_iterator = loader.lazy_load()

# 3. Stream and process each page individually
for page in pdf_iterator:
    print(f"Source: {page.metadata['source']} | Page: {page.metadata.get('page')}")
    # Process text or add to vector store here without blowing up RAM
    print(page.page_content[:100]) 
