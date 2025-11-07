# 🚀 GitHub Setup Guide

Your project is ready to be pushed to GitHub! Follow these steps:

## Step 1: Create a New Repository on GitHub

1. Go to [GitHub](https://github.com) and log in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `smart-pdf-chatbot` (or your preferred name)
   - **Description**: "AI-Powered PDF Chatbot using RAG Technology and Gemini AI"
   - **Visibility**: Choose Public or Private
   - ⚠️ **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

## Step 2: Configure Git (First Time Only)

If you haven't set up git before, configure your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Then amend the commit with the correct author:

```bash
git commit --amend --reset-author --no-edit
```

## Step 3: Connect to GitHub

Replace `yourusername` with your actual GitHub username:

```bash
git remote add origin https://github.com/yourusername/smart-pdf-chatbot.git
```

## Step 4: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

If prompted, enter your GitHub credentials or use a Personal Access Token.

## Step 5: Update README Links

After creating the repository, update these links in README.md:

1. Replace `yourusername` with your GitHub username in:
   - Clone URL
   - Bug report link
   - Feature request link

2. Update the author section with your actual:
   - LinkedIn URL
   - Email address

Then commit and push the changes:

```bash
git add README.md
git commit -m "docs: update README with correct GitHub links"
git push
```

## Step 6: Add Repository Topics (Optional)

On your GitHub repository page:

1. Click the ⚙️ gear icon next to "About"
2. Add topics: `ai`, `chatbot`, `rag`, `pdf`, `streamlit`, `gemini`, `langchain`, `faiss`, `python`
3. Save changes

## Step 7: Enable GitHub Pages (Optional)

If you want to showcase screenshots:

1. Go to repository **Settings** → **Pages**
2. Select source: **Deploy from a branch**
3. Choose **main** branch and **/ (root)** folder
4. Save

## 🎉 You're Done!

Your project is now on GitHub! Share the link:

```
https://github.com/yourusername/smart-pdf-chatbot
```

## 📝 Future Updates

When you make changes to your project:

```bash
git add .
git commit -m "description of changes"
git push
```

## 🔐 Important Security Notes

✅ **Already Protected:**
- `.env` file is in `.gitignore` (API keys are safe)
- `data/`, `chat_history/`, and `faiss_cache/` are ignored
- Virtual environment is ignored

⚠️ **Never commit:**
- API keys or secrets
- Personal data
- Large binary files

## 🆘 Troubleshooting

### Authentication Failed

If you get authentication errors, you need a Personal Access Token:

1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo` (full control)
4. Copy the token
5. Use it as your password when pushing

### Remote Already Exists

If you get "remote origin already exists":

```bash
git remote remove origin
git remote add origin https://github.com/yourusername/smart-pdf-chatbot.git
```

### Push Rejected

If push is rejected:

```bash
git pull origin main --rebase
git push -u origin main
```

---

**Need help?** Check [GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
