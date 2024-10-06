# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

def print_tuples(tup):
    halfway_point = len(tup)//2

    first_half = tup[0:halfway_point]
    second_half = tup[halfway_point:]

    return [first_half, second_half]


answer = print_tuples((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(answer)


def find_evens_tuple(tup):
    evens = []

    for item in tup:
        if item % 2 == 0:
            evens.append(item)

    return tuple(evens)


answer2 = find_evens_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(answer2)
