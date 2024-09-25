# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

import math

def formula_thing(nums):
    c = 50
    h = 30
    numbers_list = nums.split(",")
    values = []

    for d in numbers_list:
        values.append(str(math.floor(math.sqrt(2 * c * int(d) / h))))

    answer = ",".join(values)

    return answer

formula_thing("100,150,180")

# https://www.w3schools.com/python/python_ref_string.asp