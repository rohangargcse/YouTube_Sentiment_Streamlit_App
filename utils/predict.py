
import pickle
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

def load_model_and_tokenizer():
    model = load_model("model/sentiment_model.h5")
    with open("model/tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

def predict_sentiments(cleaned, translations, raw_comments, model, tokenizer, maxlen=150):
    sequences = tokenizer.texts_to_sequences(cleaned)
    padded = pad_sequences(sequences, maxlen=maxlen, padding='post')
    probs = model.predict(padded).flatten()
    labels = ['Positive' if p > 0.5 else 'Negative' for p in probs]
    return pd.DataFrame({
        "Original Comment": raw_comments,
        "Translated": translations,
        "Confidence": np.round(probs, 2),
        "Sentiment": labels
    })
