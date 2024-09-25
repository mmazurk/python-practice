
"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
"""


def find_numbers(start, end):

    nums = range(start, end + 1)
    answer = []

    for num in nums:
        if num % 7 == 0 and num % 5 != 0:
            answer.append(num)

    return answer


answer = find_numbers(5000, 5500)
print(answer)
