#6. Write a program that takes a centigrade temperature and displays the equivalent in fahrenheit. 
# The input should be a number followed by a letter C. The output should be in the same format.

def centIntoFahr(cent):
    """Converts temperature from centigrade into fahrenheit."""
    temp = int(cent[:-1])
    fahr = (temp * 1.8) + 32
    print(cent, "is", fahr, "fahrenheit")

centIntoFahr("22C")