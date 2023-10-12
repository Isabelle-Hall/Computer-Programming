#4 A kind teacher wishes to distribute a tub of sweets between her pupils. 
# She will first count the sweets and then divide them according to how many pupils attend that day. 
# Write a program that will tell the teacher how many sweets to give to each pupil, and how many she will have left over.
no_sweets = int(input("How many sweets?: "))
students = int(input("How many students?: "))
give = no_sweets // students
left = no_sweets % students
print("Each student can have", give, "sweets, there will be", left, "left over.")