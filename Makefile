.PHONY: help build run stop restart logs clean test shell health

# Variables
IMAGE_NAME = smart-pdf-chatbot
CONTAINER_NAME = smart-pdf-chatbot
PORT = 8501

# Colors for output
BLUE = \033[0;34m
GREEN = \033[0;32m
RED = \033[0;31m
NC = \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)Smart PDF Chatbot - Docker Commands$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

build: ## Build Docker image
	@echo "$(BLUE)Building Docker image...$(NC)"
	docker-compose build
	@echo "$(GREEN)✓ Build complete$(NC)"

run: ## Run the application
	@echo "$(BLUE)Starting application...$(NC)"
	docker-compose up -d
	@echo "$(GREEN)✓ Application running at http://localhost:$(PORT)$(NC)"

stop: ## Stop the application
	@echo "$(BLUE)Stopping application...$(NC)"
	docker-compose down
	@echo "$(GREEN)✓ Application stopped$(NC)"

restart: stop run ## Restart the application

logs: ## View application logs
	docker-compose logs -f

logs-tail: ## View last 100 lines of logs
	docker-compose logs --tail=100

shell: ## Open shell in container
	docker exec -it $(CONTAINER_NAME) /bin/bash

health: ## Check application health
	@curl -f http://localhost:$(PORT)/_stcore/health && echo "$(GREEN)✓ Healthy$(NC)" || echo "$(RED)✗ Unhealthy$(NC)"

ps: ## Show running containers
	docker-compose ps

stats: ## Show container resource usage
	docker stats $(CONTAINER_NAME)

clean: ## Remove containers and images
	@echo "$(BLUE)Cleaning up...$(NC)"
	docker-compose down -v
	docker rmi $(IMAGE_NAME) 2>/dev/null || true
	@echo "$(GREEN)✓ Cleanup complete$(NC)"

clean-all: clean ## Remove everything including volumes
	@echo "$(BLUE)Removing all data...$(NC)"
	rm -rf data/* chat_history/* faiss_cache/*
	@echo "$(GREEN)✓ All data removed$(NC)"

rebuild: clean build run ## Clean, rebuild and run

test: ## Run setup verification
	docker exec $(CONTAINER_NAME) python verify_setup.py

dev: ## Run in development mode with hot reload
	@echo "$(BLUE)Starting in development mode...$(NC)"
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

prod: ## Run in production mode
	@echo "$(BLUE)Starting in production mode...$(NC)"
	docker-compose up -d
	@echo "$(GREEN)✓ Production deployment complete$(NC)"

push: ## Push image to Docker Hub (set DOCKER_USERNAME first)
	@if [ -z "$(DOCKER_USERNAME)" ]; then \
		echo "$(RED)Error: DOCKER_USERNAME not set$(NC)"; \
		echo "Usage: make push DOCKER_USERNAME=yourusername"; \
		exit 1; \
	fi
	docker tag $(IMAGE_NAME) $(DOCKER_USERNAME)/$(IMAGE_NAME):latest
	docker push $(DOCKER_USERNAME)/$(IMAGE_NAME):latest
	@echo "$(GREEN)✓ Image pushed to Docker Hub$(NC)"

pull: ## Pull image from Docker Hub (set DOCKER_USERNAME first)
	@if [ -z "$(DOCKER_USERNAME)" ]; then \
		echo "$(RED)Error: DOCKER_USERNAME not set$(NC)"; \
		exit 1; \
	fi
	docker pull $(DOCKER_USERNAME)/$(IMAGE_NAME):latest

backup: ## Backup data directories
	@echo "$(BLUE)Creating backup...$(NC)"
	tar -czf backup-$$(date +%Y%m%d-%H%M%S).tar.gz data/ chat_history/ faiss_cache/
	@echo "$(GREEN)✓ Backup created$(NC)"

restore: ## Restore from backup (set BACKUP_FILE)
	@if [ -z "$(BACKUP_FILE)" ]; then \
		echo "$(RED)Error: BACKUP_FILE not set$(NC)"; \
		echo "Usage: make restore BACKUP_FILE=backup-20231107-120000.tar.gz"; \
		exit 1; \
	fi
	tar -xzf $(BACKUP_FILE)
	@echo "$(GREEN)✓ Backup restored$(NC)"

install-docker: ## Install Docker (Ubuntu/Debian)
	@echo "$(BLUE)Installing Docker...$(NC)"
	curl -fsSL https://get.docker.com -o get-docker.sh
	sudo sh get-docker.sh
	sudo usermod -aG docker $$USER
	@echo "$(GREEN)✓ Docker installed. Please log out and back in.$(NC)"

check-env: ## Check if .env file exists
	@if [ ! -f .env ]; then \
		echo "$(RED)Error: .env file not found$(NC)"; \
		echo "Copy .env.example to .env and add your API key"; \
		exit 1; \
	fi
	@echo "$(GREEN)✓ .env file exists$(NC)"

init: check-env build run ## Initialize and run the application
	@echo "$(GREEN)✓ Application initialized successfully$(NC)"
	@echo "Access at: http://localhost:$(PORT)"
