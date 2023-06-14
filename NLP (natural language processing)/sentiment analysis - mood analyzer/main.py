# Sentiment Analysis is finding the mood of a piece of text, so if it is positive or negative?
# example: analyze a tweet or a Facebook post.

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# vader_lexicon: get the mood of the words, mean Valance a word dictionary and Sentiment of Reason
nltk.download('vader_lexicon')
nltk.download('twitter_samples')

analyzer = SentimentIntensityAnalyzer() # class for analysis

text1 = 'Hey, what a beautiful day! How amazing it is!'
analyzer.polarity_scores(text1)
{'neg': 0.0, 'neu': 0.42, 'pos': 0.58, 'compound': 0.8513}

if analyzer.polarity_scores(text1)['compound'] > 0: # get positive coefficients
    print('Positive Text')
else:
    print('Negative Text')
# return
'''
Positive Text
'''

len(nltk.corpus.twitter_samples.strings()) # get list of tweets
# return: 30000

tweet1 = nltk.corpus.twitter_samples.strings()[1045] # get a specific tweet in 1045
tweet1
# return: 'My phone is so shit, it always runs out of memory :( ...2 many nudes'

analyzer.polarity_scores(tweet1)
# return: {'neg': 0.366, 'neu': 0.634, 'pos': 0.0, 'compound': -0.8184}
