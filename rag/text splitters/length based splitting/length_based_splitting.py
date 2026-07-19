from langchain_text_splitters import CharacterTextSplitter

# =====================================================================
# STEP 1: DEFINE THE TEXT
# =====================================================================
text = """Morning fog rolls over the empty pitch,
Boots laced tight, the ritual begins.

Every sprint a debt paid to the past.
Sweat on the line, no room for doubt,

The whistle hasn't blown yet — but it will.
Legs remember what the mind forgets,

One more rep, one more breath, one more try."""

# =====================================================================
# STEP 2: SPLITTER RULES (what happens under the hood)
# =====================================================================
# Rule 1 - SEPARATOR FIRST: CharacterTextSplitter does NOT cut every N
#          characters. It first splits the whole text on a separator.
#          Default separator = "\n\n" (blank line).
#
# Rule 2 - RAW LENGTH: every character counts as 1, including \n.
#
# Rule 3 - CHUNK BUILDING: a piece joins the current chunk only if:
#          current_chunk_length + separator_length + next_piece_length <= chunk_size
#
# Rule 4 - OVERLAP: when a chunk closes, LangChain checks the LAST piece
#          in that chunk to see if it can carry forward as overlap.
#          If piece_length <= chunk_overlap -> carried forward.
#          If piece_length > chunk_overlap -> dropped, next chunk starts fresh (0 overlap).
#          LangChain never cuts a piece mid-way to force overlap.

splitter = CharacterTextSplitter(
    chunk_size = 150,      # max characters allowed per chunk
    chunk_overlap = 15     # max characters allowed to carry over between chunks
)

# =====================================================================
# STEP 3: WHAT split_text() DOES INTERNALLY
# =====================================================================
# text.split("\n\n") produces 4 pieces:
#
# Piece 1: "Morning fog rolls over the empty pitch,\nBoots laced tight, the ritual begins."
#          Length = 77
#
# Piece 2: "Every sprint a debt paid to the past.\nSweat on the line, no room for doubt,"
#          Length = 75
#
# Piece 3: "The whistle hasn't blown yet — but it will.\nLegs remember what the mind forgets,"
#          Length = 80
#
# Piece 4: "One more rep, one more breath, one more try."
#          Length = 44
#
# Separator "\n\n" = length 2

chunks = splitter.split_text(text)

# =====================================================================
# STEP 4: BUILDING CHUNK 1
# =====================================================================
# Add Piece 1 -> buffer = 77            -> 77 <= 150 -> OK, keep
# Try Piece 2 -> 77 + 2 + 75 = 154      -> 154 <= 150 -> FALSE, stop
# CHUNK 1 = Piece 1 only (77 chars)

# --- Overlap check before Chunk 2 ---
# Last piece in Chunk 1 = Piece 1 (77 chars)
# Is 77 <= chunk_overlap(15)? -> FALSE -> dropped, overlap resets to 0

# =====================================================================
# STEP 5: BUILDING CHUNK 2
# =====================================================================
# Start fresh with Piece 2 -> buffer = 75         -> 75 <= 150 -> OK, keep
# Try Piece 3 -> 75 + 2 + 80 = 157                -> 157 <= 150 -> FALSE, stop
# CHUNK 2 = Piece 2 only (75 chars)

# --- Overlap check before Chunk 3 ---
# Last piece in Chunk 2 = Piece 2 (75 chars)
# Is 75 <= chunk_overlap(15)? -> FALSE -> dropped, overlap resets to 0

# =====================================================================
# STEP 6: BUILDING CHUNK 3
# =====================================================================
# Start fresh with Piece 3 -> buffer = 80         -> 80 <= 150 -> OK, keep
# Try Piece 4 -> 80 + 2 + 44 = 126                -> 126 <= 150 -> TRUE, keep
# No pieces left -> CHUNK 3 finalized
# CHUNK 3 = Piece 3 + Piece 4 (126 chars)

# =====================================================================
# STEP 7: RESULT
# =====================================================================
# Total chunks = 3
# Chunk 1 = Piece 1              (77 chars)
# Chunk 2 = Piece 2              (75 chars)
# Chunk 3 = Piece 3 + Piece 4    (126 chars)
#
# Note: chunk_overlap=15 never actually applied, because every individual
# piece (77, 75, 80, 44) is bigger than 15. Overlap only works when at
# least one piece is smaller than chunk_overlap.

print(f"Total chunks created: {len(chunks)}")
print(f"Data container type: {type(chunks)}\n")

for index, chunk in enumerate(chunks, 1):
    print(f"--- FINAL CHUNK {index} (Length: {len(chunk)} characters) ---")
    print(repr(chunk))
    print()
