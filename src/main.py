from documents import load_documents


def main():
    print("Customer Support RAG Assistant")

    documents = load_documents()

    print("Number of documents:", len(documents))
    print("Loaded filenames:", [doc["filename"] for doc in documents])


if __name__ == "__main__":
    main()
