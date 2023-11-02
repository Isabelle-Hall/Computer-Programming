# include different data-types and are immutable

student = ("Griffin, P.", 2, 38.2) # tuple packing
# can be used without brackets

address = (265, "Carnegie Village", "LS6")

empty = ()
the_one = "neo", # for a tuple with one element, use trailing comma


print(student[0])
name, year, average_grade = student # sequence unpacking


x, y, z = 10, 20, 30 # multiple assignment


def calc_squares(x, y):
    return ( x * x, y * y )
a,b = calc_squares(42, 92)
# return more than one value from a function


my_range = (10, 30)
for i in range(*my_range):
    print(i)
# can take a variable number of arguments
# unpacks my_range tuple during the call, results in equivalent to range(10, 30)
# * causes each element to be passed as a separate argument

