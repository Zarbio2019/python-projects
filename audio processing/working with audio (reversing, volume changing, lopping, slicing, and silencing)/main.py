# Author: Zarbio Romulo

from pydub import AudioSegment

original = AudioSegment.from_wav('beat.wav')
print(type(original))
print(original)

# reverse audio
reversed = original.reverse()
reversed.export('reversed.wav')
reversed = reversed + 15 # reversed plus 15 decibels (more loud)

# see the audio methods
# print(dir(original))

# extract the first 2 seconds of the audio
first_two = original[0:2000]
first_two.export('first_two.wav')

print(len(original)) # return in milliseconds

# merge 2 audios (original + reversed)
merged = original * 2 + AudioSegment.silent(1000) + reversed
# * 2: 2 times
# AudioSegment.silent(1000): silent for 1 second
merged.export('merged.wav')