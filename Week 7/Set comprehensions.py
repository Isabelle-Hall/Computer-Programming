sentence = "this is a sentence containing some letters"
unique_letters = {x for x in sentence if x != " "}

print(unique_letters)

# duplicates are not allowed so each letter will appear in the set once, including the spaces
# can restrict values by appending an if statement