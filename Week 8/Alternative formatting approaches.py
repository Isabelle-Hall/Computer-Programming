name = "Donald"
age = 75

print("Name is %s, and age is %.2f" % (name, age))


# Also possible to perform formatting with a more manual approach by making calls to string methods available.
print(name.rjust(15), " - ", str(age).center(10))    # align column width

print(f"{name:>15} - {age:^10}")    # easier way
