names = set(["John", "Eric", "Terry", "Michael", "Graham", "Terry"])

name = input("Enter your name: ")
if name not in names:
    print("You are not listed in the set of known names")


# Sets are mutable so both accessor and mutator and comparison type operations exist

#accessors:
# | or union() === adds members to the set
# & or intersection() === find common elements
# - or difference() === find elements in one set but not other
# ^ or symmetric_difference() === find elements in either set but not both

staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}

staff = staff.union({"Mark", "Ringo"})
print(staff)

staff_directors = staff.intersection(directors)
print(staff_directors)

external = directors.difference(staff)
print(external)

staff_or_external = directors.symmetric_difference(staff)
print(staff_or_external)


#mutators:
# update()
# intersection_update()
# difference_update()
# symmetric_difference_update()

vowels = set({"a", "e", "i"})

add_missing = vowels.update({"o", "u"})
print(vowels)