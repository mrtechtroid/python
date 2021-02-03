# Github: Mr Techtroid
def square():
	points = int(input("No of points:"))
	string = ""
	for j in range(points):
		string += "* "
	for i in range(points):
		print(string)

square()

def rtriangle():
	points = int(input("Points At Base:"))
	string = ""
	for i in range(1,points+1):
		string += "* "
		print(string)
rtriangle()



def diamond(rows): 
    n = 0

    for i in range(1, rows + 1): 
        # loop to print spaces 
        for j in range (1, (rows - i) + 1): 
            print(end = " ") 
          
        # loop to print star 
        while n != (2 * i - 1): 
            print("*", end = "") 
            n = n + 1
        n = 0
          
        # line break 
        print()  
  
    k = 1
    n = 1
    for i in range(1, rows): 
        # loop to print spaces 
        for j in range (1, k + 1): 
            print(end = " ") 
        k = k + 1
          
        # loop to print star 
        while n <= (2 * (rows - i) - 1): 
            print("*", end = "") 
            n = n + 1
        n = 1
        print() 
rows = int(input("No. Of Rows:"))
diamond(rows)