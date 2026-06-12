from langchain_text_splitters import CharacterTextSplitter

text = """
The whistle blows, the crowd takes flight,
Under the stadium's glowing light.

Chasing dreams in every scene.
The captain lifts his voice to speak,

This match isn't lost — it's barely begun.*
And something shifts, the tide turns slow,
"""

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 10
)

chunks = splitter.split_text(text)

print(chunks) # returns all the chunks
print(type(chunks)) # list
print(len(chunks)) # total chunks created 


"""
Point to remember we can use seperater to seperate the 
chunks as per our need, but if the seperator is not mentioned
then the default seperator is \n\n

The character text splitter does not split by the number of 
characters a text has it seperates by lines or \n\n

The text in the given example has three blank lines 
which denote \n\n so the character text splitter will 
try to split them with that blank lines 
"""
# Given:
# chunk_size = 200
# chunk_overlap = 10
# separator = "\n\n"

# Original text is divided into 3 pieces because pieces are separated by "\n\n"

# piece1:
# "The whistle blows, the crowd takes flight,\nUnder the stadium's glowing light."
# length = 89

# piece2:
# "Chasing dreams in every scene.\nThe captain lifts his voice to speak,"
# length = 68

# piece3:
# "This match isn't lost — it's barely begun.*\nAnd something shifts, the tide turns slow,"
# length = 86


# Step 1:
# Start creating chunk1 by adding piece1.
# Current chunk1 length = 89
# Since 89 <= chunk_size(200), piece1 is added to chunk1.


# Step 2:
# Try adding piece2 to chunk1.
# Formula:
# piece1 + separator + piece2
# 89 + 2 + 68 = 159
# Since 159 <= chunk_size(200), piece2 is also added to chunk1.


# Step 3:
# Try adding piece3 to chunk1.
# Formula:
# piece1 + separator + piece2 + separator + piece3
# 89 + 2 + 68 + 2 + 86 = 247
# Since 247 > chunk_size(200), piece3 cannot be added to chunk1.
# Therefore, chunk1 is finalized.


# Final chunk1:
# "The whistle blows, the crowd takes flight,\nUnder the stadium's glowing light.\n\nChasing dreams in every scene.\nThe captain lifts his voice to speak,"
# chunk1 length = 159


# Step 4:
# Now prepare overlap for chunk2.
# Previous chunk contains:
# [piece1, piece2]
#
# To create overlap, remove the oldest piece first.
# Remove piece1.
# Remaining piece = piece2
# piece2 length = 68
#
# Check overlap:
# 68 <= chunk_overlap(10)  -> False
#
# Since piece2 is larger than the allowed overlap,
# it cannot be carried forward to chunk2.
# So there is no overlap for chunk2.


# Step 5:
# Start creating chunk2 with piece3.
# Current chunk2 length = 86
# Since 86 <= chunk_size(200), piece3 is added to chunk2.
# No more pieces are left, so chunk2 is finalized.


# Final chunk2:
# "This match isn't lost — it's barely begun.*\nAnd something shifts, the tide turns slow,"
# chunk2 length = 86


# Final output:
# chunk1 =
# "The whistle blows, the crowd takes flight,\nUnder the stadium's glowing light.\n\nChasing dreams in every scene.\nThe captain lifts his voice to speak,"
#
# chunk2 =
# "This match isn't lost — it's barely begun.*\nAnd something shifts, the tide turns slow,"


# Important note:
# No overlap happens in this example.
# Reason:
# After finalizing chunk1, the possible overlap candidate is piece2.
# But piece2 has 68 characters, and chunk_overlap is only 10.
# Since 68 > 10, piece2 cannot be used as overlap.