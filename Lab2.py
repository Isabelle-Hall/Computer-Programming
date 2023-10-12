#working with variables
total = 100
total = total + 99 #total += 99 is a shorter way to write this
print("The total is ", total)

total = total * 100 # total *= 100 # multiplies

total -= 1 #subtraction
print("The total is ", total)

total *= 4 #multiplication
print("The total is", total)

total /= 2 #division
print("The total is", total)

total = 98.2
count = 5
average = total / count


#data-types
type(False) #boolean
type(100.111) #float
type("Hello") #string
type(True) #boolean
type(100 / 5) #division operator always returns a float value
type(100 //5) #float

print(10+10) #result is calculated
print("10" + "10") #string is concatonated
print("ABC" * 10) #prints ABC 10 times

#calling built-in functions
name_length = ("Eric Idle")
print("The length of your name is ", len(name_length)) #gives number of characters in the name
print("The average was ", total/count) #passes two arguments

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

#single, double, and triple quotes
print("john")
print('john')
print('I would have "thought" you knew better')

#escape sequences
print("Hello! \nWhat is your name?")

#using triple quotes
print("""This is a triple quotes string""")
print("""This "can"
be 'spread' across
serparate lines""")

#indexing and slicing
surname = "Smith"
initial = surname[2] #prints letter i
print(initial)
#if give number out of letters available, eg 10, an error will occur
val = surname[-4] #negative starts count from end of name and goes backwards, m is printed
print(val)

middle = surname[1:4]
print(middle) #prints from the second letter to the third, mit is printed
#the second number is always one less thn given, so 4 would give the 3rd letter
copy = surname[:] #prints whole name
tail = surname[1:] #prints from second letter to the end
butlast = surname[:4] #print all letters but the last
#slicing out of range does not give error untlike indexing, eg tail = surname[1:100000]

#lists
names = ["Terry", "John", "Michael", "Eric"] #string
primes = [2, 3, 5, 7, 13, 17, 19, 23] #integers
slice = primes[0:5] #prints first 4 prime numbers
print(slice)

#mutable list can be changed after being created
names[0] = "Terry, G." #changes first name in names list
names[0:0] = ["Tim", "Barry"] #adds names to start of list
names.append #adds names to end of list
names = names + ["James"] #doesn't add to list but makes a new one
names += ["Jacob"] #does mutate existing list
nums = [1,2,3] * 5 #will print nums list 5 times

#immutable lists cannot be changed


