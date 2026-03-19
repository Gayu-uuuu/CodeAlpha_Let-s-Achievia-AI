import json
import chromadb

client = chromadb.PersistentClient(path="vectorstore")

collection = client.get_or_create_collection("vettri_ai")

with open("data/student_faqs.json", "r") as f:
    data = json.load(f)

documents = []
ids = []

for i, item in enumerate(data):

    text = f"""
Question: {item['question']}
Answer: {item['answer']}
Category: {item['category']}
"""

    documents.append(text)
    ids.append(str(i))

collection.add(
    documents=documents,
    ids=ids
)

print("Knowledge base created successfully")