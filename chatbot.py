import re
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

from faqs import FAQ_DATA

try:
    _nlp = spacy.load("en_core_web_sm")
    _SPACY_OK = True
except Exception:
    _nlp = None
    _SPACY_OK = False

GREETINGS = ["hi", "hello", "hey", "howdy", "sup", "good morning", "good afternoon", "good evening"]
FAREWELLS = ["bye", "goodbye", "see you", "exit", "quit", "thanks bye", "thank you bye"]

GREETING_RESPONSES = [
    "Hello! Ask me anything about AI, machine learning, or the CodeAlpha internship.",
    "Hi there! I can answer questions about artificial intelligence, ML concepts, and more.",
    "Hey! What would you like to know about AI or machine learning today?",
]

FAREWELL_RESPONSES = [
    "Goodbye! Hope I was helpful.",
    "See you later! Good luck with your AI journey.",
    "Bye! Feel free to come back with more questions.",
]

UNKNOWN_RESPONSES = [
    "I don't have a good answer for that. Try rephrasing or ask about AI, machine learning, or deep learning.",
    "That one's outside my knowledge base. Ask me about ML concepts, neural networks, or the internship.",
    "Not sure about that. I work best with questions about artificial intelligence and related topics.",
]


def preprocess(text):
    text = text.lower().strip()
    text = text.translate(str.maketrans("", "", string.punctuation))
    if _SPACY_OK:
        doc = _nlp(text)
        tokens = [t.lemma_ for t in doc if not t.is_stop and not t.is_punct and t.lemma_.strip()]
        return " ".join(tokens) if tokens else text
    return text


class FAQChatbot:
    def __init__(self):
        self.questions = [item["question"] for item in FAQ_DATA]
        self.answers = [item["answer"] for item in FAQ_DATA]
        self.processed_questions = [preprocess(q) for q in self.questions]

        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        self.tfidf_matrix = self.vectorizer.fit_transform(self.processed_questions)

    def respond(self, user_input):
        raw = user_input.strip()
        if not raw:
            return "", 0.0

        lowered = raw.lower()

        if any(re.search(r"\b" + re.escape(g) + r"\b", lowered) for g in GREETINGS):
            return random.choice(GREETING_RESPONSES), 1.0

        if any(re.search(r"\b" + re.escape(f) + r"\b", lowered) for f in FAREWELLS):
            return random.choice(FAREWELL_RESPONSES), 1.0

        processed = preprocess(raw)

        try:
            query_vec = self.vectorizer.transform([processed])
            scores = cosine_similarity(query_vec, self.tfidf_matrix)[0]
            best_idx = scores.argmax()
            best_score = scores[best_idx]
        except Exception:
            return random.choice(UNKNOWN_RESPONSES), 0.0

        if best_score < 0.12:
            return random.choice(UNKNOWN_RESPONSES), float(best_score)

        return self.answers[best_idx], float(best_score)

    def get_suggestions(self, n=5):
        indices = random.sample(range(len(self.questions)), min(n, len(self.questions)))
        return [self.questions[i] for i in indices]
