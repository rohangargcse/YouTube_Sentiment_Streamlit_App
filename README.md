# 🎯 YouTube Comment Sentiment Analysis App

A **Streamlit-based web application** that performs **real-time sentiment analysis** on YouTube video comments using an **LSTM-based deep learning model** trained on the IMDB dataset.  
The app also supports **multi-language comment translation** for accurate sentiment prediction.


## 📌 Features
- 🔍 **Fetch YouTube comments** using YouTube Data API.
- 🧠 **Deep Learning Sentiment Model** (LSTM) trained on IMDB movie reviews dataset.
- 🌍 **Multi-language support** — auto-translates comments to English before analysis.
- 📊 **Interactive visualizations** — Pie chart & Bar chart showing sentiment distribution.
- 💾 **Download results** as CSV.
- ⚡ **Real-time predictions** on new videos.


## 🛠️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Machine Learning**: TensorFlow/Keras (LSTM)
- **API**: Google YouTube Data API v3
- **Translation**: [deep-translator](https://pypi.org/project/deep-translator/)
- **Visualization**: Matplotlib, Seaborn

1️⃣ Clone the Repository
git clone https://github.com/rohangargcse/YouTube_Sentiment_Streamlit_App.git
cd YouTube_Sentiment_Streamlit_App

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Your YouTube API Key
Open config.py and replace with your API key:
YOUTUBE_API_KEY = "YOUR_API_KEY_HERE"
Get API Key from: Google Cloud Console

4️⃣ Run the App
streamlit run app.py
The app will be available at:
http://localhost:8501

📊 Example Output
Sentiment Distribution (Pie Chart)
Sentiment Count (Bar Chart)

📂 Project Structure
📦 YouTube_Sentiment_Streamlit_App
 ┣ 📂 model            # Trained LSTM model files
 ┣ 📂 utils            # Data preprocessing & helper functions
 ┣ 📜 app.py           # Main Streamlit app
 ┣ 📜 config.py        # API key configuration
 ┣ 📜 requirements.txt # Dependencies
 ┗ 📜 README.md        # Project documentation
💡 How It Works

User enters a YouTube video URL or ID.

The app fetches comments via YouTube Data API.
Comments are cleaned & translated to English.
The trained LSTM model predicts sentiment.
Results are visualized and can be exported as CSV.

🔮 Future Improvements
Support for real-time comment streaming from live videos.
Model fine-tuning with YouTube-specific dataset.
Additional NLP features like sarcasm detection.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
