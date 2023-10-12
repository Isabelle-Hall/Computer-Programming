#Logical Operators with Expressions
age = 30
print(age >=18 and age <= 65) #True
print(age <18 or age>65) #False
print(not age > 18) #False

print((age>=18 and age <=65) and (not age==30)) #False / 'not' has higher precedence than 'and'
