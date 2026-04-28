import streamlit as st
from keras.models import load_model
import pickle
from keras.preprocessing.sequence import pad_sequences
import numpy as np  


## Loading the Tensorflow Model for Prediction

model = load_model('models/sentiment_analysis_model.keras')

with open('models/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

st.title("Twitter Tweets Sentiment Analysis")

tweet = st.text_input("Enter a tweet to analyze its sentiment:")

if st.button("Predict Sentiment") and tweet.strip():
    sequences = tokenizer.texts_to_sequences([tweet])
    padded_sequences = pad_sequences(sequences,padding='post', maxlen=99)
    prdiction = model.predict(padded_sequences)
    predicted_class = np.argmax(prdiction,axis=1)[0]

    sentiment_map = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}


    st.write(f"Sentiment: {sentiment_map[predicted_class]}")
