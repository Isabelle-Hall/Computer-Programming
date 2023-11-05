#1 Write a function that accepts a positive integer as a parameter and then returns a representation of that number in binary (base 2).
# Hint: This is in many ways a trick question. Think!

def binary(number):
    """Positive integer into binary."""
    if number > 0:
        print(bin(number))
    else:
        print("You did not enter a positive number!")

binary(17)