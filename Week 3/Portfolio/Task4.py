#4. Modify your program again so that the chosen password cannot be one of a list of common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password = input("Choose a password: ")
passcon = input("Confirm password: ")

bad_password = ['password', 'letmein', 'hello', 'justinbieber']
if password in bad_password:
    print("Password is not secure")

