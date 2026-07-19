from langchain_text_splitters import CharacterTextSplitter

text = """Morning fog rolls over the empty pitch,
Boots laced tight, the ritual begins.

Every sprint a debt paid to the past.
Sweat on the line, no room for doubt,

The whistle hasn't blown yet — but it will.
Legs remember what the mind forgets,

One more rep, one more breath, one more try."""


splitter = CharacterTextSplitter(
    chunk_size = 150,      # Max target character budget per chunk
    chunk_overlap = 15     # Max character budget allowed for continuity overlap
)

chunks = splitter.split_text(text)

print(f"Total chunks created: {len(chunks)}")
print(f"Data container type: {type(chunks)}\n")

for index, chunk in enumerate(chunks, 1):
    print(f"--- FINAL CHUNK {index} (Length: {len(chunk)} characters) ---")
    print(chunk) # repr shows raw formatting structure like \n
    print()
