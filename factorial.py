# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def factorial(num):
    if num == 1:
        return 1

    answer = num * factorial(num - 1)
    return answer


solution = factorial(8)
print(f" The solution is {solution}")
