# Author: Zarbio Romulo

from speech_recognition import Recognizer, AudioFile
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

recognizer = Recognizer()

# convert audio into text
with AudioFile('chile.wav') as audio_file:
  audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio)
#print(text)

# analyze the mood of the text
nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)
print(scores)

if scores['compound'] > 0:
  print('Positive Speech')
else:
  print('Negative Speech')
