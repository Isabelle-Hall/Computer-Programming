# The mode of operation is specified using a second string type parameter.
# This can contain a single character that specifies whether the file is to be opened for reading (r), writing (w), appending (a) or reading and writing (r+).
# An additional letter can also be appended that, if present, indicates the file should be processed as binary (b) rather than text.

# If a file that does not exist is opened for writing (w) or appending (a) then the file is automatically created.
# If it is opened for reading (r) or reading and writing (r+) then the file must exist otherwise an error will be reported.


# open new file for writing
f1 = open("nextfile.txt", "w")

# open existing file for appending
f2 = open("file123.txt", "a")

# open file for reading and writing
f3 = open("fileABC.txt", "r+")

# open file for reading in binary mode
f4 = open("image.png", "rb")
