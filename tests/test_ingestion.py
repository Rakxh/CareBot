from src.ingestion import load_documents, chunk_documents, run_ingestion


def test_load_documents():
    documents = load_documents()
    assert len(documents) > 0


def test_chunk_documents():
    documents = load_documents()
    chunks = chunk_documents(documents, chunk_size=200, chunk_overlap=20)
    assert len(chunks) >= len(documents)
    assert all(len(chunk.page_content) <= 250 for chunk in chunks)


def test_run_ingestion():
    chunks = run_ingestion()
    assert len(chunks) > 0
    assert all(chunk.page_content for chunk in chunks)
