#Elif Clause
age = int(input("How old are you? "))
if age > 100:
    print("you are very old,")
    print("well done!")
elif age > 80:
    print("you are fairly old")
    print("pretty good!")
elif age > 40:
    print("you are middle aged")
    print("never mind")
elif age >30 and age <40:
    print("You're almost middle aged!!!")
else:
    print("you are not very old - yet")