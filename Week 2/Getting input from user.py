#getting input from user
name = input("What is your name? ")
print("Hello,", name)

age = input("Enter your age: ")
age = int(age) #changes str to int
print("In one year, your age will be,", age + 1)

num_1 = input("Give one number: ")
num_2 = input("Give a second number: ")
num_1 = int(num_1)
num_2 = int(num_2)
print("Multiplying these numbers gives the total,", num_1 * num_2)