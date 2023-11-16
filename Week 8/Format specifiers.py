# Is a small string included after expressions withtin braces, must be prefixed by :


# Result is output to two decimal places
import math
r = 50
print(f"A circle with radius {r} has an area of {math.pi * r * r:.2f}")


width = 104.32
width = float(width)
height = 15.645
height = float(height)
print(f"The area of a rectangle with a width of {width} and a height of {height} is {width * height:.2f}")


# Control column width and alignment
name = "Donald"
age = 75
print(f"{name:15} - {age:10}")

# <	Aligns the value left within the available space
# >	Aligns the value right within the available space
# ^	Aligns the value to the centre within the available space
# =	Adds padding after the sign (numerical values only)


print(f"{name:$>20} - {age:$>20}")