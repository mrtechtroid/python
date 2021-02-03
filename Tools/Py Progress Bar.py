# Github: Mr Techtroid
# This Program May Not Give Desired Results With Interpreters
import time
from os import system, name
# Modify The Following Values To Change How It Works
plen = 10
plength = 50
tps = 0.1
pbar = "="
# Use █ for a modern Style Unicode+2588
def easyprogress():
	for i in range(plen):
		if i != (plen-1):
			print(pbar, end = "")
		else:
			print(">")
		time.sleep(tps)
	print("Welcome")

def advprog(pbar):
	str_pbar = pbar
	for i in range(plength):
		print(str_pbar,">  ","["+str(2*i)+"%"+" completed]")
		str_pbar += pbar
		time.sleep(tps)
		if name == "nt":
			_ = system("cls")
		elif name == "posix":
			_ = system("clear")
		else:
			print("ERROR 101: We Dont Support Follow OS Yet. ")
	print("Welcome")
easyprogress()
advprog(pbar=pbar)



