# Github: Mr Techtroid
import pyautogui
import time
name = "Screenshot.png"
def screenshot():
	time.sleep(5)
	image = pyautogui.screenshot(name)
	image.show()

def timedscreenshot():
	timer = int(input("Time(s):"))
	time.sleep(timer)
	image = pyautogui.screenshot(name)
print("Type 1 for Screenshot in 5sec and 2 for Screenshot in Custom No. Of Seconds")
index = input(">")
if index == "1":
	screenshot()
elif index == "2":
	timedscreenshot()
else:
	exit()
