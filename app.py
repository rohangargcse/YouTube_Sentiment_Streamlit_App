
import streamlit as st
import pandas as pd
from utils.youtube_api import fetch_comments
from utils.preprocess import clean_and_translate_comments
from utils.predict import load_model_and_tokenizer, predict_sentiments
from matplotlib import pyplot as plt
import seaborn as sns

st.set_page_config(page_title="YouTube Sentiment Analyzer", layout="wide")
st.title("🎥 YouTube Comment Sentiment Analysis")
st.markdown("Analyze comments from any YouTube video using an LSTM model. Multilingual supported 🌍")

video_id = st.text_input("🔗 Enter YouTube Video ID or Full URL:", "")

if st.button("Analyze") and video_id:
    with st.spinner("Fetching and analyzing comments..."):
        comments = fetch_comments(video_id)
        if not comments:
            st.warning("No comments fetched.")
        else:
            cleaned, translations = clean_and_translate_comments(comments)
            model, tokenizer = load_model_and_tokenizer()
            results_df = predict_sentiments(cleaned, translations, comments, model, tokenizer)

            st.success("Analysis Complete ✅")
            st.dataframe(results_df.head(10))

            # Visuals
            fig1, ax1 = plt.subplots()
            results_df['Sentiment'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightgreen','lightcoral'], ax=ax1)
            ax1.set_ylabel('')
            ax1.set_title('Sentiment Distribution')
            st.pyplot(fig1)

            fig2, ax2 = plt.subplots()
            sns.countplot(data=results_df, x='Sentiment', palette='coolwarm', ax=ax2)
            ax2.set_title('Sentiment Count')
            st.pyplot(fig2)

            # Download
            csv = results_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv, "sentiment_results.csv", "text/csv")
