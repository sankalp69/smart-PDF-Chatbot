import streamlit as st
from rag_pipeline import RAGPipeline
from session_manager import SessionManager
from history_manager import HistoryManager
import os

# -------------------------------
# Streamlit Page Configuration
# -------------------------------
st.set_page_config(
    page_title="📄 PDF Chatbot",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Enhanced Modern UI Styling
# -------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Global App Styling */
* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

body {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #e2e8f0;
}

/* Streamlit Main Container */
.main {
    background: linear-gradient(145deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.95));
    padding: 2rem;
    border-radius: 1.5rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(10px);
}

/* Animated gradient background */
.stApp {
    background: linear-gradient(-45deg, #0f172a, #1e293b, #0f172a, #1e3a5f);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Title with glow effect */
h1 {
    text-align: center;
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 2.8rem !important;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin-bottom: 0.5rem;
    text-shadow: 0 0 40px rgba(56, 189, 248, 0.3);
    animation: titleGlow 3s ease-in-out infinite;
}

@keyframes titleGlow {
    0%, 100% { filter: brightness(1); }
    50% { filter: brightness(1.2); }
}

/* Sidebar Enhancement */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(15, 23, 42, 0.98) 0%, rgba(30, 41, 59, 0.98) 100%);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(56, 189, 248, 0.2);
    box-shadow: 4px 0 24px rgba(0, 0, 0, 0.3);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 2rem;
}

/* Sidebar header */
[data-testid="stSidebar"] h1 {
    font-size: 1.4rem !important;
    color: #38bdf8;
    margin-bottom: 1.5rem;
}

/* Radio buttons styling */
[data-testid="stSidebar"] .row-widget.stRadio > div {
    background: rgba(30, 41, 59, 0.6);
    padding: 0.8rem;
    border-radius: 0.8rem;
    border: 1px solid rgba(56, 189, 248, 0.1);
    transition: all 0.3s ease;
}

[data-testid="stSidebar"] .row-widget.stRadio > div:hover {
    background: rgba(56, 189, 248, 0.1);
    border-color: rgba(56, 189, 248, 0.3);
    transform: translateX(4px);
}

/* Enhanced Buttons */
.stButton > button {
    background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
    color: white;
    border: none;
    border-radius: 0.75rem;
    padding: 0.6rem 1.5rem;
    font-weight: 600;
    font-size: 0.95rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    width: 100%;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #2563eb 0%, #7c3aed 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
}

.stButton > button:active {
    transform: translateY(0);
}

/* File uploader enhancement */
[data-testid="stFileUploader"] {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.8) 100%);
    border: 2px dashed rgba(56, 189, 248, 0.4);
    border-radius: 1.2rem;
    padding: 2rem;
    transition: all 0.3s ease;
}

[data-testid="stFileUploader"]:hover {
    border-color: rgba(56, 189, 248, 0.7);
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.9) 100%);
    box-shadow: 0 8px 24px rgba(56, 189, 248, 0.2);
}

/* Chat message bubbles with animation */
.stChatMessage {
    padding: 1.2rem 1.5rem;
    border-radius: 1.2rem;
    margin: 0.8rem 0;
    line-height: 1.6;
    animation: messageSlideIn 0.4s ease-out;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

@keyframes messageSlideIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* User messages */
.stChatMessage[data-testid="user"] {
    background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
    color: white;
    margin-left: 2rem;
    border-bottom-right-radius: 0.3rem;
}

/* Assistant messages */
.stChatMessage[data-testid="assistant"] {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.95) 0%, rgba(51, 65, 85, 0.95) 100%);
    color: #e2e8f0;
    margin-right: 2rem;
    border-bottom-left-radius: 0.3rem;
    border-left: 3px solid #38bdf8;
}

/* Chat input enhancement */
[data-testid="stChatInputContainer"] {
    background: linear-gradient(180deg, transparent 0%, rgba(15, 23, 42, 0.98) 20%);
    border-top: 1px solid rgba(56, 189, 248, 0.2);
    padding: 1.5rem 0 1rem 0;
    backdrop-filter: blur(10px);
}

