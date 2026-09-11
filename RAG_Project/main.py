from google import genai
import numpy as np

client = genai.Client()

document = [
    "Refund requests are allowed within 7 days.",
    "Python classes happen monday to friday.",
    "Students get 3 interview opportunities.",
    "Course access is available for 6 months.",
]

question = "Can I get my money back after 5 days?"

# 1. Create document embeddings

document_vectors = []

for document in documents:
    result = client.models.embed_content(model="gemini-embedding-2", contents=document)

    vector = result.embeddings[0].values
    document_vectors.append(vector)

# 2. Create question embedding

question_result = client.models.embed_content(
    model="gemini-embedding-2", contents=question
)

question_vector = question_result.embeddings[0].values

# 3. Compare similarity


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


scores = []

for vector in document_vectors:
    score = cosine_similarity(question_vector, vector)
    scores.append(score)
# 4. Retrieve best chunk

best_index = np.argmax(scores)
best_document = document[best_index]

print("Retrieved Context: ")
print(best_document)

# 5. Send retrieved chunk to LLM

prompt = f"""
Answer the question using only the context below.

conduct:
{best_document}

Question:
{question}
"""

# 6: Generate final answer

response = client.models.generate_content(model="gemini-3.6-flash", contents=prompt)

print("\n Final Answer: ")
print(response.txt)
