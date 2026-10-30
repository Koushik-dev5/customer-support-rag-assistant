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


if __name__ == "__main__":
    loaded_documents = load_documents()

    for document in loaded_documents:
        print(f"Filename: {document['filename']}")
        print(f"Content: {document['content']}")
        print("-" * 40)