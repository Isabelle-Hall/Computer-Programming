some_list = [8, 2, 4, 99, 1]
some_list.sort()
print(some_list)

sorted_list = sorted(some_list)
print(some_list) # order of original list is unchanged, produces new list in memory

some_list.sort(reverse=True)
print(some_list)


names = [ "Mark", "Alicia", "Ben" ]
names.sort()
print(names) # strings are sorted alphabetically

names.sort(key=lambda n : len(n)) # sorts string by word length
print(names)

new_names = [ "Eric", "anna", "Sophie", "sam" ]
new_names.sort()
print(new_names) # lower-case letters appear later than upper-case with default sort

str.upper("anna") # convert to uppercase
str.upper("sam")
new_names.sort(key=lambda n : len(n))
print(new_names)