[data-testid="stChatInput"] textarea {
    background: rgba(30, 41, 59, 0.9) !important;
    color: #e2e8f0 !important;
    border: 2px solid rgba(56, 189, 248, 0.3) !important;
    border-radius: 1rem !important;
    padding: 1rem !important;
    font-size: 0.95rem !important;
    transition: all 0.3s ease !important;
}

[data-testid="stChatInput"] textarea:focus {
    border-color: rgba(56, 189, 248, 0.6) !important;
    box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.1) !important;
}

/* Text input styling */
.stTextInput > div > div > input {
    background: rgba(30, 41, 59, 0.8);
    color: #e2e8f0;
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 0.7rem;
    padding: 0.6rem 1rem;
    transition: all 0.3s ease;
}

.stTextInput > div > div > input:focus {
    border-color: rgba(56, 189, 248, 0.6);
    box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.1);
}

/* Info/Warning/Error boxes */
.stAlert {
    background: rgba(30, 41, 59, 0.8);
    border-radius: 1rem;
    border-left: 4px solid;
    padding: 1rem 1.5rem;
    backdrop-filter: blur(10px);
}

.stInfo {
    border-left-color: #38bdf8;
    background: linear-gradient(135deg, rgba(56, 189, 248, 0.1) 0%, rgba(30, 41, 59, 0.8) 100%);
}

.stSuccess {
    border-left-color: #10b981;
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(30, 41, 59, 0.8) 100%);
}

.stWarning {
    border-left-color: #f59e0b;
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(30, 41, 59, 0.8) 100%);
}

