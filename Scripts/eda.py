import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
merged_data = pd.read_csv("merged_nba_rookie_data.csv")

# Plot 1: Histogram of Compound Sentiment Scores
plt.figure(figsize=(8, 5))
plt.hist(merged_data['Compound Sentiment Score'], bins=10, edgecolor='black', alpha=0.7)
plt.xlabel('Compound Sentiment Score')
plt.ylabel('Frequency')
plt.title('Distribution of Compound Sentiment Scores')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plot 2: Boxplots for Positive, Negative, and Neutral Sentiment Scores
plt.figure(figsize=(8, 5))
merged_data[['Positive Sentiment Score', 'Negative Sentiment Score', 'Neutral Sentiment Score']].boxplot()
plt.title('Boxplots of Sentiment Scores')
plt.ylabel('Sentiment Score')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
