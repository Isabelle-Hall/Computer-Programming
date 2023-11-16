# Python has a generic mechanism for dealing with errors, called exception handling.

# To ensure that a file is always closed, whether an error occurs or not, there is a construct provided in Python.
# The 'with' statement can be used to wrap file access within a code block.
# The advantage of this is that the file is automatically closed once the code block finishes.
# The 'with' statement includes the opening of the file, then the code within the associated block accesses that file.

with open("info.txt") as f:
    lines = f.readlines()
    print(lines)


