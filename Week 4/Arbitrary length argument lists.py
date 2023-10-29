def calcAve(*numbers): #'*' defines arbitrary length arguments which indicates use of a Tuple
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)

calcAve(8,9,20)
