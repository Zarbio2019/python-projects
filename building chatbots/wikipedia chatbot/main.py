# Author: Zarbio Romulo

import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import wikipedia

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')

# from a text:
text = 'Originally, vegetables were collected from the wild by hunter-gatherers.
Vegetables are all plants. Vegetables can be eaten either raw or cooked.'
question = 'What are plants?'
# answer: Vegetables are all plants.

# from wikipedia:
text = wikipedia.page('Vegetables').content # database of Wikipedia API about Vegetables
# the user can choose any topic in that

lemmatizer = WordNetLemmatizer()

# lemmatization: convert words into lemmas (find out the root of words)
def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas

def process(text, question):
  sentence_tokens = nltk.sent_tokenize(text)
  sentence_tokens.append(question)

  tv = TfidfVectorizer(tokenizer=lemma_me) # get the important of the words
  tf = tv.fit_transform(sentence_tokens)
  values = cosine_similarity(tf[-1], tf) # [-1]: for the question
  index = values.argsort()[0][-2]
  values_flat = values.flatten()
  values_flat.sort()
  coeff = values_flat[-2]
  if coeff > 0.3: # coefficient of similarity from question to the sentence
    return sentence_tokens[index] # return the answer


# Console
while True:
  question = input("Hi, what do you want to know?\n")
  output = process(text, question)
  if output: # = if output!=None
    print(output)
  elif question=='quit': # to exit I must to write "quit"
    break
  else:
    print("I don't know.")