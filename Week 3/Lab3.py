#Boolean Expressions
print(10 < 100) #True
print(100 != 100) #False
print(50 >= 50) #True

age = 19
print(age > 18) #True
print(age < 21) #True
print(age < 31) #True

print("a" < "b") #True
print("b" < "a") #False
print("John" < "Terry") #True / J is lower in the alphabet than T

print("john" < "Terry") #False / j is higher in T in Python / capital letters evaluate les-than lower-case

print(5 < 10.2) #True
#print(5 < "Monty") #Error / not same data type
#print(5 < "5") #Error / not same data type

#Logical Operators with Expressions
age = 30
print(age >=18 and age <= 65) #True
print(age <18 or age>65) #False
print(not age > 18) #False

print((age>=18 and age <=65) and (not age==30)) #False / 'not' has higher precedence than 'and'

#Chaining Relational Operators
weight = 140
height = 164
print(100 < weight and weight < 200) #True
print(height > 131 and height < 160) #False

#Membership Testing


#If Statement


#Else Clause


#Elif Clause


#Non-Boolean Conditions


#Ternary Operator


#While and For Loops


#Range() Function


#Break


#Continue