#1 Write a program that prints a cheery message (such as "Hello World") on the screen. 
# Run it, and note that you have taken the first step to becoming a programmer!
print("Hello World!")

#2 Make a copy of the previous program, and modify it so that it displays your name. 
# So if your name is Herbert the message should become: Hello, Herbert!
print("Hello, Isabelle!")

#3  Over the summer, temperatures in Yorkshire reached 38.4C. 
# Write a program that converts this value in Celsius to the equivalent temperature in Fahrenheit, and then displays both.
tempc =38.4
tempf =(tempc * 1.8)+32
print("The temperature in celsius for Yorkshire reached: ", (tempc))
print("In fahrenheit this is: ", (tempf))

#4 In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014 times, was not out 162 times, and scored 48426 runs. 
# Write a program to calculate and display Boycott's batting average
matches = 609
bats = 1014
not_out = 162
runs = 48426
batting_average = runs / (bats - not_out)
print("Geoffrey Boycott's batting average is: ", (batting_average))

#5 The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups. 
# A lab group is 24 students, since this is the number of PCs in a lab. 
# Write a program that calculates how many groups are needed for the following number of students: 113, 175, 12. 
# Display how many full groups there will be, and how many students will be in the smaller "left over" group.
lab_group = 24
group1 = 113 // 24
group2 = 175 // 24
group3 = 12 / 24
print("For 113 students you will need ", group1, "groups")
print("For 175 students you will need ", group2, "groups")
print("For 12 students you will need ", group3, "groups")