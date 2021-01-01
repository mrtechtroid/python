# Github: Mr Techtroid
import random
choices = ["stone","paper","scissor","scissor","paper","stone"]

def choice():
	pscore = 0
	cscore = 0
	draw = 0
	while True:
		word = input(">").lower()
		number = random.randint(0,5)
		if word == "/stop":
			break
		elif word == "/help":
			helpmenu()
		elif word == "/new":
			pscore = 0
			cscore = 0
			draw = 0
			print("New Game Initiated")
		elif word == "/current":
			currentres(pscore,cscore,draw)
		elif word == "stone" or word == "st":
			print("Computer Chose:" + choices[number])
			if choices[number] == "paper":
				cscore += 1
			elif choices[number] == "scissor":
				pscore += 1
			elif choices[number] == "stone":
				draw +=1
			else:
				print("ERROR")
				break
		elif word == "paper" or word == "p":
			print("Computer Chose:" + choices[number])
			if choices[number] == "scissor":
				cscore += 1
			elif choices[number] == "stone":
				pscore += 1
			elif choices[number] == "paper":
				draw +=1
			else:
				print("ERROR")
				break
		elif word == "scissor" or word == "sc":
			print("Computer Chose:" + choices[number])
			if choices[number] == "stone":
				cscore += 1
			elif choices[number] == "paper":
				pscore += 1
			elif choices[number] == "scissor":
				draw +=1
			else:
				print("ERROR")
				break

	result(pscore,cscore,draw)


def result(pscore,cscore,draw):
	print("-------FINAL SCORE----------")
	print("No. of Wins:" + str(pscore))
	print("No. of Loses:" + str(cscore))
	print("No. of Draws:" + str(draw))
	if pscore > cscore:
		print("You Won the Game by " + str(pscore-cscore) +" points")
	elif pscore < cscore:
		print("You Lost the Game by " + str(cscore-pscore) +" points")
	else:
		print("It's was a draw. Both have equal points. ")
	input("Press Any Key to Close")

def currentres(pscore,cscore,draw):
	print("No. of Wins:" + str(pscore))
	print("No. of Loses:" + str(cscore))
	print("No. of Draws:" + str(draw))
	if pscore > cscore:
		print("You are Winning the Game by " + str(pscore-cscore) +" points")
	elif pscore < cscore:
		print("You are Losing the Game by " + str(cscore-pscore) +" points")
	else:
		print("It's is a draw currently. Both have equal points. ")
def helpmenu():
	print("To Play the game type stone or st for Stone type paper or p for Paper and scissor or sc for Scissor.")
	print("To Stop the game anytime type /stop.")
	print("Type /new to start a new game.")
	print("Type /current to see the current scores. ")


print("Rock Paper Scissor Game By Mr Techtroid")
print("Type /help for game instructions.")
choice()