import random
import json
import nltk
import numpy as np

from nltk.stem import WordNetLemmatizer

# Download NLTK data (run only once)
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json", "r") as file:
    intents = json.load(file)

words = []
classes = []
documents = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        tokens = pattern.split()

        words.extend(tokens)
        documents.append((tokens, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = sorted(set([lemmatizer.lemmatize(w.lower()) for w in words if w.isalpha()]))
classes = sorted(set(classes))

# Create a bag-of-words
def bag_of_words(sentence):
    sentence_words = sentence.split()
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    bag = [0] * len(words)
    for sw in sentence_words:
        for i, w in enumerate(words):
            if w == sw:
                bag[i] = 1
    return np.array(bag)

# Predict intent
def predict_class(sentence):
    bow = bag_of_words(sentence)
    scores = []
    for idx, doc in enumerate(documents):
        tag = doc[1]
        pattern_words = [lemmatizer.lemmatize(w.lower()) for w in doc[0]]
        match = len(set(bow).intersection(set(bag_of_words(" ".join(pattern_words)))))
        scores.append((tag, match))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[0][0] if scores[0][1] > 0 else "no_match"

# Response generator
def get_response(intent_tag):
    for intent in intents['intents']:
        if intent['tag'] == intent_tag:
            return random.choice(intent['responses'])
    return "Sorry, I don't understand that."

# Chat loop
print("🤖 Chatbot is online! Type 'quit' to exit.")
while True:
    msg = input("You: ")
    if msg.lower() == "quit":
        print("Bot: Goodbye! 👋")
        break
    intent = predict_class(msg)
    response = get_response(intent)
    print("Bot:", response)
