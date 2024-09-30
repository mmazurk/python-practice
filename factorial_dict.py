# With a given number n, write a program to generate a dictionary that contains the number and it's square
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def squares_list(num):

    ans = {}

    for i in range(1, num+1):
        ans[i] = i**2

    return ans


sol = squares_list(8)
print(sol)
