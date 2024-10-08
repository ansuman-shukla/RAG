

# 🦾 Chroma & Ollama Setup Guide 🦄

Welcome to **The AI RAG Adventure**! 🎉 This project combines document search 🔍, vector embedding magic 🧙‍♂️, and the power of Ollama 🚀 to answer your queries based on your own data. Ready to dive in? Let's go! 🎢

---

## 🔧 Setup Instructions

### Step 1: Clone this repo 🛠️
```bash
git clone https://github.com/ansuman-shukla/RAG.git
cd RAG
```

### Step 2: Install dependencies 📦

Make sure you’ve got Python 🐍 installed (3.8+). Then:

```bash
pip install -r requirements.txt
```

### Step 3: Start the Ollama 🦙 engine
Ollama is a beast. To tame it, you need to:
1. Install the Ollama CLI:
   ```bash
   brew install ollama
   ```

2. Fire up the server:
   ```bash
   ollama serve
   ```

Now Ollama’s ready to help with all your deep 🧠 AI queries.

---

## 📚 Adding Your Books (PDFs)

To feed your AI with knowledge, place all your **PDF files** in the `data/` directory inside the project folder. That's where the magic happens! 🧙‍♀️

```
RAG/
│
├── data/
│   └── your-book.pdf
│   └── another-book.pdf
│
├── chroma/
├── main.py
└── ...
```

---

## 🚀 Running the Application

To start the adventure, run the main program:

```bash
python main.py --query "How do I become an AI wizard?"
```

This will load your documents, split them into chunks 🔪, and run a similarity search 🧐 using Chroma's vector store. The best matches will be fed into Ollama to generate responses that are sharp as a ⚔️!

If you want to **clear the database** 🗑️ (and start fresh), simply add the `--reset` flag:

```bash
python main.py --reset
```

---

## 📂 File Structure
- **main.py**: This is the brain 🧠 of the operation. It handles document loading, chunking, embedding, and searching.
- **data/**: Put your PDF books here 📚.
- **chroma/**: Chroma's magic database lives here 💾. Don’t worry, it's persistent across runs!
- **requirements.txt**: All the tasty dependencies 🍜 you'll need.

---

### Bonus: What does this do? 🎲

In a nutshell, this project does **RAG** (Retrieval-Augmented Generation). We:
1. **Load** PDFs 📚,
2. **Split** 'em into digestible chunks 🍰,
3. **Embed** those chunks in a vector space 🌌,
4. **Search** for relevant chunks when you ask a question 🔍,
5. **Generate** a response with Ollama that’s smart as heck 🤓.

Enjoy your quest to AI greatness! ✨

---

### Troubleshooting 🔧
- 🐢 If things are slow, check your server load or internet speed.
- ❓ If Ollama’s not behaving, try restarting it with `ollama serve`.
- 📞 Need help? Drop a message to the tech wizards on the internet.
