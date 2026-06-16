import os
from langchain_community.vectorstores import FAISS


def build_vector_store(chunks, embeddings):
    return FAISS.from_documents(chunks, embeddings)


def save_vector_store(vector_store, path="vector_db"):
    os.makedirs(path, exist_ok=True)
    vector_store.save_local(path)


def load_vector_store(embeddings, path="vector_db"):
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)


def build_and_save(source_dir="data/medical_documents", path="vector_db", embeddings=None):
    from src.ingestion import run_ingestion

    chunks = run_ingestion(source_dir)
    vector_store = build_vector_store(chunks, embeddings)
    save_vector_store(vector_store, path)
    return vector_store


if __name__ == "__main__":
    from src.embeddings import get_embeddings

    embeddings = get_embeddings()
    build_and_save(embeddings=embeddings)
