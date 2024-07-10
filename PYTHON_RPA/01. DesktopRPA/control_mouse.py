import pyautogui
import time

# Screen Size
print(pyautogui.size())

# show mouseInfo
# pyautogui.mouseInfo()

# Mouse Postion
time.sleep(2)
print(pyautogui.position())

# Move Mouse Postion moveTo(X, Y, duration)
pyautogui.moveTo(739,226)

# Mouse Click
pyautogui.click() # left
pyautogui.click(button='right') # right
pyautogui.doubleClick() # double click
pyautogui.click(clicks=3, interval=1) # total click 3 times, for every second

# Moust Drag
pyautogui.dragTo(549, 80, 2) # X, Y, Duration