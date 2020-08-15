import pyautogui
import time
'This computer on which this has been built has a display of 1366x768'
pyautogui.hotkey("win", "d")
'This command will minimise all tasks and bring desktop'
pyautogui.hotkey("win", "r")
'This command will open Run using the shortcut windows+r'
pyautogui.click(100, 620)
'This Command Will Take the cursor to the position of run Command Box'
time.sleep(0.01)
'This is used to give the above commands time to execute'
pyautogui.typewrite(["backspace"])
'This will clear the text there'
pyautogui.typewrite("mspaint")
'This will type mspaint'
pyautogui.typewrite(["enter"])
time.sleep(0.01)
'This will bring up the Paint'
time.sleep(5)
pyautogui.click(289, 72)
'This will click the Text Bar'
pyautogui.doubleClick(65, 372)
'This will click at the canvas'
for x in range(0, 5):
    pyautogui.hotkey("ctrl", "shift", ">")
'The statement has been repeated to increse the default size of text in paint from 8 to 24'
pyautogui.typewrite("Hello World!")
'This statement will type Hello World In Paint'
