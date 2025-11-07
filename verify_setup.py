#!/usr/bin/env python3
"""
Quick verification script to check if all dependencies are properly installed
"""

import sys

def check_imports():
    """Check if all required packages can be imported"""
    required_packages = [
        ('streamlit', 'Streamlit'),
        ('langchain', 'LangChain'),
        ('faiss', 'FAISS'),
        ('dotenv', 'python-dotenv'),
        ('google.generativeai', 'Google Generative AI'),
        ('sentence_transformers', 'Sentence Transformers'),
    ]
    
    print("🔍 Checking required packages...\n")
    all_good = True
    
    for package, name in required_packages:
        try:
            __import__(package)
            print(f"✅ {name}")
        except ImportError:
            print(f"❌ {name} - NOT INSTALLED")
            all_good = False
    
    return all_good

def check_env_file():
    """Check if .env file exists and has API key"""
    import os
    from dotenv import load_dotenv
    
    print("\n🔍 Checking environment configuration...\n")
    
    if not os.path.exists('.env'):
        print("❌ .env file not found")
        return False
    
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("❌ GEMINI_API_KEY not set in .env")
        return False
    
    print(f"✅ GEMINI_API_KEY found (length: {len(api_key)})")
    return True

def check_directories():
    """Check if required directories exist"""
    import os
    
    print("\n🔍 Checking directory structure...\n")
    
    dirs = ['data', 'chat_history', 'faiss_cache']
    for dir_name in dirs:
        if os.path.exists(dir_name):
            print(f"✅ {dir_name}/ exists")
        else:
            print(f"⚠️  {dir_name}/ will be created on first run")
    
    return True

if __name__ == "__main__":
    print("=" * 50)
    print("  Smart PDF Chatbot - Setup Verification")
    print("=" * 50 + "\n")
    
    checks = [
        check_imports(),
        check_env_file(),
        check_directories()
    ]
    
    print("\n" + "=" * 50)
    if all(checks):
        print("✅ All checks passed! You're ready to run the app.")
        print("\nRun: streamlit run app.py")
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        sys.exit(1)
    print("=" * 50)
