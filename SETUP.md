# Quick Setup Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager

## Installation Steps

### 1. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
# OR
venv\Scripts\activate     # On Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Make sure your `.env` file contains your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage
1. Upload one or more PDF files using the file uploader
2. Wait for the vectorstore to be created (first time only)
3. Ask questions about your PDFs in the chat interface
4. Create new chat sessions or rename existing ones from the sidebar

## Troubleshooting

### If you get "command not found: python"
Use `python3` instead of `python`

### If embeddings download fails
The first run will download the sentence-transformers model (~80MB). Ensure you have a stable internet connection.

### If FAISS index fails to load
Delete the `faiss_cache/` folder and restart the app to rebuild the index.

## Project Structure
- `app.py` - Main Streamlit application
- `rag_pipeline.py` - RAG logic (retrieval + generation)
- `chat_gemini.py` - Gemini API integration
- `vectorstore_manager.py` - FAISS vector store management
- `history_manager.py` - Chat history persistence
- `session_manager.py` - Session management
- `data/` - Uploaded PDF files
- `chat_history/` - Saved chat sessions
- `faiss_cache/` - Cached vector embeddings
