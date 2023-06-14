import pyautogui

# double click in a file (sample.txt)
position = pyautogui.position()
print(position)

pyautogui.doubleClick(132, 200)

# press the down arrow key to go to the ends of the text file
time.sleep(1) # 1 second
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.write('Python is good too!\n')

# copy all text from file
pyautogui.hotkey('command', 'a') # for mac
#pyautogui.hotkey('ctrl', 'a') # select all text, for windows

pyautogui.hotkey('command', 'c') # ctrl+c, for windows

# paste text 5 times
pyautogui.press(5*[down]) # = [down, down, down, down, down]
pyautogui.hotkey('command', 'v') # ctrl+v, for windows
