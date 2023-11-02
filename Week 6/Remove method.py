import math

squares = [4, 9, 16, 25]
squares.remove(25)
for n in squares:
    print(int(math.sqrt(n)))

list = [1, 2, 3, 1, 2]
list.remove(2) #removes first 2 in the list
print(list)
