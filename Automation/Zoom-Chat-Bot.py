# Github: Mrtechtroid
import pyautogui as trump
import time
notimes = int(input("How Many Times should the Message Be Typed?"))
message = input("Message:")
print("Quickly Click Your Mouse Over the Zoom App")
time.sleep(5)
trump.hotkey("alt","h")
for i in range(notimes):
    trump.typewrite(message)
    trump.typewrite(["enter"])
