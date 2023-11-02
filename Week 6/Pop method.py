#pop mutates a list by removing and returing the right-most value from the list

import math

squares = [4, 9, 16, 25]
squares.pop()
for n in squares:
    print(n)

help(list.pop)