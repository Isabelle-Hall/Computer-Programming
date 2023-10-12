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
