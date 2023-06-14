import sounddevice
from scipy.io.wavfile import write

seconds = 5
fps = 44100 # frame per seconds, sampling rate (hertz)

myrecording = sounddevice.rec(frames=seconds * fps, samplerate=fps, channels=1) # 1 for laptop
#print(myrecording)
sounddevice.wait() # wait until audio ended
#print(myrecording)
write('output.mp3', fps, myrecording)

# In Mac give permission to PyCharm IDE to use recording
