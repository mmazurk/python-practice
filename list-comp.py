# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

def square_numbers(number_string):
    number_list = number_string.split(",")
    squares = [int(num)**2 for num in number_list if int(num) % 2 != 0]
    return squares


print(square_numbers("1,2,3,4,5,6,7"))
