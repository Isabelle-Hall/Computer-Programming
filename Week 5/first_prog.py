#asks the user to input a number
number = input("Enter a number: ")

#changes the input to an integer
number = int(number)

#prints the number back to the user in a string
print("The numbered entered was", number)

#determines whether the number was odd or even
if (number % 2) == 0:
	print("That is an even number")
else:
	print("That is an odd number")

#determines whether the number is divisible by 10
if (number % 10) == 0:
	print("It is divisible by 10")
else:
	print("It is not divisible by 10")