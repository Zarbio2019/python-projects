from mss import mss

with mss() as screen:
  screen.shot(output='screenshot.png')
  