# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def all_evens1(start, end):

    evens = []

    for num in range(start, end):
        digits = [int(digit) for digit in str(num)]
        odds = [item for item in digits if item % 2 != 0]
        if (len(odds)) > 0:
            continue
        evens.append(num)

    return evens


answer = all_evens1(1000, 3000)
print(answer)

# Better version with lots of clever things going on
# This uses modulo 10 to strip off the last digit
# It also uses // which is floor division to take all numbers but the last


def all_evens2(start, end):

    evens = []

    for num in range(start, end):
        is_even = True
        temp = num

        while temp > 0:
            digit = temp % 10
            if digit % 2 != 0:
                is_even = False
                break
            temp = temp // 10

        if is_even:
            evens.append(num)

    return evens


answer = all_evens2(1000, 3000)
print(f"The answer is {answer}")
