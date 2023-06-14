import pyautogui

# control the cursor of the mouse
# get coordinates of the mouse
position = pyautogui.position()
print(position) # Point(x=55, y=227)

# move mouse to specific coordinate
pyautogui.moveTo(139, 280) # x,y
pyautogui.moveTo(139, 280, duration=1) # 1 second, absolute position
pyautogui.move(100, 0, duration=1)

pyautogui.click(clicks=2) # mouse makes 2 clicks (may be to open a file)
#pyautogui.doubleClick() # the same

# CLICK ON WINDOWS
pyautogui.click(139, 280, clicks=2) # 2 clicks in a specific coordinate, by default left click
pyautogui.click(139, 280, button='right') # right click

# CLICK ON MAC
pyautogui.click(139, 280)
pyautogui.drag(139, 280, button='right')

#################################################

# Exercise: Dragn Paint:
pyautogui.moveTo(1326, 567, duration=1)
pyautogui.click()
pyautogui.drag(150, 0, duration=1, button='left')
pyautogui.drag(0, -150, duration=1, button='left')
pyautogui.drag(-150, 0, duration=1, button='left')
pyautogui.drag(0, 150, duration=1, button='left')
