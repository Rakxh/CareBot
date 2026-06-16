from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_documents(source_dir="data/medical_documents"):
    loader = DirectoryLoader(source_dir, glob="*.txt", loader_cls=TextLoader)
    return loader.load()


def chunk_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " "],
    )
    return splitter.split_documents(documents)


def run_ingestion(source_dir="data/medical_documents", chunk_size=500, chunk_overlap=50):
    documents = load_documents(source_dir)
    chunks = chunk_documents(documents, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return chunks


if __name__ == "__main__":
    chunks = run_ingestion()
    print(f"Loaded documents and produced {len(chunks)} chunks")
