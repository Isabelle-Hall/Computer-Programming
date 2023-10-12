#Break in a loop
value = int(input("enter a number: "))
for n in range(2, value//2):
    if value % n == 0:
        print(value,"is not a prime number")
        break