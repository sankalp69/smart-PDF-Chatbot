# ⚡ Quick Command Reference

## 🚀 Push to GitHub (Copy & Paste)

### First Time Setup

```bash
# 1. Configure git (replace with your info)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 2. Amend the commit with correct author
git commit --amend --reset-author --no-edit

# 3. Add remote (replace 'yourusername' with your GitHub username)
git remote add origin https://github.com/yourusername/smart-pdf-chatbot.git

# 4. Push to GitHub
git branch -M main
git push -u origin main
```

### After Creating GitHub Repository

Just run these three commands (replace `yourusername`):

```bash
git remote add origin https://github.com/yourusername/smart-pdf-chatbot.git
git branch -M main
git push -u origin main
```

---

## 🔄 Future Updates

When you make changes:

```bash
git add .
git commit -m "your commit message"
git push
```

---

## 🏃 Run the App

```bash
# Activate virtual environment
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

# Run the app
streamlit run app.py
```

---

## ✅ Verify Setup

```bash
python3 verify_setup.py
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔍 Check Git Status

```bash
git status
git log --oneline
```

---

## 🌿 Create New Branch

```bash
git checkout -b feature/new-feature
git push -u origin feature/new-feature
```

---

## 📊 View Repository Info

```bash
git remote -v
git branch -a
```

---

## 🔙 Undo Last Commit (Keep Changes)

```bash
git reset --soft HEAD~1
```

---

## 🗑️ Discard Local Changes

```bash
git checkout -- .
```

---

## 📥 Pull Latest Changes

```bash
git pull origin main
```

---

## 🏷️ Create a Release Tag

```bash
git tag -a v1.0.0 -m "First release"
git push origin v1.0.0
```

---

## 🔐 Update .env (Never Commit!)

```bash
echo "GEMINI_API_KEY=your_key_here" > .env
```

---

## 🧹 Clean Up

```bash
# Remove cached files
rm -rf faiss_cache/
rm -rf chat_history/

# Remove virtual environment
rm -rf venv/
```

---

## 📝 Quick Commit Messages

- `feat: add new feature`
- `fix: bug fix`
- `docs: update documentation`
- `style: formatting changes`
- `refactor: code restructuring`
- `test: add tests`
- `chore: maintenance tasks`

---

**Pro Tip**: Bookmark this file for quick reference! 🔖
