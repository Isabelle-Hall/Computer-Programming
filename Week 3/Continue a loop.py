#Continue a loop
grades = [20, 50, 43, 33, 90, 15]
pass_mark = 40
passes = 0
total = 0
for grade in grades:
    if grade < pass_mark:
        continue
    passes += 1
    total += grade

print("average pass mark was", total/passes)

numbers = [10, 20, 30, 90, 200, 30, 22, 11]
for number in numbers:
    print(number)
    if number >100:
        break
else:
    print("All numbers processed")