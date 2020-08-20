#Github: Mrtechtroid
def simple():
    print("Welcome To Simple Calculator")
    print("Here you can Add(+), Subtract(-), Multiply(*) and Divide(/)")
    num1 = input("Enter the First Number:")
    operator = input("Enter the Operation :")
    num2 = input("Enter the Second Number:")
    num1 = float(num1)
    num2 = float(num2)
    if operator == "+":
        out = num1 + num2
    elif operator == "-":
        out = num1 - num2
    elif operator == "*":
        out = num1 * num2
    elif operator == "/":
        out = num1 / num2
    else:
        out = "Please Enter A Valid string"
    print("Answer: " + str(out))
    print("Do you want to go back or re-calculate")
    msgres = input("1. Exit 2. Recalculate:")
    if msgres == "1":
        exit()
    else:
        simple()

simple()