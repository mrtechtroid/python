#Github: Mr Techtroid
password = input("Type Password:")

pscore = 0
if len(password) < 10:
	print("Length Of Password Is Too Short...(Less Than 8 Chars)")
elif len(password) < 15:
	print("Length Of Password Is Short...(Less Than 15 Chars)")
	pscore = pscore + 1
else:
	print("Length Of Password is above 15 which is Good")
	pscore = pscore + 2
capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=[}]{|\\:;'\"<>,.?/"
scc = 0
scn = 0
scs = 0
# Capital Letters
for i in range(0,26):
	if password.find(capitals[i]) != -1:
		scc = 1
		break
if scc == 1:
	print("Password Contains A Capital Character")
	pscore = pscore + 2
else:
	print("Password Doesnt Contain A Capital Character")
# -----------------------------------------------------------
# Numbers
for i in range(0,10):
	if password.find(numbers[i]) != -1:
		scn = 1
		break
if scn == 1:
	print("Password Contains A Number")
	pscore = pscore + 2
else:
	print("Password Doesnt Contain Number")
# -----------------------------------------------------------
# Special Characters
for i in range(0,30):
	if password.find(symbols[i]) != -1:
		scs = 1
		break
if scs == 1:
	print("Password Contains A Special Character")
	pscore = pscore + 2
else:
	print("Password Doesnt Contain A Special Character")
# -----------------------------------------------------------
print("Your Password Score is " + str(pscore))
if pscore > 7:
	print("You have a Good Password.Good Job. ")
elif pscore > 5 and pscore < 7:
	print("Your password is not that much safe.. Make your password Much More Safer.")
else:
	print("Please Consider making yourself a better password as this password can be cracked very soon. ")