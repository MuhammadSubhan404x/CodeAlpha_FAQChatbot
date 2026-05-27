# FAQ Chatbot

A Streamlit chatbot that answers questions about artificial intelligence and machine learning
using TF-IDF cosine similarity with spaCy NLP preprocessing.

## Features

- 50 Q&A pairs covering AI, ML, deep learning, NLP, and more
- TF-IDF vectorization with bigram support for accurate matching
- spaCy lemmatization and stop-word removal for cleaner text matching
- Confidence score shown per response (High / Medium / Low)
- Suggested questions on startup
- Sidebar with knowledge base stats and conversation counter
- Graceful fallback for out-of-scope questions

## How to run

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

## How it works

User input is preprocessed using spaCy (lemmatization, stop-word removal), then vectorized
with TF-IDF alongside all FAQ questions. Cosine similarity finds the closest matching question.
If the best match score is below the confidence threshold, the bot returns a graceful fallback
instead of a wrong answer.

## Project structure

```
CodeAlpha_FAQChatbot/
|-- app.py          - Streamlit chat interface
|-- chatbot.py      - FAQChatbot class with TF-IDF matching logic
|-- faqs.py         - 50 Q&A pairs knowledge base
|-- requirements.txt
```

## Dependencies

`streamlit` | `scikit-learn` | `spacy`
