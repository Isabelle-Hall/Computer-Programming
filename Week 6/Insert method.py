import math

squares = [4, 9, 16, 25]
squares.insert(0, 2)
#first argument is position, second is value
for n in squares:
    print(int(math.sqrt(n)))


