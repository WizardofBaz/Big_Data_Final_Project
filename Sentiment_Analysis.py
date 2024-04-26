#Sentiment Analysis of cleaned_hm then see how many polarity 1 we actually got.

"""
TextBlob returns polarity and subjectivity of a sentence. Polarity lies between [-1,1],
 -1 defines a negative sentiment and 1 defines a positive sentiment.
"""

"""
Subjectivity lies between [0,1]. Subjectivity quantifies the amount of personal opinion and factual information 
contained in the text. 
The higher subjectivity means that the text contains personal opinion rather than factual information.
"""

import pandas as pd

df = pd.read_csv('What_Made_You_Happy.csv')

from textblob import TextBlob
""" nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
 """
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
  #print(text)
  return text

df['cleaned_hm'].apply(lambda x: get_sentiment(' '.join(x)))

for column in df:
    columnSeriesObj = df["cleaned_hm"]

polarity_1_count = 0
for text in df['cleaned_hm']: 
    blob = TextBlob(str(text))  # Ensure text is converted to string
    # Check polarity
    if blob.sentiment.polarity == 1:
        polarity_1_count += 1
    
with open('sentiment_analysis_results.txt', 'w') as file:
    for abstract in df["cleaned_hm"].values:
        blob = TextBlob(str(abstract))  #Convert to string
        sentiment = blob.sentiment
        file.write(f'Sentiment: {sentiment}\n')

# Open the file in append mode
with open('sentiment_analysis_results.txt', 'a') as f:
    f.write("Number of polarity 1 sentiments: " + str(polarity_1_count) + "\n")