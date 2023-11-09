# clear(), pop(), copy(), get() and update() can be used in dictionaries

stock = dict({"apple":10, "banana":15, "orange":11})

# pop and return stock level
stock.pop("orange")

#update stock to include two new fruits
stock.update(lemmon=15, strawberry=99)

print(stock)

help(dict)