<div align="center">

# 🤖 Smart PDF Chatbot

### *AI-Powered Document Intelligence with RAG Technology*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://langchain.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Chat naturally with your PDF documents • Get accurate, context-aware answers • Powered by Gemini AI**

[Features](#-features) • [Demo](#-demo) • [Installation](#️-quick-start) • [Usage](#-usage) • [Tech Stack](#️-tech-stack)

</div>

---

## � FOverview

Transform the way you interact with documents! **Smart PDF Chatbot** leverages cutting-edge **Retrieval-Augmented Generation (RAG)** technology to let you have natural conversations with your PDF files. Upload your documents, ask questions, and get precise answers backed by your actual content.

### Why This Project?

- 🎯 **Accurate Answers**: Responses are grounded in your documents, not hallucinated
- � **ASmart Context**: Uses vector similarity search to find relevant information
- 🚀 **Fast & Efficient**: FAISS-powered vector store for lightning-fast retrieval
- 💬 **Session Management**: Save, rename, and manage multiple conversations
- 🎨 **Beautiful UI**: Modern, animated interface with smooth interactions
- 🔒 **Privacy First**: All processing happens locally with your API key

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 📄 Document Processing
- **Multi-PDF Upload**: Handle multiple documents simultaneously
- **Smart Chunking**: Intelligent text splitting for optimal retrieval
- **Auto-Caching**: FAISS index caching for faster subsequent loads
- **Change Detection**: Automatically rebuilds index when PDFs are updated

</td>
<td width="50%">

### 🧠 AI Intelligence
- **RAG Architecture**: Retrieval-Augmented Generation for accuracy
- **Gemini 2.5 Flash**: Powered by Google's latest AI model
- **Context-Aware**: Maintains conversation history
- **Honest Responses**: Clearly states when info isn't in documents

</td>
</tr>
<tr>
<td width="50%">

### 💬 Chat Experience
- **Session Management**: Create, rename, and switch between chats
- **Persistent History**: All conversations are automatically saved
- **Real-time Responses**: Fast answer generation
- **Intuitive Interface**: Clean, modern design with animations

</td>
<td width="50%">

### 🎨 Modern UI
- **Animated Gradients**: Smooth background transitions
- **Glowing Effects**: Eye-catching title and button animations
- **Responsive Design**: Works on all screen sizes
- **Dark Theme**: Easy on the eyes with blue-purple accents

</td>
</tr>
</table>

---

## 🎬 Demo

### Example Interaction

```
👤 User: "What is the main topic of this document?"

🤖 Bot: Based on the document, the main topic is [specific answer from PDF]...

👤 User: "Summarize the key points"

🤖 Bot: Here are the key points from your document:
     1. [Point from page X]
     2. [Point from page Y]
     3. [Point from page Z]
```

### Interface Preview

![Smart PDF Chatbot Interface](https://github.com/user-attachments/assets/d052de15-0347-4d4f-bd14-536440b4cad9)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                        │
│              (Streamlit Web Application)                 │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                   RAG Pipeline                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Retrieve   │→ │    Prompt    │→ │   Generate   │  │
│  │   Context    │  │  Construction│  │   Response   │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              Vector Store (FAISS Index)                  │
│         + HuggingFace Sentence Embeddings                │
└─────────────────────────────────────────────────────────┘
```

---

## ⚙️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Interactive web interface |
| **LLM** | Google Gemini 2.5 Flash | Answer generation |
| **Framework** | LangChain | RAG pipeline orchestration |
| **Embeddings** | HuggingFace Transformers | Text vectorization |
| **Vector DB** | FAISS | Similarity search |
| **PDF Parser** | PyPDF | Document loading |
| **State** | Streamlit Session State | Chat history management |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- Docker (optional, for containerized deployment)

### Installation

#### Option A: Docker (Recommended) 🐳

**Fastest way to get started!**

```bash
# 1. Clone repository
git clone https://github.com/yourusername/smart-pdf-chatbot.git
cd smart-pdf-chatbot

# 2. Set up environment
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# 3. Run with Docker Compose
docker-compose up -d

# 4. Access at http://localhost:8501
```

Or use the Makefile:
```bash
make init  # Build and run everything
```

See [DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md) for detailed Docker instructions.

#### Option B: Local Installation

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/smart-pdf-chatbot.git
cd smart-pdf-chatbot
```

2️⃣ **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
# OR
venv\Scripts\activate     # On Windows
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Configure API key**

Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_api_key_here
```

5️⃣ **Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Verify Setup (Optional)

```bash
python3 verify_setup.py
```

---

## 📖 Usage

1. **Upload PDFs**: Click the upload area and select one or more PDF files
2. **Wait for Processing**: The app will create embeddings (first time only)
3. **Ask Questions**: Type your question in the chat input
4. **Get Answers**: Receive AI-generated responses based on your documents
5. **Manage Sessions**: Create new chats or rename existing ones from the sidebar

### Tips for Best Results

- ✅ Ask specific questions about content in your PDFs
- ✅ Use clear, concise language
- ✅ Reference specific topics or sections when possible
- ❌ Avoid questions completely unrelated to your documents

---

## 🧩 Project Structure

```
smart-pdf-chatbot/
├── 📱 Application
│   ├── app.py                      # Main Streamlit application
│   ├── rag_pipeline.py             # RAG logic (retrieval + generation)
│   ├── chat_gemini.py              # Gemini API integration
│   ├── vectorstore_manager.py      # FAISS vector store management
│   ├── history_manager.py          # Chat history persistence
│   └── session_manager.py          # Session management
│
├── 🐳 Docker
│   ├── Dockerfile                  # Container definition
│   ├── docker-compose.yml          # Production compose
│   ├── docker-compose.dev.yml      # Development compose
│   ├── .dockerignore               # Docker ignore rules
│   └── Makefile                    # Docker commands
│
├── 📚 Documentation
│   ├── README.md                   # Main documentation
│   ├── SETUP.md                    # Local setup guide
│   ├── DOCKER_DEPLOYMENT.md        # Docker deployment guide
│   ├── GITHUB_SETUP.md             # GitHub setup guide
│   ├── QUICK_COMMANDS.md           # Command reference
│   └── DEPLOYMENT_CHECKLIST.md     # Deployment checklist
│
├── ⚙️ Configuration
│   ├── requirements.txt            # Python dependencies
│   ├── .env.example                # Environment template
│   ├── .env                        # API keys (not in repo)
│   └── .gitignore                  # Git ignore rules
│
├── 🧪 Tools
│   ├── verify_setup.py             # Setup verification
│   └── .github/workflows/          # CI/CD pipelines
│
├── 💾 Data (auto-created)
│   ├── data/                       # Uploaded PDF files
│   ├── chat_history/               # Saved conversations
│   └── faiss_cache/                # Cached embeddings
│
└── 📄 LICENSE                      # MIT License
```

---

## 🔄 How It Works

### 1. Document Processing
- PDFs are uploaded and stored in the `data/` folder
- LangChain's `PyPDFLoader` extracts text from each page
- Text is split into chunks using `RecursiveCharacterTextSplitter`

### 2. Embedding & Indexing
- Each chunk is converted to a vector using HuggingFace embeddings
- Vectors are stored in a FAISS index for fast similarity search
- Index is cached to disk for faster subsequent loads

### 3. Query Processing
- User question is embedded using the same model
- FAISS finds the top 3 most similar document chunks
- Chunks are combined with chat history to create context

### 4. Answer Generation
- Context + question is sent to Gemini AI
- LLM generates an answer grounded in the provided context
- Response is displayed and saved to chat history

---

## 🎨 UI Features

- **Animated Background**: Smooth gradient transitions
- **Glowing Title**: Eye-catching header with gradient text
- **Chat Bubbles**: Rounded, animated message containers
- **Hover Effects**: Interactive buttons and cards
- **Loading States**: Clear feedback during processing
- **Empty States**: Beautiful placeholders with helpful tips
- **Responsive Layout**: Adapts to different screen sizes

---

## 🐳 Docker Deployment

### Quick Docker Commands

```bash
# Using Makefile (easiest)
make build          # Build Docker image
make run            # Start application
make logs           # View logs
make stop           # Stop application
make restart        # Restart application
make clean          # Remove containers and images

# Using Docker Compose
docker-compose up -d              # Start in background
docker-compose logs -f            # Follow logs
docker-compose down               # Stop and remove
docker-compose ps                 # Show status

# Using Docker CLI
docker build -t smart-pdf-chatbot .
docker run -d -p 8501:8501 --env-file .env smart-pdf-chatbot
```

### Deploy to Cloud

**AWS ECS/Fargate:**
```bash
docker build -t smart-pdf-chatbot .
docker tag smart-pdf-chatbot:latest <account>.dkr.ecr.us-east-1.amazonaws.com/smart-pdf-chatbot
docker push <account>.dkr.ecr.us-east-1.amazonaws.com/smart-pdf-chatbot
```

**Google Cloud Run:**
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/smart-pdf-chatbot
gcloud run deploy --image gcr.io/PROJECT-ID/smart-pdf-chatbot --platform managed
```

**Heroku:**
```bash
heroku container:push web -a your-app-name
heroku container:release web -a your-app-name
```

See [DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md) for complete deployment guide.

---

## 🔧 Configuration

### Changing the LLM Model

Edit `chat_gemini.py`:
```python
self.model = genai.GenerativeModel("gemini-2.5-flash")  # Change model here
```

### Adjusting Chunk Size

Edit `vectorstore_manager.py`:
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,    # Adjust chunk size
    chunk_overlap=200   # Adjust overlap
)
```

### Modifying Retrieval Count

Edit `rag_pipeline.py`:
```python
docs = self.vectorstore.similarity_search(query, k=3)  # Change k value
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `command not found: python`
- **Solution**: Use `python3` instead of `python`

**Issue**: Embeddings download fails
- **Solution**: Ensure stable internet connection. First run downloads ~80MB model.

**Issue**: FAISS index fails to load
- **Solution**: Delete `faiss_cache/` folder and restart the app

**Issue**: API key error
- **Solution**: Verify `.env` file exists and contains valid `GEMINI_API_KEY`

**Issue**: Out of memory
- **Solution**: Reduce chunk size or process fewer PDFs at once

---

## 🚧 Future Enhancements

- [ ] Support for more document formats (DOCX, TXT, etc.)
- [ ] Multi-language support
- [ ] Export chat history to PDF/TXT
- [ ] Delete individual chat sessions
- [ ] Question suggestions based on document content
- [ ] Highlight source passages in PDFs
- [ ] Multi-user authentication
- [ ] Cloud deployment guide

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate tests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Chandan Aruk**
📊 Data Analyst | 💡 AI & Data Science Enthusiast

📧 Linkedin [https://linkedin.com/in/chandan-aruk]
