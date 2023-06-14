# Author: Zarbio Romulo

from googletrans import Translator

translator = Translator()

translation = translator.translate('Oa mai oe?', dest='en').text # 'en' = to English

print(translation) # return: How are you today?