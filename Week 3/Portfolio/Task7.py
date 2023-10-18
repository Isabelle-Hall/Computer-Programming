#7. Modify your "Times Table" program so that the user enters the number of the table they require.
# This number should be between 0 and 12 inclusive.


number = int(input("Enter a number for the times table: "))
for count in range (0,13):
    print(number,"x",count,"=",number*count)