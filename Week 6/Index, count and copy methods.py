colours = [ "red", "green", "yellow", "blue", "red" ]

print(colours.index("yellow")) # gives position of value in list
print(colours.index("red",3)) # search from given range
print(colours.index("blue"))

print(colours.count("red")) # how many times element appears

new_colours = colours.copy()
print(new_colours)

colours.append("orange")
print(colours)
print(new_colours) # copy doesn't have new element

del colours[0] # removes first value
del colours[-1:] # removes last colour
del colours # removes colour variable