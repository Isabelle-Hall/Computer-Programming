#7. Write a program that reads 6 temperatures (in the same format as before), and displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. 
# If you hunt, you might also find one for the mean.

import statistics

def find(temp1, temp2, temp3, temp4, temp5, temp6):
    """Finds max, min and mean of six temperatures."""
    min_value = min(temp1, temp2, temp3, temp4, temp5, temp6)
    print("The minimum value is", min_value)
    max_value = max(temp1, temp2, temp3, temp4, temp5, temp6)
    print("The maximum value is", max_value)
    mean_value = statistics.mean([temp1, temp2, temp3, temp4, temp5, temp6])
    print("The mean value is", mean_value)

find(23, 43, 65, 12, 96, 62)