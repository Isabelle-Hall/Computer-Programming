import math

squares = [4, 9, 16, 25]
squares.extend([49, 64, 100])
#or
squares[len(squares):] = [49, 64, 100]

squares.extend([121, 144, 169])
for n in squares:
    print(int(math.sqrt(n)))



help(list.extend)