
from sentence_transformers import SentenceTransformer
from documents import load_documents, chunk_documents

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)

def generate_embedding(chunks):
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts)
    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding.tolist()
    return chunks

if __name__ == "__main__":
    documents = load_documents()
    chunks = chunk_documents(documents)
    embedded_chunks = generate_embedding(chunks)

    print("\nTotal embedded chunks:", len(embedded_chunks))
    print("embedding matrix shape:", (len(embedded_chunks), len(embedded_chunks[0]["embedding"])))
    print("Text:", embedded_chunks[0]["text"])
    print("vector dimensions:", len(embedded_chunks[0]["embedding"]))
    print("first five values:", embedded_chunks[0]["embedding"][:5])

for chunk in embedded_chunks:
    assert "filename" in chunk
    assert "text" in chunk
    assert "embedding" in chunk
    assert len(chunk["embedding"]) == 384

print("\nAll assertions passed. Each chunk contains 'filename', 'text', and 'embedding' with the correct dimensions.")