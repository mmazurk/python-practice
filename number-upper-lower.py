# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

import string


def case_count(sentence):
    lower_count = 0
    upper_count = 0
    count = []

    for char in sentence:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        else:
            continue

    count.append(lower_count)
    count.append(upper_count)
    return count


phrase = "Hello, I think the dog just FARTED."
count = case_count(phrase)
print(count)


def case_count2(sentence):
    upper = 0
    lower = 0

    for char in sentence:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1

    return [lower, upper]


phrase2 = "Hello, I think the dog just FARTED."
count = case_count2(phrase2)
print(count)
