# 🐳 Docker Deployment Guide

Complete guide for containerized deployment of Smart PDF Chatbot.

## 📋 Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed (included with Docker Desktop)
- Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

## 🚀 Quick Start

### Option 1: Using Docker Compose (Recommended)

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/smart-pdf-chatbot.git
cd smart-pdf-chatbot
```

2. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

3. **Build and run**
```bash
docker-compose up -d
```

4. **Access the app**
```
http://localhost:8501
```

### Option 2: Using Docker CLI

1. **Build the image**
```bash
docker build -t smart-pdf-chatbot .
```

2. **Run the container**
```bash
docker run -d \
  --name smart-pdf-chatbot \
  -p 8501:8501 \
  -e GEMINI_API_KEY=your_api_key_here \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/chat_history:/app/chat_history \
  -v $(pwd)/faiss_cache:/app/faiss_cache \
  smart-pdf-chatbot
```

3. **Access the app**
```
http://localhost:8501
```

## 📦 Docker Commands Reference

### Build & Run

```bash
# Build image
docker-compose build

# Start services
docker-compose up -d

# Start with rebuild
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### Container Management

```bash
# List running containers
docker ps

# View logs
docker logs smart-pdf-chatbot

# Follow logs in real-time
docker logs -f smart-pdf-chatbot

# Execute command in container
docker exec -it smart-pdf-chatbot bash

# Restart container
docker restart smart-pdf-chatbot

# Stop container
docker stop smart-pdf-chatbot

# Remove container
docker rm smart-pdf-chatbot
```

### Image Management

```bash
# List images
docker images

# Remove image
docker rmi smart-pdf-chatbot

# Prune unused images
docker image prune -a

# View image details
docker inspect smart-pdf-chatbot
```

## 🔧 Configuration

### Environment Variables

Edit `.env` file:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

### Port Configuration

To use a different port, edit `docker-compose.yml`:

```yaml
ports:
  - "8080:8501"  # Change 8080 to your desired port
```

Or with Docker CLI:

```bash
docker run -p 8080:8501 ...
```

### Volume Mounts

Data persistence is handled through volumes:

- `./data` - Uploaded PDF files
- `./chat_history` - Conversation history
- `./faiss_cache` - Vector embeddings cache

## 🌐 Production Deployment

### Deploy to Cloud Platforms

#### 1. AWS ECS/Fargate

```bash
# Build for ARM64 (Graviton)
docker buildx build --platform linux/arm64 -t smart-pdf-chatbot .

# Push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
docker tag smart-pdf-chatbot:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/smart-pdf-chatbot:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/smart-pdf-chatbot:latest
```

#### 2. Google Cloud Run

```bash
# Build and push
gcloud builds submit --tag gcr.io/PROJECT-ID/smart-pdf-chatbot

# Deploy
gcloud run deploy smart-pdf-chatbot \
  --image gcr.io/PROJECT-ID/smart-pdf-chatbot \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY=your_key
```

#### 3. Azure Container Instances

```bash
# Build and push to ACR
az acr build --registry myregistry --image smart-pdf-chatbot .

# Deploy
az container create \
  --resource-group myResourceGroup \
  --name smart-pdf-chatbot \
  --image myregistry.azurecr.io/smart-pdf-chatbot \
  --dns-name-label smart-pdf-chatbot \
  --ports 8501 \
  --environment-variables GEMINI_API_KEY=your_key
```

#### 4. DigitalOcean App Platform

```bash
# Push to Docker Hub
docker tag smart-pdf-chatbot yourusername/smart-pdf-chatbot
docker push yourusername/smart-pdf-chatbot

# Deploy via DigitalOcean UI or doctl
doctl apps create --spec .do/app.yaml
```

#### 5. Heroku

```bash
# Login to Heroku Container Registry
heroku container:login

# Build and push
heroku container:push web -a your-app-name

# Release
heroku container:release web -a your-app-name

# Set environment variables
heroku config:set GEMINI_API_KEY=your_key -a your-app-name
```

### Using Docker Hub

1. **Tag the image**
```bash
docker tag smart-pdf-chatbot yourusername/smart-pdf-chatbot:latest
```

2. **Push to Docker Hub**
```bash
docker login
docker push yourusername/smart-pdf-chatbot:latest
```

3. **Pull and run on any server**
```bash
docker pull yourusername/smart-pdf-chatbot:latest
docker run -d -p 8501:8501 -e GEMINI_API_KEY=your_key yourusername/smart-pdf-chatbot:latest
```

## 🔒 Security Best Practices

### 1. Never Commit Secrets

```bash
# Always use .env file (already in .gitignore)
echo "GEMINI_API_KEY=your_key" > .env
```

### 2. Use Docker Secrets (Swarm/Kubernetes)

```bash
# Create secret
echo "your_api_key" | docker secret create gemini_api_key -

# Use in docker-compose.yml
secrets:
  - gemini_api_key
```

### 3. Run as Non-Root User

Add to Dockerfile:

```dockerfile
RUN useradd -m -u 1000 appuser
USER appuser
```

### 4. Scan for Vulnerabilities

```bash
# Using Docker Scout
docker scout cves smart-pdf-chatbot

# Using Trivy
trivy image smart-pdf-chatbot
```

## 🔍 Troubleshooting

### Container Won't Start

```bash
# Check logs
docker logs smart-pdf-chatbot

# Check if port is already in use
lsof -i :8501

# Verify environment variables
docker exec smart-pdf-chatbot env | grep GEMINI
```

### Out of Memory

Edit `docker-compose.yml`:

```yaml
services:
  smart-pdf-chatbot:
    deploy:
      resources:
        limits:
          memory: 2G
        reservations:
          memory: 1G
```

### Slow Performance

```bash
# Increase shared memory
docker run --shm-size=2g ...

# Or in docker-compose.yml
shm_size: '2gb'
```

### Permission Issues

```bash
# Fix volume permissions
sudo chown -R $USER:$USER data/ chat_history/ faiss_cache/
```

## 📊 Monitoring

### Health Check

```bash
# Manual health check
curl http://localhost:8501/_stcore/health

# Container health status
docker inspect --format='{{.State.Health.Status}}' smart-pdf-chatbot
```

### Resource Usage

```bash
# Real-time stats
docker stats smart-pdf-chatbot

# Detailed info
docker inspect smart-pdf-chatbot
```

## 🧹 Cleanup

```bash
# Stop and remove everything
docker-compose down -v

# Remove all unused containers, networks, images
docker system prune -a

# Remove specific image
docker rmi smart-pdf-chatbot
```

## 🚀 Advanced: Multi-Stage Build

For smaller image size, use multi-stage build:

```dockerfile
# Builder stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["streamlit", "run", "app.py"]
```

## 📝 Docker Compose Profiles

For development vs production:

```yaml
services:
  smart-pdf-chatbot:
    profiles: ["prod"]
    # production config
  
  smart-pdf-chatbot-dev:
    profiles: ["dev"]
    # development config with hot reload
```

Run with:
```bash
docker-compose --profile prod up
```

## 🎯 Next Steps

- [ ] Set up CI/CD pipeline
- [ ] Configure reverse proxy (Nginx/Traefik)
- [ ] Add SSL/TLS certificates
- [ ] Set up monitoring (Prometheus/Grafana)
- [ ] Configure log aggregation
- [ ] Implement backup strategy

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Streamlit Docker Guide](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)
- [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

**Need help?** Open an issue on GitHub or check the troubleshooting section above.
