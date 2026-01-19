💬 Sentiment Analyzer

A Machine Learning–based Sentiment Analysis web app that predicts whether a given text expresses positive or negative sentiment, built using Python, NLP, and Streamlit.

🚀 Features

Analyze sentiment of user-entered text in real time

TF-IDF + Logistic Regression based NLP model

Interactive and minimal Streamlit UI

Fast and lightweight inference

🧠 Tech Stack

Language: Python

Machine Learning: Scikit-learn

NLP: TF-IDF Vectorization

Web App: Streamlit

Data Handling: Pandas, NumPy

📂 Project Structure
sentiment-streamlit-app/
├── app.py                 # Streamlit application
├── train.py               # Model training script
├── requirements.txt       # Dependencies
├── model/
│   ├── sentiment_model.pkl
│   └── tfidf.pkl
└── README.md

⚙️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/apurva1334/sentiment-streamlit-app.git
cd sentiment-streamlit-app

2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Train the model (if .pkl files not present)
python train.py

5️⃣ Run the Streamlit app
streamlit run app.py


App will open at:

http://localhost:8501

☁️ Deployment

This project is deployed using Streamlit Community Cloud.

Steps:

Push code to GitHub

Go to https://share.streamlit.io

Select repository & app.py

Click Deploy

📝 Example

Input:

I love this product!

Output:
😊 Positive Sentiment