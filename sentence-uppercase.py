# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def sentenece_case(word_list):

    final_list = []

    for item in word_list:
        capitalized = item.upper()
        final_list.append(capitalized)

    return final_list


answer = sentenece_case(["Hello world", "Practice makes perfect"])
print(answer)
