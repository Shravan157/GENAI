from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path=r"C:\Users\Shravan\Music\GEN AI\spring boot notes", # name of the directory
    glob='*.pdf', # format patter (fetch all the pdf files present in folder),
    loader_cls=PyPDFLoader # each file we find how to load it  
)

docs = loader.load()

docs = loader.load()

print(len(docs))
total_pages = docs[0].metadata['total_pages']
print(docs[0].metadata)
print(docs[0].metadata['source'])