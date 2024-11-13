import os
from pinecone import Pinecone, ServerlessSpec

# Step 1: Initialize Pinecone with your API key
api_key = os.environ.get("PINECONE_API_KEY", "b4b590d9-6eed-498d-af10-d11d92bbda04")  # Replace with actual API key or use environment variable
pc = Pinecone(api_key=api_key)

# Step 2: Check and Create an Index
index_name = "sample-index"
dimension = 128  # Make sure this dimension is consistently used
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric="euclidean",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-west-2"  # Free-tier region for AWS
        )
    )
print(f"Index '{index_name}' created.")

# Step 3: Use the Index
index = pc.Index(index_name)

# Step 4: Insert Data into the Index
# Ensure each 'values' list has exactly 128 dimensions
data = [
    {"id": "item1", "values": [0.1, 0.2, 0.3] * (dimension // 3) + [0.1] * (dimension % 3)},  # Padding to 128 elements
    {"id": "item2", "values": [0.4, 0.5, 0.6] * (dimension // 3) + [0.4] * (dimension % 3)}   # Padding to 128 elements
]
index.upsert(vectors=data)
print("Data upserted into index.")

# Step 5: Query the Index
query_vector = [0.1, 0.2, 0.3] * (dimension // 3) + [0.1] * (dimension % 3)  # Padding to 128 elements
query_result = index.query(vector=query_vector, top_k=1)
print("Query result:", query_result)

# Step 6: Clean Up by Deleting the Index
pc.delete_index(index_name)
print(f"Index '{index_name}' deleted.")
