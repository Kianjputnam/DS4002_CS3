import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')  # Download sentence tokenizer

# Load datasets
scouting_reports = pd.read_csv("scouting_reports.csv")
nba_stats = pd.read_csv("merged_nba_stats2.csv")

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to preprocess text
def clean_text(text):
    if pd.isna(text):  # Handle missing values
        return ""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text)  # Remove excessive whitespace
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()

# Function to analyze sentiment of multiple sentences
def get_sentiment_scores(text):
    text = clean_text(text)  # Preprocess text
    sentences = sent_tokenize(text)  # Split into sentences
    scores = [analyzer.polarity_scores(sentence) for sentence in sentences]
    
    # Aggregate sentence-level scores into an overall report-level score
    if scores:
        compound = sum(score['compound'] for score in scores) / len(scores)
        positive = sum(score['pos'] for score in scores) / len(scores)
        negative = sum(score['neg'] for score in scores) / len(scores)
        neutral = sum(score['neu'] for score in scores) / len(scores)
    else:
        compound, positive, negative, neutral = 0, 0, 0, 0  # Handle empty text

    return compound, positive, negative, neutral

# Apply sentiment analysis to scouting reports
scouting_reports[['Compound Sentiment Score', 'Positive Sentiment Score', 
                  'Negative Sentiment Score', 'Neutral Sentiment Score']] = scouting_reports['Scouting Report'].apply(
    lambda x: pd.Series(get_sentiment_scores(x))
)

# Rename columns in NBA stats dataset for clarity
nba_stats.rename(columns={
    'Player': 'Player Name',
    'Min': 'Player Minutes Played',
    '+/-': 'Player Plus Minus',
    'PER': 'Player PER',
    'WS': 'Player WS',
    'VORP': 'Player VORP',
    'Awards': 'Player Awards'
}, inplace=True)

# Select relevant columns from NBA stats
nba_stats_filtered = nba_stats[['Player Name', 'Player Minutes Played', 'Player Plus Minus', 
                                'Player PER', 'Player WS', 'Player VORP', 'Player Awards']]

# Merge datasets on 'Player Name'
merged_data = pd.merge(scouting_reports, nba_stats_filtered, on='Player Name', how='inner')

# Save merged dataset
merged_data.to_csv("merged_nba_rookie_data_cleaned.csv", index=False)

# Display first few rows
print(merged_data.head())
