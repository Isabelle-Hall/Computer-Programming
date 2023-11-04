#4. When processing data it is often useful to remove the last character from some input (it is often a newline). 
# Write and test a function that takes a string parameter and returns it with the last character removed. 
# (If the string contains one or fewer characters, return it unchanged.)

def removeLast(message):
    """Removes last character from a string."""
    blank = ""
    if message == blank:
        return message
    elif message == len(message) * message[0]:
        return message
    else:
        print(message[:-1])

removeLast("This is a message.")