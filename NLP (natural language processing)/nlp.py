x = 'was' # root of this word = be
y = 'is' # root of this word = be
x == y # False

# NLP allow to define that these 2 words derive form verb "to be"

# Lemmatization of words
# allow to fin the root of the words

import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

lemma1 = lemmatizer.lemmatize(x, 'v') # v = verb, return "be"
lemma2 = lemmatizer.lemmatize(y, 'v') # v = verb, return "be"
x == y # True

lemma1 = lemmatizer.lemmatize('vegetables', 'n') # n = noun
lemma2 = lemmatizer.lemmatize('vegetable', 'v') # v = verb

lemma1 # return 'vegetable'

#################################################

# Lemmatization of Sentences
Lemmatization is find the root word of a word

import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

sentence = 'Vegetables are types of plants.'

- Tokenizing sentences
Tokenization: Convert sentence to word

nltk.download('punkt') # for Tokenizing

sentence_tokens = nltk.word_tokenize(sentence.lower())
sentence_tokens # ['vegetables', 'are', 'types', 'of', 'plants', '.']

for token in sentence_tokens:
  lemma = lematizer.lemmatize(token, 'v')
  print(lemma)
# return
'''
vegetables
be
type
of
plant
.
'''

pos_tags = nlk.pos_tag(sentence_tokens)
pos_tags
# return
'''
[('vegetables', 'NNS'), # N = noun
 ('are', 'VBP'), # V = verb
 ('types', 'NNS'),
 ('of', 'IN'), # I = preposition
 ('plants', 'NNS'),
 ('.', '.')]
'''

# sample 1
for token, pos_tag in zip(sentence_tokens, pos_tags):
  if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']: # n = noun, v = verb
        lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower()) # for NNS [1][0] 
        print(lemma)
# return
'''
vegetable
be
type
plant
'''

# sample 2: compare sentences using Natural Language Processing
import nltk 
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma) # show: ['vegetable', 'be', 'type', 'plant']

    return sentence_lemmas
    
l1 = lemma_me('Vegetables are types of plants.')
l1 # ['vegetable', 'be', 'type', 'plant']

l2 = lemma_me('A vegetable is a type of plant')
l2 # ['vegetable', 'be', 'type', 'plant']

l1 == l2 # True

#################################################

# Find the most similar sentence: Chatbot

From a text and a question, give me the answer.
Ex: Chatbot of Wikipedia

text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked.'
question = 'What are vegetables?' 

import nltk 
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas

# get the sentence tokens
sentence_tokens = nltk.sent_tokenize(text)
sentence_tokens.append(question)
sentence_tokens
# return
'''
['Originally, vegetables were collected from the wild by hunter-gatherers.',
 'Vegetables are all plants.',
 'Vegetables can be eaten either raw or cooked.',
 'What are vegetables?']
'''

# importance of words and tokenize sentence to work
from sklearn.feature_extraction.text import TfidfVectorizer # class for statistical analysis to find out the importance of words of a text

tv = TfidfVectorizer(tokenizer=lemma_me) # tokenize sentence to work
tv
# return
'''
TfidfVectorizer(tokenizer=<function lemma_me at 0x7f31a2caf9e0>)
'''

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

True

tf = tv.fit_transform(sentence_tokens)
tf
# return
'''
<4x8 sparse matrix of type '<class 'numpy.float64'>'
	with 14 stored elements in Compressed Sparse Row format>
'''

tf.toarray()
# return matrix of list of importance or weight of each word, one list for each sentence
# word "the" is uncounted
'''
array([[0.27717414, 0.53114624, 0.        , 0.        , 0.53114624,
        0.53114624, 0.        , 0.27717414],
       [0.41988018, 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.8046125 , 0.41988018],
       [0.32713399, 0.        , 0.62688384, 0.62688384, 0.        ,
        0.        , 0.        , 0.32713399],
       [0.70710678, 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.70710678]])
'''
# sentences
'''
['Originally, vegetables were collected from the wild by hunter-gatherers.',
 'Vegetables are all plants.',
 'Vegetables can be eaten either raw or cooked.',
 'What are vegetables?']
'''

# to get a better representation in form of table of the matrix
import pandas
df = pandas.DataFrame(tf.toarray(), columns=tv.get_feature_names())
df # df = dataframe
# return a table

# compare the question with the entire matrix (tf)
from sklearn.metrics.pairwise import cosine_similarity
values = cosine_similarity(tf[-1], tf) # [-1] = the least is the question
values
# return
'''
array([[0.39198343, 0.59380024, 0.46263733, 1.        ]])
'''
# that means how similar is our question with the first sentence.

text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked.'
question = 'What are vegetables?' 

index = values.argsort()[0][-2] # get the index of the maximun value
index
# 1

values_flat = values.flatten()
values_flat
# array([0.39198343, 0.59380024, 0.46263733, 1.        ])

values_flat.sort()
values_flat
# array([0.39198343, 0.46263733, 0.59380024, 1.        ])

coeff = values_flat[-2]
coeff
# 0.593800244493221

if coeff > 0.3:
    print(sentence_tokens[index]) # get the answer
# return
# Vegetables are all plants.