/* Caption text */
.stCaption {
    color: #94a3b8;
    font-size: 0.9rem;
    text-align: center;
    margin-bottom: 1.5rem;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

::-webkit-scrollbar-track {
    background: rgba(15, 23, 42, 0.5);
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #3b82f6, #8b5cf6);
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #2563eb, #7c3aed);
}

/* Loading spinner */
.stSpinner > div {
    border-top-color: #38bdf8 !important;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Initialize Session State
# -------------------------------
if "sessions" not in st.session_state:
    st.session_state.sessions = {}  # stores all session histories

if "session_manager" not in st.session_state:
    st.session_state.session_manager = SessionManager(st.session_state.sessions)

if "active_session" not in st.session_state:
    st.session_state.active_session = st.session_state.session_manager.create_session()

if "chat_history" not in st.session_state:
    # link chat_history to the active session
    st.session_state.chat_history = st.session_state.sessions[st.session_state.active_session]

if "last_user_query" not in st.session_state:
    st.session_state.last_user_query = None

# -------------------------------
# Sidebar: Chat Sessions
# -------------------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0 1.5rem 0; border-bottom: 1px solid rgba(56,189,248,0.2);">
        <h2 style="color: #38bdf8; font-size: 1.5rem; margin: 0; font-weight: 700;">
            💬 Chat Sessions
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    # New Chat Button at top
    if st.button("➕ New Chat", use_container_width=True, type="primary"):
        new_session = st.session_state.session_manager.create_session()
        st.session_state.active_session = new_session
        st.session_state.chat_history = st.session_state.sessions[new_session]
        st.rerun()
    
    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)
    
    sessions = list(st.session_state.sessions.keys())
    
    # Session selection
    if sessions:
        st.markdown("""
        <div style="margin-bottom: 1rem;">
            <p style='font-size: 0.9rem; font-weight: 600; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em;'>
                Your Conversations
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        selected = st.radio(
            "Select conversation",
            sessions,
            index=sessions.index(st.session_state.active_session),
            label_visibility="collapsed"
        )
        
        st.session_state.active_session = selected
        st.session_state.chat_history = st.session_state.sessions[selected]
        
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        
        # Rename section
        with st.expander("✏️ Rename Chat", expanded=False):
            new_name = st.text_input(
                "New name",
                value=selected,
                key=f"rename_input_{selected}",
                label_visibility="collapsed"
            )
            if st.button("💾 Save", use_container_width=True):
                updated_name = st.session_state.session_manager.rename_session(selected, new_name)
                st.session_state.active_session = updated_name
                st.session_state.chat_history = st.session_state.sessions[updated_name]
                st.success(f"✓ Renamed!")
                st.rerun()
    else:
        st.markdown("""
        <div style="
            text-align: center;
            padding: 2rem 1rem;
            color: #64748b;
            background: rgba(30, 41, 59, 0.5);
            border-radius: 0.8rem;
            border: 1px dashed rgba(56,189,248,0.2);
        ">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">📝</div>
            <p style="font-size: 0.9rem; margin: 0;">
                No chats yet.<br/>Start a new conversation!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer info
    st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        text-align: center;
        padding: 1rem;
        border-top: 1px solid rgba(56,189,248,0.2);
        color: #64748b;
        font-size: 0.8rem;
    ">
        <div style="margin-bottom: 0.5rem;">🚀 Powered by</div>
        <div style="color: #38bdf8; font-weight: 600;">Gemini AI & FAISS</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# Main Title & Header
# -------------------------------
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <h1 style="margin-bottom: 0.5rem;">🤖 Smart PDF Chatbot</h1>
    <p style="color: #94a3b8; font-size: 1.1rem; margin: 0;">
        Powered by AI • RAG Technology • Gemini 2.5
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(56,189,248,0.15) 0%, rgba(139,92,246,0.15) 100%);
    border: 2px solid rgba(56,189,248,0.3);
    padding: 1.2rem 1.5rem;
    border-radius: 1rem;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 4px 16px rgba(56,189,248,0.2);
">
    <div style="font-size: 1.1rem; color: #e2e8f0; font-weight: 600; margin-bottom: 0.5rem;">
        ✨ Intelligent Document Q&A
    </div>
    <div style="color: #94a3b8; font-size: 0.95rem;">
        Upload your PDFs and get accurate answers grounded in your documents
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# File Upload Section
# -------------------------------
st.markdown("""
<div style="margin-bottom: 1rem;">
    <h3 style="color: #38bdf8; font-size: 1.3rem; font-weight: 600; margin-bottom: 0.5rem;">
        📚 Upload Your Documents
    </h3>
    <p style="color: #94a3b8; font-size: 0.9rem; margin: 0;">
        Drag and drop or click to browse • Supports multiple PDFs
    </p>
</div>
""", unsafe_allow_html=True)

uploaded_files = st.file_uploader(
    "Upload PDF files",
    accept_multiple_files=True,
    type="pdf",
    label_visibility="collapsed"
)

if uploaded_files:
    # Show uploaded files info
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(16,185,129,0.1) 0%, rgba(30,41,59,0.8) 100%);
        border-left: 4px solid #10b981;
        padding: 1rem 1.5rem;
        border-radius: 0.8rem;
        margin-bottom: 1.5rem;
    ">
        <div style="color: #10b981; font-weight: 600; margin-bottom: 0.3rem;">
            ✓ {len(uploaded_files)} PDF{'s' if len(uploaded_files) > 1 else ''} Loaded
        </div>
        <div style="color: #94a3b8; font-size: 0.85rem;">
            {', '.join([f.name for f in uploaded_files])}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    pdf_paths = []
    os.makedirs("data", exist_ok=True)
    for file in uploaded_files:
        file_path = os.path.join("data", file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        pdf_paths.append(file_path)

    # Initialize persistent pipeline and history manager
    if "pipeline" not in st.session_state or st.session_state.pipeline is None:
        with st.spinner("🔄 Processing documents and building knowledge base..."):
            st.session_state.pipeline = RAGPipeline(st.session_state.active_session, pdf_paths)
            st.session_state.history_manager = HistoryManager(st.session_state.active_session)
            # Load existing history for the active session
            st.session_state.chat_history = st.session_state.history_manager.load_history()

    pipeline = st.session_state.pipeline
    history_manager = st.session_state.history_manager

    # -------------------------------
    # Display Previous Chat
    # -------------------------------
    if len(st.session_state.chat_history) == 0:
        st.markdown("""
        <div style="
            text-align: center;
            padding: 4rem 2rem;
            color: #64748b;
        ">
            <div style="font-size: 4rem; margin-bottom: 1rem; opacity: 0.5;">💬</div>
            <h3 style="color: #94a3b8; font-weight: 600; margin-bottom: 0.5rem;">
                Ready to Chat!
            </h3>
            <p style="color: #64748b; font-size: 0.95rem;">
                Ask any question about your uploaded documents below
            </p>
            <div style="margin-top: 2rem; display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <span style="background: rgba(56,189,248,0.1); padding: 0.5rem 1rem; border-radius: 0.5rem; font-size: 0.85rem;">
                    💡 Try: "Summarize this document"
                </span>
                <span style="background: rgba(139,92,246,0.1); padding: 0.5rem 1rem; border-radius: 0.5rem; font-size: 0.85rem;">
                    🔍 Try: "What are the key points?"
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # -------------------------------
    # Chat Input
    # -------------------------------
    user_query = st.chat_input("💭 Ask a question about your PDFs...")

    if user_query:
        # Avoid duplicate processing on rerun
        if user_query != st.session_state.get("last_user_query", None):
            st.session_state.last_user_query = user_query

            with st.chat_message("user"):
                st.markdown(user_query)

            answer = pipeline.ask(user_query)

            with st.chat_message("assistant"):
                st.markdown(answer)

            # Save to history manager
            history_manager.save_turn("user", user_query)
            history_manager.save_turn("assistant", answer)

            # Update session-specific chat history
            st.session_state.chat_history.append({"role": "user", "content": user_query})
            st.session_state.chat_history.append({"role": "assistant", "content": answer})
            st.session_state.sessions[st.session_state.active_session] = st.session_state.chat_history

            # 🧠 Auto-rename session based on first question
            if "Untitled Chat" in st.session_state.active_session or st.session_state.active_session.startswith("session_"):
                suggested_name = user_query.split(" ")[0].capitalize() + " Chat"
                new_name = st.session_state.session_manager.rename_session(
                    st.session_state.active_session, suggested_name
                )
                st.session_state.active_session = new_name
                st.session_state.chat_history = st.session_state.sessions[new_name]
        else:
            st.stop()
else:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(56,189,248,0.1) 0%, rgba(139,92,246,0.1) 100%);
        border: 2px dashed rgba(56,189,248,0.3);
        padding: 3rem 2rem;
        border-radius: 1.2rem;
        text-align: center;
        margin-top: 2rem;
    ">
        <div style="font-size: 3.5rem; margin-bottom: 1rem;">📄</div>
        <h3 style="color: #38bdf8; font-weight: 600; margin-bottom: 0.8rem; font-size: 1.4rem;">
            No Documents Uploaded Yet
        </h3>
        <p style="color: #94a3b8; font-size: 1rem; margin-bottom: 1.5rem;">
            Upload your PDF files above to start an intelligent conversation
        </p>
        <div style="display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap; margin-top: 1.5rem;">
            <div style="background: rgba(30,41,59,0.6); padding: 1rem 1.5rem; border-radius: 0.8rem; max-width: 200px;">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🧠</div>
                <div style="color: #e2e8f0; font-weight: 600; font-size: 0.9rem;">AI-Powered</div>
                <div style="color: #64748b; font-size: 0.8rem;">Smart answers</div>
            </div>
            <div style="background: rgba(30,41,59,0.6); padding: 1rem 1.5rem; border-radius: 0.8rem; max-width: 200px;">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⚡</div>
                <div style="color: #e2e8f0; font-weight: 600; font-size: 0.9rem;">Fast Search</div>
                <div style="color: #64748b; font-size: 0.8rem;">Vector-based</div>
            </div>
            <div style="background: rgba(30,41,59,0.6); padding: 1rem 1.5rem; border-radius: 0.8rem; max-width: 200px;">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">💾</div>
                <div style="color: #e2e8f0; font-weight: 600; font-size: 0.9rem;">Auto-Save</div>
                <div style="color: #64748b; font-size: 0.8rem;">Chat history</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
