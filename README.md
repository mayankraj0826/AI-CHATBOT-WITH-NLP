# AI-CHATBOT-WITH-NLP

# 🤖 AI Chatbot with NLP (Rule-Based)

This is a simple rule-based AI chatbot developed using **Python** and **Natural Language Processing (NLP)** techniques. It uses **`intents.json`** to match user input with predefined patterns and returns a suitable response. No training, no internet — just clean logic and smart replies using `NLTK` (or simplified split for Python 3.13).

---

## 📌 Features

- Works offline  
- Easy to customize (`intents.json`)  
- Built with core NLP concepts: tokenizing, lemmatizing, bag-of-words  
- No ML model or API key required  
- Perfect for beginners and college submissions

---

## 🛠 Tools & Technologies

- **Python 3.13** (or compatible)  
- **NLTK** (used partially)  
- **NumPy**  
- `intents.json` file for pattern matching  
- (Optional) GUI with Tkinter can be added

---

## 📁 File Structure

```

project-folder/
│
├── chatbot.py         # Main Python chatbot script
├── intents.json       # All patterns and replies
└── README.md          # Project description

```

---

## 📚 How It Works

1. The chatbot reads `intents.json`, which contains:
   - Tags (intents like greeting, goodbye, thanks)
   - Patterns (what user might say)
   - Responses (what the bot should reply)

2. Input is processed using:
   - Tokenization (`.split()` for Python 3.13)
   - Lemmatization (`WordNetLemmatizer`)
   - Bag of Words to compare input with patterns

3. It finds the **most relevant tag** and returns a **random response** from that tag.

---

## 🧪 Sample Chat

```

🤖 Chatbot is online! Type 'quit' to exit.

You: Hello
Bot: Hi there!

You: What's your name?
Bot: I am a chatbot created using Python!

You: Bye
Bot: See you!

````

---

## 🚀 How to Run

### Step 1: Install Dependencies

```bash
pip install nltk numpy
````

> If you're using Python 3.13, no need to download `punkt` — code uses `.split()` instead of `word_tokenize`.

### Step 2: Run the Script

```bash
python chatbot.py
```

---

## 🛠 Customization

* Add more intents in `intents.json`
* Modify responses or add your own personality to the bot
* Optional: Add Tkinter GUI or voice support for advanced UI

---

## 📌 Project Title Suggestions

* AI Chatbot with NLP
* Python Rule-Based Chatbot
* Offline NLP Chatbot using Intents
* Smart Assistant Using JSON + NLP

---

## ✅ Ideal For

* College mini-projects
* AI/NLP assignment demos
* Learning how chatbots work
* Offline chatbot setup without APIs

---

## 👨‍💻 Author

**Developed by:** Mayank
*Second Year Student, B.Tech (CSE)*


