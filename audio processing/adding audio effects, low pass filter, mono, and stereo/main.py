# Author: Zarbio Romulo

from pydub import AudioSegment

beat = AudioSegment.from_wav('beat.wav')

beat_low = beat.low_pass_filter(2000) # remove high frequencies above of 2000 decibels
beat_low.export('beat_low.wav')

# mono effect
beat_left = beat_low.pan(-1) # -1: left speaker high, right speaker 0 
beat_right = beat_low.pan(1) # 1: right speaker high, left speaker 0 
beat_right = beat_low.pan(-0.5) # -0.5: right speaker low, left speaker low 

# combine and export
beat_final = beat_left + beat_right + beat_low
beat_final.export('beat_final.wav')

#dir(AudioSegment) #show methods
