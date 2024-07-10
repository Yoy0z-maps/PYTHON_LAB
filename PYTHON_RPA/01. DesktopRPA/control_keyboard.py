import pyautogui
import pyperclip

# write (not support Korean)
pyautogui.write('startcoding',interval=0.25)

# countermeasure
pyperclip.copy('한글')
pyautogui.hotkey('command', 'v')

# command
pyautogui.press('enter')
pyautogui.press('up')

# SIMULTANEOUSLY
pyautogui.hotkey('command', 'c')
