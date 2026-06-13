from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import OllamaEmbeddings

ollama_embeddings = OllamaEmbeddings(model="mxbai-embed-large:latest")

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next 
season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier
League (IPL) is the biggest cricket league in the world. People all over the world watch the 
matches and cheer for thier favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates
fear in cities and villages. When such attacks happen, they leave behind pain and 
sadness. To fight terrorism, we need strong laws, alert security forces, and support 
from people who care about peace and safety.
"""

splitter = SemanticChunker(
    embeddings=ollama_embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1,
)

chunks = splitter.create_documents([sample])
print(len(chunks))
print(chunks)

# ─────────────────────────────────────────────────────────────────────────────
# HOW SemanticChunker WORKS
# breakpoint_threshold_type="standard_deviation"
# breakpoint_threshold_amount=1
#
# NOTE: Numbers below are approximate example values.
# Actual values change depending on the embedding model.
# ─────────────────────────────────────────────────────────────────────────────
#
# STEP 1: Split text into sentences
#
#   SemanticChunker splits text using:
#       (?<=[.?!])\s+
#   Meaning: split after '.', '?', or '!' when followed by whitespace.
#
#   Example:
#       S1: Farmers were working hard in the fields...
#       S2: The sun was bright, and the air smelled of earth and fresh grass.
#       S3: The Indian Premier League (IPL) is the biggest cricket league...
#       S4: People all over the world watch the matches...
#       S5: Terrorism is a big danger to peace and safety.
#       S6: It causes harm to people and creates fear in cities and villages.
#       S7: When such attacks happen, they leave behind pain and sadness.
#       S8: To fight terrorism, we need strong laws, alert security forces...
#
# ─────────────────────────────────────────────────────────────────────────────
#
# STEP 2: Generate embeddings
#
#   Each sentence is converted into an embedding vector:
#       S1 -> embedding vector E1   (farming / agriculture)
#       S2 -> embedding vector E2   (weather / nature / field environment)
#       S3 -> embedding vector E3   (IPL / cricket)
#       S4 -> embedding vector E4   (IPL / fans / teams)
#       S5 -> embedding vector E5   (terrorism / safety)
#       S6 -> embedding vector E6   (terrorism / harm / fear)
#       S7 -> embedding vector E7   (terrorism / sadness / attacks)
#       S8 -> embedding vector E8   (terrorism / laws / security)
#
# ─────────────────────────────────────────────────────────────────────────────
#
# STEP 3: Compare neighboring sentences (cosine similarity)
#
#   Pair         | Meaning relation                     | Approx similarity
#   -------------|--------------------------------------|------------------
#   S1 <-> S2    | farming and field/nature             | 0.78
#   S2 <-> S3    | nature to cricket                    | 0.32
#   S3 <-> S4    | cricket to cricket fans              | 0.84
#   S4 <-> S5    | cricket to terrorism                 | 0.25
#   S5 <-> S6    | terrorism danger to harm/fear        | 0.86
#   S6 <-> S7    | harm/fear to attacks/sadness         | 0.80
#   S7 <-> S8    | attacks/sadness to anti-terrorism    | 0.76
#
#   Higher similarity = sentences are more related.
#
# ─────────────────────────────────────────────────────────────────────────────
#
# STEP 4: Convert similarity into distance
#
#   Formula: distance = 1 - cosine_similarity 
#
#   Pair         | Similarity | Distance
#   -------------|------------|----------
#   S1 <-> S2    |   0.78     |   0.22
#   S2 <-> S3    |   0.32     |   0.68
#   S3 <-> S4    |   0.84     |   0.16
#   S4 <-> S5    |   0.25     |   0.75
#   S5 <-> S6    |   0.86     |   0.14
#   S6 <-> S7    |   0.80     |   0.20
#   S7 <-> S8    |   0.76     |   0.24
#
#   Distance list: [0.22, 0.68, 0.16, 0.75, 0.14, 0.20, 0.24]
#   Large distance = topic may have changed.
#
# ─────────────────────────────────────────────────────────────────────────────
#
# STEP 5: Calculate mean distance
#
#   mean = (0.22 + 0.68 + 0.16 + 0.75 + 0.14 + 0.20 + 0.24) / 7
#        = 2.39 / 7
#        ≈ 0.34
#
# ─────────────────────────────────────────────────────────────────────────────
#
# STEP 6: Calculate standard deviation
#
#   Deviations from mean (0.34):
#       0.22 - 0.34 = -0.12
#       0.68 - 0.34 =  0.34
#       0.16 - 0.34 = -0.18
#       0.75 - 0.34 =  0.41
#       0.14 - 0.34 = -0.20
#       0.20 - 0.34 = -0.14
#       0.24 - 0.34 = -0.10
#
#   Squared deviations:
#       (-0.12)² = 0.0144
#       ( 0.34)² = 0.1156
#       (-0.18)² = 0.0324
#       ( 0.41)² = 0.1681
#       (-0.20)² = 0.0400
#       (-0.14)² = 0.0196
#       (-0.10)² = 0.0100
#
#   Variance = (0.0144 + 0.1156 + 0.0324 + 0.1681 + 0.0400 + 0.0196 + 0.0100) / 7
#            = 0.4001 / 7
#            ≈ 0.057
#
#   std = sqrt(0.057) ≈ 0.24
#
# ─────────────────────────────────────────────────────────────────────────────
#
# STEP 7: Calculate threshold
#
#   Formula: threshold = mean + (breakpoint_threshold_amount × std)
#          = 0.34 + (1 × 0.24)
#          = 0.58
#
# ─────────────────────────────────────────────────────────────────────────────
#
# STEP 8: Compare distances with threshold (0.58)
#
#   Pair         | Distance | Threshold | Split?
#   -------------|----------|-----------|-------
#   S1 <-> S2    |   0.22   |   0.58    | No
#   S2 <-> S3    |   0.68   |   0.58    | YES  <-- breakpoint
#   S3 <-> S4    |   0.16   |   0.58    | No
#   S4 <-> S5    |   0.75   |   0.58    | YES  <-- breakpoint
#   S5 <-> S6    |   0.14   |   0.58    | No
#   S6 <-> S7    |   0.20   |   0.58    | No
#   S7 <-> S8    |   0.24   |   0.58    | No
#
#   Breakpoints: After S2, After S4
#
# ─────────────────────────────────────────────────────────────────────────────
#
# STEP 9: Final chunks formed
#
#   Chunk 1 (S1 + S2) — Farming / field environment
#       "Farmers were working hard in the fields... The sun was bright..."
#
#   Chunk 2 (S3 + S4) — IPL / cricket
#       "The Indian Premier League (IPL) is the biggest cricket league...
#        People all over the world watch the matches..."
#
#   Chunk 3 (S5 + S6 + S7 + S8) — Terrorism / safety
#       "Terrorism is a big danger... It causes harm... When such attacks
#        happen... To fight terrorism, we need strong laws..."
#
# ─────────────────────────────────────────────────────────────────────────────
#
# FULL FLOW:
#
#   Text
#   -> Split into sentences using punctuation regex
#   -> Generate embeddings for each sentence
#   -> Calculate cosine similarity between neighboring sentences
#   -> Convert similarity into distance  (distance = 1 - similarity)
#   -> Calculate mean and standard deviation of all distances
#   -> threshold = mean + (amount × std)
#   -> Split wherever distance > threshold
#   -> Group sentences between breakpoints into chunks
#
# ─────────────────────────────────────────────────────────────────────────────

