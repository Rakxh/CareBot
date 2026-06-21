import os


def get_llm(provider=None, temperature=0.2):
    provider = provider or os.getenv("LLM_PROVIDER", "openai")

    if provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model="gpt-4o-mini", temperature=temperature)

    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
      
        return ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=temperature)

    raise ValueError(f"Unsupported LLM provider: {provider}")
