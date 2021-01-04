# Github: Mr Techtroid, AmithS01
import random
namelist = [
"Hi, Can I Know Your Name?",
"Hello Friend, What is your Name?",
"May I ask you what your name is?",
"Hi I think User might not be a good Name. So can you tell me your name.",
]
introduction = [
"Welcome to the Simple Temperature Calculator",
"I am Called Simple Temperature Calculator. Simple Right?:-)",
"I am Simple Temperature Calculator. You can Call me STC.",
]
tempprompt = [
"Write the temperature you like to convert? (e.g., 45F, 102C etc.)",
"Hey So what you want me to Calculate? Like 45F, 102C etc. ",
"I am a Geek. So What Conversion Should I help you with? ",
]
errorprompt = [
"I Couldnt Understand What You Wrote. Maybe You Could Type Again..",
"Hey there was some Problem. I couldnt Answer What You Had Written. ",
]
def interactive(): 
  temp = input(tempprompt[random.randint(0,2)])
  degree = int(temp[:-1])
  i_convention = temp[-1]
  if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
    print("Hey "+name+" the temperature in", o_convention, "is", result, "degree.")
  elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"
    print("Hey "+name+" the temperature in", o_convention, "is", result, "degree.")
  else:
    print(errorprompt[0,3])
    quit()
def plain():
  print("May be you wanted me to be fast... Its fine..Enter the Temperature in F or C.")
  temp = input("Temperature in C/F:")
  degree = int(temp[:-1])
  i_convention = temp[-1]
  if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
    print(str(result)+o_convention)
  elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"
    print(str(result)+o_convention)
  else:
    print("ERROR")
    quit()


name = input(namelist[random.randint(0,3)])
print("Hello " +name+ " , " + introduction[random.randint(0,2)])
it = input("Do you want Me To Be Interactive? yes/no:").lower()
if it == "yes":
  interactive()
else:
  plain()
ans=input("Are you happy with what I have helped you with, "+name+"?")
if ans == "yes":
  print("Good to hear that " +name+ "!")
elif ans == "no":
  print("Sorry "+name+ "I will Try To Be Better Soon")
elif ans == "":
  print("Was it soo bad that you cant give a yes or no " +name+ "!")
else:
  print("Seriously... i  just wanted yes or no, "+name+ "!")
  print("ok then take this one easy, "+name+ "!")
print("Just Wanna Tell Something, I am Co-Developed By Mrtechtroid and AmithS01. You can check these two awesome developers who bought me to life. ")
print("See ya "+name+" !")

