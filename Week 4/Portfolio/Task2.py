#2. Write a function that has a single string as its parameter, and returns the number of uppercase letters, and the number of lowercase letters in the string. 
# Test the function with a short program.

def stringContent(word):
    """Prints the amount of lower and uppercase letters in a word."""
    l={"upperCase":0, "lowerCase":0}
    for str in word:
        if str.isupper():
            l["upperCase"]+=1
        elif str.islower():
            l["lowerCase"]+=1
        else:
            pass
    print("Number of upper case letters: ", l["upperCase"])
    print("Number of lower case letters: ", l["lowerCase"])

stringContent("HellO")