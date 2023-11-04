#1. Functions are often used to validate input. 
# Write a function that accepts a single integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive), or False otherwise. 
# Write a short program to test the function.

def singleParameter(number):
    """Returns True if the number is between 0-100, otherwise returns False."""
    if number >= 0 and number <= 100:
        return True
    else:
        return False

singleParameter(60)