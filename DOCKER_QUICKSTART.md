# 🐳 Docker Quick Start

Get your Smart PDF Chatbot running in 3 minutes!

## ⚡ Super Quick Start

```bash
# 1. Clone and enter directory
git clone https://github.com/yourusername/smart-pdf-chatbot.git
cd smart-pdf-chatbot

# 2. Set up API key
cp .env.example .env
echo "GEMINI_API_KEY=your_actual_key_here" > .env

# 3. Run!
make init
```

That's it! Open http://localhost:8501

## 📋 What You Need

- ✅ Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- ✅ Gemini API key ([Get key](https://makersuite.google.com/app/apikey))
- ✅ 5 minutes of your time

## 🎯 Three Ways to Run

### Method 1: Makefile (Easiest)

```bash
make init     # First time setup
make run      # Start
make stop     # Stop
make logs     # View logs
make restart  # Restart
```

### Method 2: Docker Compose

```bash
docker-compose up -d        # Start
docker-compose logs -f      # View logs
docker-compose down         # Stop
```

### Method 3: Docker CLI

```bash
docker build -t smart-pdf-chatbot .
docker run -d -p 8501:8501 --env-file .env smart-pdf-chatbot
```

## 🔧 Common Commands

```bash
# View running containers
docker ps

# View logs
make logs
# or
docker logs -f smart-pdf-chatbot

# Restart
make restart

# Stop
make stop

# Clean everything
make clean

# Rebuild from scratch
make rebuild
```

## 🌐 Access the App

Once running, open your browser:
- **Local**: http://localhost:8501
- **Network**: http://YOUR_IP:8501

## 📁 Data Persistence

Your data is saved in these folders:
- `data/` - Uploaded PDFs
- `chat_history/` - Conversations
- `faiss_cache/` - Vector embeddings

These persist even when you stop/restart the container!

## 🔒 Security Note

Never commit your `.env` file! It's already in `.gitignore`.

## 🆘 Troubleshooting

### Port Already in Use
```bash
# Use different port
docker run -p 8080:8501 ...
```

### Container Won't Start
```bash
# Check logs
make logs

# Verify API key
cat .env
```

### Out of Memory
```bash
# Increase Docker memory in Docker Desktop settings
# Preferences → Resources → Memory → 4GB+
```

### Permission Denied
```bash
# Fix permissions
sudo chown -R $USER:$USER data/ chat_history/ faiss_cache/
```

## 🚀 Deploy to Cloud

### Heroku (Free Tier Available)
```bash
heroku container:login
heroku create your-app-name
heroku container:push web
heroku container:release web
heroku config:set GEMINI_API_KEY=your_key
```

### Google Cloud Run (Free Tier Available)
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/smart-pdf-chatbot
gcloud run deploy --image gcr.io/PROJECT-ID/smart-pdf-chatbot
```

### DigitalOcean (From $5/month)
```bash
# Push to Docker Hub
docker tag smart-pdf-chatbot yourusername/smart-pdf-chatbot
docker push yourusername/smart-pdf-chatbot

# Deploy via DigitalOcean App Platform UI
```

## 📚 Next Steps

- Read [DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md) for advanced deployment
- Check [README.md](README.md) for full documentation
- See [Makefile](Makefile) for all available commands

## 💡 Pro Tips

1. **Use Makefile**: It's the easiest way - `make help` shows all commands
2. **Check logs**: If something's wrong, `make logs` is your friend
3. **Backup data**: Use `make backup` before major changes
4. **Monitor resources**: Use `make stats` to see CPU/memory usage

## 🎉 You're Done!

Your chatbot is now running in a container. Upload PDFs and start chatting!

---

**Questions?** Check [DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md) or open an issue on GitHub.
