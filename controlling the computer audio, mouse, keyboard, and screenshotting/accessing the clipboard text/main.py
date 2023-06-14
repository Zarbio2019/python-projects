import pyautogui
import pyperclip

position = pyautogui.position()
print(position)

pyautogui.doubleClick(126, 231)
pyautogui.hotkey('command', 'a') # select all text
pyautogui.hotkey('command', 'c') # copy

text = pyperclip.paste()
pyautogui.alert(text) # show message in your computer
print(text)
