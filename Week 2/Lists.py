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