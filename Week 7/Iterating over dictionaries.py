stock = dict({"apple":10, "banana":15, "orange":11})

# print keys
for item in stock:
    print(item)

# print values
for level in stock.values():
    print(level)

# print both in a string
for item,level in stock.items():
    print(item, "has a stock level of", level)
