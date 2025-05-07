# DS4002_CS3

## NBA Rookie Sentiment Analysis 

## Goals and Theories

Motivation and Context: 
Statistics like PER, Win Shares, and Plus-Minus are widely used to measure a player’s performance on the court, but scouting reports offer qualitative evaluations that capture traits/intangibles/potential like basketball IQ, work ethic, clutch, coachability,  and instincts—attributes that don’t always show up in box scores. Despite their importance in draft decisions, little research has tested whether the sentiment in pre-draft scouting reports can actually predict rookie performance in the NBA.

Hypothesis
Pre-draft scouting report sentiment correlates with rookie performance.

Research Question: 
Do the sentiment scores of the 2023 NBA rookie pre-draft scouting reports correlate with the players’ performance metrics in their rookie season?

## Software and Platform

We are using Jupter Notebooks for this program that run on Python 3 (prefferably 3.10+). Our code can also be run on **Google Colab** by importing our notebooks.

Files will need a Python base on a **Windows** environment with the following packages: `Pandas`, `Numpy`, `Seaborn`, `Matplotlib`,`statsmodels`, `nltk`, `wordcloud`, `scipy`. These files can alternatively be run on **Google Colab** or **Rivanna**. 

## Reproducing Results

- Our NBA stats data came from NBA.com and NBAReference.com. They are found in Reference_stats1.xls and Reference_stats2.xls which were merged using Compiling_stats_code.ipynb to form merged_nba_stats2.csv (if reference stats are not working properly due to excel reading error, you can just refer to merged_nba_stats2.csv). You may have to update the data path to where you have stored the data, or you may clone the github repository and include this code.

- scraper.py was used to get the scouting reports online and were turned into scouting_reports.csv, which was then compiled into merged_nba_rookie_data.csv

- textblob_analysis.ipynb was performed and compiled to rookie_data_textblob.csv

- Sentiment_Analysis_Correlations.ipynb was performed on rookie_data_textblob.csv and displays our findings. This also contains most of the figures shown in our presentation

## References

 [1] "2023 NBA Draft – Actual Draft Results," NBADraft.net, 2023. [Online]. Available: https://www.nbadraft.net/actual-draft/?year-mock=2023. [Accessed: Feb. 5, 2025].
 
 [2] "2023 NBA Draft – ESPN Insider," ESPN, 2023. [Online]. Available: https://insider.espn.com/nba/draft/rounds/_/season/2023. [Accessed: Feb. 5, 2025].
 
 [3] “NBA Draft Prospect Profiles: Scouting Report Archives,” NBA Draft on SI, 2024 [Online]. Available:
 https://www.si.com/nba/draft/newsfeed/nba-draft-prospect-profiles-scouting-report-archives#_wmi8586qa (Accessed Feb.17, 2025).
 
 [4] "2024 NBA Rookies | Basketball-Reference.com," Basketball-Reference, 2024. [Online]. Available: 
https://www.basketball-reference.com/leagues/NBA_2024_rookies.html. [Accessed: Feb. 5, 2025].

 [5] "NBA Player Stats – Traditional," NBA.com, 2024. [Online]. Available: https://www.nba.com/stats/players/traditional?DraftYear=2023&Season=2023-24&dir=A&sort=GP. 
[Accessed: Feb. 5, 2025].

 [6] "The Numbers Don't Lie," Samford University, 2023. [Online]. Available: https://www.samford.edu/sports-analytics/fans/2023/The-Numbers-Dont-Lie. [Accessed: Feb. 5, 
2025].

 [7] "nltk.sentiment.vader Module Documentation," NLTK, 2024. [Online]. Available: https://www.nltk.org/api/nltk.sentiment.vader.html. [Accessed: Feb. 7, 2025].
 
 [8] A. S. M. Sultan, M. A. Rahman, and M. S. Hossain, "TextBlob and BiLSTM for Sentiment Analysis Toward COVID-19 Tweets," 2022 International Conference on Innovations 
in Science, Engineering and Technology (ICISET), Sylhet, Bangladesh, 2022, pp. 1-6. [Online]. Available: https://ieeexplore.ieee.org/document/9736380/. [Accessed: Feb. 10, 
2025].

 [9] C. Lawlor, J. Rookwood, and C. Wright, "Player scouting and recruitment in English men’s professional football: opportunities for research," J. Qual. Res. Sports Stud., vol. 
15, no. 1, pp. 57–76, 2021. [Online]. Available: https://www.academia.edu/60947249/. [Accessed: Jan. 30, 2025].

 [10] C. J. Hutto and E. Gilbert, “VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text,” in *Proc. 8th Int. Conf. Weblogs Social Media 
(ICWSM-14)*, 2014. [Online]. Available: 
https://www.researchgate.net/publication/275828927_VADER_A_Parsimonious_Rule-based_Model_for_Sentiment_Analysis_of_Social_Media_Text. [Accessed: Jan. 29, 
2025].

 [11] R. P. Schumaker, A. T. Jarmoszko, and C. S. Labedz Jr., “Predicting wins and spread in the Premier League using a sentiment analysis of Twitter,” *Decision Support Syst.*, 
vol. 88, pp. 76–84, 2016. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S0167923616300835. [Accessed: Jan. 29, 2025].

