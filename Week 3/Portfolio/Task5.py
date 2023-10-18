#5. Modify your program a final time so that it executes until the user successfully chooses a password.
# That is, if the password chosen fails any of the checks, the program should return to asking for the password the first time.


password = input("Choose a password: ")

bad_password = ['password', 'letmein', 'hello', 'justinbieber']

while password != bad_password:
    if password in bad_password:
        print("Password is not secure")
    if password not in bad_password:
        passcon = input("Confirm password: ")
        if password == passcon:
            print("Password set.")
        else:
            print("Passwords do not match.")
    break

x = True
while x:  
    if (len(password)<8 or len(password)>16):
        break
    else:
        x=False
        break

if x:
    print("Password must be between 8 and 12 characters!")

