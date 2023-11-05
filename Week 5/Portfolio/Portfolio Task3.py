#3 Write a program that takes a bunch of command-line arguments, and then prints out the shortest. 
# If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them.

import sys

numbers = sys.argv[1:]
numbers_sort = sorted(numbers, key=lambda x: float(x))
print("Shortest value is", numbers_sort[0])

