#1 Last week you wrote a program that printed out a cheery greeting including your name. 
# Take a copy of it, and modify it so that the user enters their name at the keyboard, and then receives a greeting. 
# For example: Hello, what is your name? 
# Mr Apricot.
# Hello, Mr Apricot. Good to meet you!
name = input("Hello, what is your name? ")
print("Hello,", name, "Good to meet you!")

#2 Write a program that prompts a user to enter a temperature in Celsius, and then displays the corresponding temperature in Fahrenheit, like so: 
# Enter a temperature in Celsius: 32.5 32.5C is equivalent to 90.5F.
tempc = float(input("What is the temperature in celsius? "))
tempf = (tempc * 1.8)+32
print("In fahrenheit, the temperature is:", tempf)

#3 The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups. 
# A lab group is usually 24 students, but this is sometimes varied to create groups of similar size. 
# Write a program that prompts for the number of students and group size, and then displays how many groups will be needed and how many will be left over in a smaller group. 
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101 students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.
no_students = int(input("How many students?: "))
group_size = int(input("Required group size?: "))
groups = no_students // group_size
remainder = no_students % group_size
if remainder == 1:
    print("There will be", groups, "groups, with", remainder, "student left over")
else:
    print("There will be", groups, "groups, with", remainder, "students left over")

#4 A kind teacher wishes to distribute a tub of sweets between her pupils. 
# She will first count the sweets and then divide them according to how many pupils attend that day. 
# Write a program that will tell the teacher how many sweets to give to each pupil, and how many she will have left over.
no_sweets = int(input("How many sweets?: "))
students = int(input("How many students?: "))
give = no_sweets // students
left = no_sweets % students
print("Each student can have", give, "sweets, there will be", left, "left over.")