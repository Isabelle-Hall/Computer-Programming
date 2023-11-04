#8. Modify the previous program so that it can process any number of values. 
# The input terminates when the user just pressed "Enter" at the prompt rather than entering a value.

import statistics

def find(*temp):
    """Finds max, min and mean of six temperatures."""
    min_value = min(*temp)
    print("The minimum value is", min_value)
    max_value = max(*temp)
    print("The maximum value is", max_value)
    mean_value = statistics.mean([*temp])
    print("The mean value is", mean_value)

find(23, 43, 98, 56, 10)