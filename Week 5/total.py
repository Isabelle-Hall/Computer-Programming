#imports modules to the program
import sys
import statistics

#calucates the total
count = len(sys.argv)
total = 0
while count > 1:
    count -= 1 
    total += float(sys.argv[count])

#prints total to user
print("Total is", total)

#calculates average and prints to the user
average = statistics.mean([count, total])
print("Average is,", average)

#prints message to user if no argument was passed
if total == 0:
    print("No arguments were provided")