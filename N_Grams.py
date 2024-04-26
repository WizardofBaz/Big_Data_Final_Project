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

""" from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Generate word cloud from n-gram frequencies
ngrams_dict = dict(sum((Counter(item) for item in df['ngrams_frequency']), Counter()))

sorted_ngrams = sorted(ngrams_dict.items(), key=lambda x: x[1], reverse=True)

# Select the top 20 words
top_20_ngrams = dict(sorted_ngrams[:20])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_20_ngrams)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig('ngram_wordcloud.png')
plt.show() """
