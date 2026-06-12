from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("IPL_Matches_2008_2022.csv")

result = loader.load()

print(len(result))
print(result[0].page_content)
print(result[0].metadata)