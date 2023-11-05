#2 Write a program that, when run from the command line, reports how many arguments were provided. 
# (Remember that the program name itself is not an argument).

import sys

number = int(input("Input a number: "))
print("The number you gave was", number)

print("Arguments provided: ", len(sys.argv))