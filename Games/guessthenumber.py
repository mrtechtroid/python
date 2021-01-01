# Github: Mr Techtroid
import random
print("Guess The Number I have In My Mind. If you want to know the answer in between type ':close'.")
print("Type /cb to Change Number Range.")

counter = 1
minn = 0
maxn = 10000
number = random.randint(minn,maxn)

while True:
	a = input("Guess:")
	if a == "/cb":
			minn = int(input("Min Value:"))
			maxn = int(input("Max Value:"))
			print("Value And Counter Reseted")
			a = 0
			counter = 0
			number = random.randint(minn,maxn)
	if a == ":close":
			print("Sad that you couldnt find my number. The number was " + str(number))
			break
	elif int(a) < minn or int(a) > maxn:
			print("The Limit is " + str(minn) + " to " + str(maxn))
			counter = counter + 1
	elif int(a) > number:
			print("Your Number is Greater Than My Number")
			counter = counter + 1
	elif int(a) < number:
			print("Your Number is Smaller Than My Number")
			counter = counter + 1
	elif int(a) == number:
			print("Congrats, You Found the Number I was Thinking Of in " + str(counter) +" attempts")
			break
	else:
			print("ERROR")
			break
