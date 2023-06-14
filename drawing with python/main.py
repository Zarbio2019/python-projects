import pyautogui
from mss import mss, tools

# DRAW
print(pyautogui.position()) # get position of mouse

pyautogui.moveTo(1218, 355, duration=1)
pyautogui.click()

dur = 0.1
pyautogui.drag(0, 200, duration=dur, button='left') # Down 200px
pyautogui.drag(60, 0, duration=dur, button='left') # Right 60px
pyautogui.drag(0, -3, duration=dur, button='left') # Up 3px
pyautogui.drag(0, 6, duration=dur, button='left') # Down 6px
pyautogui.drag(60, 0, duration=dur, button='left') # Right 60px
pyautogui.drag(0, -6, duration=dur, button='left') # Up 6px
pyautogui.drag(-60, 0, duration=dur, button='left') # Left 6px

pyautogui.move(60, 0, duration=dur) # Right back 60px
pyautogui.move(0, 3, duration=dur) # Down back 4px

pyautogui.drag(100, 0, duration=dur, button='left') # Right 100px
pyautogui.drag(0, -120, duration=dur, button='left') # Up 120px

pyautogui.move(0, -40, duration=dur) # Skip 40px up
pyautogui.drag(0, -40, duration=dur, button='left') # Up 40px

pyautogui.drag(-200, 0, duration=dur, button='left') # Left 220px
pyautogui.move(-50, -50) # move mouse

# SCREENSHOT
with mss() as screen:
  part = {'top': 345, 'left': 1208, 'width': 240, 'height': 220}
  image = screen.grab(part)
  tools.to_png(image.rgb, image.size, output='output2.png')
