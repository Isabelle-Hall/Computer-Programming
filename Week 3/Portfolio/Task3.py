#3. Modify your previous program so that the password must be between 8 and 12 characters (inclusive) long.

password = input("Choose a password: ")

x = True
while x:  
    if (len(password)<8 or len(password)>16):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Password must be between 8 and 12 characters!")