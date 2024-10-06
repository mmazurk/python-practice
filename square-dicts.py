# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

def number_dict():
    number_dict = {}

    for i in range(1, 4):
        number_dict[i] = i**2

    return number_dict


room_for_squares = number_dict()
print(room_for_squares)
