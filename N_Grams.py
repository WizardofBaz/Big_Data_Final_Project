from nltk import ngrams, word_tokenize
from collections import Counter
import pandas as pd

df = pd.read_csv('What_Made_You_Happy.csv')


# Tokenize the text data in the column
df['tokenized_text'] = df['cleaned_hm'].apply(word_tokenize)

def generate_ngrams(tokens, n):
    return list(ngrams(tokens, n))

#value of 'n' for n-grams
n = 2 

df['ngrams'] = df['tokenized_text'].apply(lambda x: generate_ngrams(x, n))

df['ngrams_frequency'] = df['ngrams'].apply(lambda x: Counter(x))

df.to_csv("Happy_N-Grams.csv",index=False)

columns_to_keep = ['tokenized_text', 'ngrams', 'ngrams_frequency']  # Replace with the column names you want to keep

# Save selected columns to a new CSV file
df[columns_to_keep].to_csv('Happy_N-Grams.csv', index=False)