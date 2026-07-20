from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to
exploring Mars, humanity continues to push the boundaries of what's possible beyond our
planet.

These missions have not only expanded our knowledge of the universe but have also 
contributed to advancements in technology here on Earth. Satellite communications, GPS, and 
even certain medical imaging techniques trace their roots back to innovations driven by 
space programs.
"""


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 80,
    chunk_overlap = 20
)

chunks = splitter.split_text(text)
print(chunks)
print('-'*30)
print(len(chunks))


# example from the image 

# from langchain_text_splitters import RecursiveCharacterTextSplitter

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 10,
#     chunk_overlap = 0
# )

# text = text = """My name is shravan
# I am 21 years old

# I live near panvel
# how are you"""


# result = splitter.split_text(text)


# for index,chunk in enumerate(result,1):
#     print(f'chunk {index}, length of the chunk is {len(chunk)}')
#     print(f'{chunk}')
#     print()
    
    
