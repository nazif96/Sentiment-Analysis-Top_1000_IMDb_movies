import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Chargement des objets

model = load_model("sentiment_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)


# Fonction de prédiction

def predict_sentiment(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=200, padding='post', truncating='post')
    pred = model.predict(padded)
    label = label_encoder.inverse_transform([np.argmax(pred)])
    proba = np.max(pred)
    return label[0], proba


# Interface utilisateur

st.title("🎬 Analyse de sentiment IMDb")

user_input = st.text_area("Entrez une critique de film :")

if st.button("Prédire le sentiment"):
    if user_input.strip() == "":
        st.warning("Veuillez entrer une critique.")
    else:
        sentiment, confidence = predict_sentiment(user_input)
        st.success(f"Sentiment prédit : **{sentiment}** ({confidence:.2%} de confiance)")
