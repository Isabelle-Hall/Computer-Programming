stock = dict({"apple":10, "banana":15, "orange":11})

# access a value by proving its key as an index
stock = dict({"apple":10, "banana":15, "orange":11})

stock["pear"] = 50  # add new key:value pair
stock["apple"] += 1  # increase apple stock value

stock["kiwi"] = 10

print(stock)

#membership testing
if "apple" in stock:
    print("Apples have a stock level")
