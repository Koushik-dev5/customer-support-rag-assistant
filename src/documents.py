
from pathlib import Path


def load_documents():
    project_root = Path(__file__).resolve().parent.parent
    folder = project_root / "data" / "documents"

    documents = []

    for file in folder.glob("*.txt"):
        content = file.read_text(encoding="utf-8")

        document = {
            "filename": file.name,
            "content": content
        }

        documents.append(document)

    return documents


def chunk_documents(documents):
    chunks = []

    chunk_size = 2
    overlap = 1
    step = chunk_size - overlap

    for document in documents:
        filename = document["filename"]
        content = document["content"]

        sentences = content.split(".")

        sentences = [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]

        for start in range(0, len(sentences), step):
            chunk_sentences = sentences[start:start + chunk_size]

            # Skip incomplete final chunks
            if len(chunk_sentences) < chunk_size:
                continue

            chunk_text = ". ".join(chunk_sentences) + "."

            chunks.append({
                "filename": filename,
                "text": chunk_text
            })

    return chunks


if __name__ == "__main__":

    loaded_documents = load_documents()

    print("Total documents:", len(loaded_documents))
    print("-" * 40)

    chunks = chunk_documents(loaded_documents)

    print("Total chunks:", len(chunks))
    print("-" * 40)

    for index, chunk in enumerate(chunks, start=1):
        print(f"Chunk ID: {index}")
        print(f"Filename: {chunk['filename']}")
        print(f"Text: {chunk['text']}")
        print("-" * 40)
