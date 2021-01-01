# Github: Mr Techtroid
number = input("Number:")
terms = len(number)
sum = 0
for i in range(terms):
	a = int(number[i])
	sum = sum + int(a)**terms
if sum == int(number):
	print("It is an Armstrong Number")
else:
	print("It is not an Armstrong Number")
