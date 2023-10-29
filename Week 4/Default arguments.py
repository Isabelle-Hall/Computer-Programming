def displayMessage(msg, suffix = "?"):
    """Prints a message with a suffix."""
    print(msg, suffix)

displayMessage("Save file")
displayMessage("An error occurred", "!")

def multiply(a,b):
    """Multiplies a and b together"""
    answer = a * b
    return answer
multiply(a=3,b=5)