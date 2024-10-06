# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def gen_list(start, end):
    final_list = []

    for i in range(start, end+1):
        final_list.append(i**2)

    return final_list


l = gen_list(1, 20)
print(l[5::1])
print(tuple(l))
