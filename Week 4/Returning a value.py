def findMax(a,b):
    """Find the maximum of two values."""
    if ( a > b ):
        max = a
    else:
        max = b
    return max
  
valuea = input("What is the value of a: ")
valueb = input("What is the value of b: ")
findMax(a=valuea,b=valueb)