import os
import streamlit as st
from src.embeddings import get_embeddings
from src.vector_store import build_and_save, load_vector_store
from src.llm_router import get_llm
from src.agent import build_agent
from src.drive_sync import download_folder, upload_folder

st.set_page_config(page_title="CareBot - AI Health Assistant", page_icon="🩺")

st.title("🩺 CareBot")
st.caption("AI-powered health information assistant. Not a substitute for professional medical advice.")

provider = st.sidebar.selectbox("LLM provider", ["openai", "gemini"])
embedding_provider = st.sidebar.selectbox("Embedding provider", ["openai", "gemini"])
vector_db_path = "vector_db"
drive_folder_id = os.getenv("GOOGLE_DRIVE_FOLDER_ID")


def index_exists(path):
    """A FAISS index saved with save_local() always writes index.faiss + index.pkl."""
    return os.path.isfile(os.path.join(path, "index.faiss")) and os.path.isfile(
        os.path.join(path, "index.pkl")
    )


if st.sidebar.button("Sync index from Google Drive"):
    if drive_folder_id:
        with st.spinner("Syncing index from Google Drive..."):
            download_folder(drive_folder_id, vector_db_path)
        st.sidebar.success("Synced index from Google Drive.")
    else:
        st.sidebar.error("GOOGLE_DRIVE_FOLDER_ID is not set.")

if st.sidebar.button("Rebuild index from documents"):
    with st.spinner("Rebuilding vector index from local documents..."):
        embeddings = get_embeddings(embedding_provider)
        build_and_save(embeddings=embeddings, path=vector_db_path)
    st.sidebar.success("Vector index rebuilt.")
    st.cache_resource.clear()
    if drive_folder_id:
        with st.spinner("Backing up index to Google Drive..."):
            upload_folder(vector_db_path, drive_folder_id)
        st.sidebar.success("Backed up index to Google Drive.")
    st.rerun()


@st.cache_resource
def load_agent(provider, embedding_provider, vector_db_path):
    embeddings = get_embeddings(embedding_provider)
    vector_store = load_vector_store(embeddings, vector_db_path)
    llm = get_llm(provider)
    return build_agent(vector_store, llm)


    st.warning(
        "No vector index found yet. This usually happens on a fresh deploy, "
        "since the index isn't committed to the repo.\n\n"
        "Build one of the two options below, then come back here to chat:"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Option A — Rebuild from documents**")
        st.caption("Uses the local files in `data/medical_documents/`.")
        if st.button("⚙️ Rebuild index now", type="primary"):
            with st.spinner("Embedding documents and building FAISS index..."):
                embeddings = get_embeddings(embedding_provider)
                build_and_save(embeddings=embeddings, path=vector_db_path)
            st.success("Index built. Reloading...")
            if drive_folder_id:
                with st.spinner("Backing up index to Google Drive..."):
                    upload_folder(vector_db_path, drive_folder_id)
            st.cache_resource.clear()
            st.rerun()

    with col2:
        st.markdown("**Option B — Restore from Google Drive**")
        if drive_folder_id:
            st.caption("Pulls a previously-built index from Drive.")
            if st.button("☁️ Sync from Google Drive"):
                with st.spinner("Downloading index from Google Drive..."):
                    download_folder(drive_folder_id, vector_db_path)
                st.cache_resource.clear()
                st.rerun()
        else:
            st.caption("Not configured — set `GOOGLE_DRIVE_FOLDER_ID` to enable this.")

    st.stop()



if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask a health question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        agent_executor = load_agent(provider, embedding_provider, vector_db_path)
        response = agent_executor.invoke({"input": user_input, "chat_history": []})
        answer = response["output"]
    except Exception as exc:
        answer = f"Something went wrong while answering: {exc}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
