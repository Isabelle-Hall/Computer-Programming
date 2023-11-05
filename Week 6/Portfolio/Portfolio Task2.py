#2 Write and test a function that takes an integer as its parameter and returns the factors of that integer. 
# (A factor is an integer which can be multiplied by another to yield the original).

def factor(number):
    """Return factors of given number."""
    print("The factors of", number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

factor(34)