#4 Computers are commonly used in encryption. 
# A very simple form of encryption (more accurately "obfuscation") would be to remove the spaces from a message and reverse the resulting string. 
# Write, and test, a function that takes a string containing a message and "encrypts" it in this way

def encrypt(phrase):
    """Function takes a string and removes the spaces and reverses the result."""
    no_space = (phrase.replace(" ", ""))
    flip = no_space[::-1]
    print(flip)

encrypt("this is a message")