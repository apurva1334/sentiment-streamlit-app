import streamlit as st
import pickle
import os

st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬")

@st.cache_resource
def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    model_path = os.path.join(BASE_DIR, "model", "sentiment_model.pkl")
    vectorizer_path = os.path.join(BASE_DIR, "model", "tfidf.pkl")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer

model, vectorizer = load_model()

st.title("💬 Sentiment Analyzer")
st.write("Analyze sentiment of text using Machine Learning")

text = st.text_area("Enter text here")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        vec = vectorizer.transform([text])
        prediction = model.predict(vec)[0]

        if len(text.split()) < 3:
            st.warning("Please enter a longer sentence for accurate prediction.")
            st.stop()

        if prediction.lower() == "positive":
            st.success("😊 Positive Sentiment")
        else:
            st.error("😠 Negative Sentiment")
