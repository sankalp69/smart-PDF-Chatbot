# ⚡ Quick Start Guide

**Get running in 3 minutes!**

## 🐳 Docker (Recommended)

```bash
# 1. Clone
git clone https://github.com/yourusername/smart-pdf-chatbot.git
cd smart-pdf-chatbot

# 2. Configure
cp .env.example .env
# Edit .env: add your GEMINI_API_KEY

# 3. Run
make init

# 4. Open
# http://localhost:8501
```

## 🐍 Python (Local)

```bash
# 1. Clone
git clone https://github.com/yourusername/smart-pdf-chatbot.git
cd smart-pdf-chatbot

# 2. Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Configure
cp .env.example .env
# Edit .env: add your GEMINI_API_KEY

# 4. Run
streamlit run app.py

# 5. Open
# http://localhost:8501
```

## 📚 Common Commands

### Docker
```bash
make run      # Start
make stop     # Stop
make logs     # View logs
make restart  # Restart
make help     # All commands
```

### Python
```bash
streamlit run app.py              # Start
python3 verify_setup.py           # Verify setup
```

## 🆘 Troubleshooting

**Port already in use?**
```bash
# Docker: edit docker-compose.yml, change port
# Python: streamlit run app.py --server.port=8080
```

**API key error?**
```bash
# Check .env file exists and has correct key
cat .env
```

**Docker not working?**
```bash
# Check Docker is running
docker --version
docker ps
```

## 📖 Full Documentation

- [README.md](README.md) - Complete guide
- [DOCKER_QUICKSTART.md](DOCKER_QUICKSTART.md) - Docker details
- [DEPLOYMENT_OPTIONS.md](DEPLOYMENT_OPTIONS.md) - All deployment methods

## 🎯 Next Steps

1. Upload PDFs
2. Ask questions
3. Enjoy AI-powered answers!

---

**Need help?** Check the documentation or open an issue on GitHub.
