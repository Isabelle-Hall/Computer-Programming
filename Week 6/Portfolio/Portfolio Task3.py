#3 Write and test a function that determines if a given integer is a prime number. 
# A prime number is an integer greater than 1 that cannot be produced by multiplying two other integers.

def prime(number):
    """Test if given integer is a prime."""
    for i in range(2, int(number/2)+1):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

prime(7)