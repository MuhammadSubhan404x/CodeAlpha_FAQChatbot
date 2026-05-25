import streamlit as st
from chatbot import FAQChatbot

st.set_page_config(page_title="AI FAQ Chatbot", layout="wide")

if "bot" not in st.session_state:
    st.session_state.bot = FAQChatbot()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "suggestions_shown" not in st.session_state:
    st.session_state.suggestions_shown = False

bot = st.session_state.bot

with st.sidebar:
    st.title("FAQ Chatbot")
    st.caption("AI & Machine Learning Q&A")
    st.divider()
    st.markdown(f"**Questions in knowledge base:** {len(bot.questions)}")
    st.markdown(f"**Messages exchanged:** {len(st.session_state.messages)}")
    st.divider()

    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.suggestions_shown = False
        st.rerun()

    st.divider()
    st.markdown("**Try asking about:**")
    st.markdown("- What is machine learning?")
    st.markdown("- Explain neural networks")
    st.markdown("- What is overfitting?")
    st.markdown("- Difference between AI and ML")
    st.markdown("- What is a transformer?")

st.title("AI & Machine Learning FAQ Chatbot")
st.caption(
    "Ask questions about artificial intelligence, machine learning, deep learning, "
    "and related topics. Powered by TF-IDF cosine similarity with spaCy NLP preprocessing."
)

if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown(
            "Hello! I'm an AI-powered FAQ assistant. I can answer questions about "
            "artificial intelligence, machine learning, deep learning, and the CodeAlpha internship. "
            "What would you like to know?"
        )
    if not st.session_state.suggestions_shown:
        suggestions = bot.get_suggestions(4)
        st.markdown("**Suggested questions:**")
        cols = st.columns(2)
        for i, suggestion in enumerate(suggestions):
            with cols[i % 2]:
                if st.button(suggestion, key=f"sugg_{i}", use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": suggestion})
                    answer, score = bot.respond(suggestion)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "score": score
                    })
                    st.session_state.suggestions_shown = True
                    st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and "score" in msg and msg["score"] < 1.0:
            confidence = msg["score"]
            label = "High" if confidence > 0.4 else ("Medium" if confidence > 0.2 else "Low")
            color = "green" if confidence > 0.4 else ("orange" if confidence > 0.2 else "red")
            st.caption(f"Match confidence: :{color}[{label}] ({confidence:.0%})")

user_input = st.chat_input("Ask a question about AI or machine learning...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    answer, score = bot.respond(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "score": score
    })
    st.rerun()
