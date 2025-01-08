import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

# Download necessary NLTK packages
nltk.download('vader_lexicon')
nltk.download('punkt')

# Initialize Sentiment Intensity Analyzer
analyzer = SentimentIntensityAnalyzer()

# Ensure you have the NRC Emotion Lexicon file and update the path here
nrc_lexicon_path = r"C:\Users\Akshada\PycharmProjects\sentiment\venv\Lib\NRC-Emotion-Lexicon-Wordlevel-v0.92.txt"
nrc_lexicon = pd.read_csv(r"C:\Users\Akshada\PycharmProjects\sentiment\venv\Lib\nltk_data\vader_lexicon.txt", sep='\t', names=["word", "emotion", "association"], skiprows=45)

def get_emotion_score(text):
    words = word_tokenize(text.lower())
    emotion_scores = nrc_lexicon[nrc_lexicon['word'].isin(words)]['emotion'].value_counts()
    return emotion_scores.to_dict()

def analyze_sentiment(text):
    return analyzer.polarity_scores(text)['compound']

def predict_mood(sentiment_score, emotion_scores):
    mood_score = sentiment_score + sum(emotion_scores.values())
    return "Positive Mood" if mood_score >= 0 else "Negative Mood"

def main():
    while True:
        text = input("Enter text (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            break

        sentiment_score = analyze_sentiment(text)
        emotion_scores = get_emotion_score(text)
        mood_prediction = predict_mood(sentiment_score, emotion_scores)

        print(f"Sentiment Score: {sentiment_score}")
        print(f"Emotion Scores: {emotion_scores}")
        print(f"Mood Prediction: {mood_prediction}")

if _name_ == "_main_":
    main()