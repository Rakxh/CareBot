from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import Tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

SYSTEM_PROMPT = (
    "You are CareBot, a careful and empathetic health information assistant. "
    "Use the search_medical_documents tool to retrieve relevant medical reference "
    "material before answering health-related questions. Always remind users that "
    "you are not a substitute for professional medical advice and recommend they "
    "consult a licensed clinician for diagnosis or treatment decisions."
)


def build_retrieval_tool(vector_store, k=4):
    retriever = vector_store.as_retriever(search_kwargs={"k": k})

    def search_medical_documents(query):
        results = retriever.invoke(query)
        return "\n\n".join(
            f"Source: {doc.metadata.get('source', 'unknown')}\n{doc.page_content}"
            for doc in results
        )

    return Tool(
        name="search_medical_documents",
        func=search_medical_documents,
        description="Search the medical knowledge base for relevant reference passages on symptoms, conditions, causes, and treatments.",
    )


def build_agent(vector_store, llm, k=4):
    tools = [build_retrieval_tool(vector_store, k=k)]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            MessagesPlaceholder("chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ]
    )

    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False,
        return_intermediate_steps=True,
    )
