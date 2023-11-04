import math

squares = [4, 9, 16, 25]

squares = []
for x in range(10):
    squares.append(x*x)

# easier way is:

squares = [x * x for x in range(10)]

cubes = []
for x in range(2,21):
    cubes.append(x*x*x)
    print(cubes)

even_nums = [num for num in range(100,201) if num % 2 == 0]
# when if statement is True = value is evaluated and added to list

triples = [n for n in range(1,6) for count in range(3)]
print(triples)
# can have multiple for...in loops but can become complicated
# acts as a nested loop where inner loop is executed for every iteration of outer loop
