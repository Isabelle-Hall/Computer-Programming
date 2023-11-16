# open() returns a file object
f = open("info.txt")

# readline() to read line by line
for l in "info.txt":
    print(f.readline())

# or read() to read entire contents

# close() to close the file
f.close()


