import os


def get_embeddings(provider=None):
    provider = provider or os.getenv("EMBEDDING_PROVIDER", "openai")

    if provider == "openai":
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(model="text-embedding-3-small")

    if provider == "gemini":
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
       
        return GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    raise ValueError(f"Unsupported embedding provider: {provider}")
