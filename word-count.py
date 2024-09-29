# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def word_count(sentence):
    letters = {}
    digits = {}

    for char in sentence:

        if char in [" ", "!", ".", "?", ";", ":"]:
            continue

        elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            if (digits.get(char)):
                digits[char] = digits[char] + 1
            else:
                digits[char] = 1

        else:
            if (letters.get(char)):
                letters[char] = letters[char] + 1
            else:
                letters[char] = 1

    digit_count = sum(digits.values())
    letter_count = sum(letters.values())

    return [digit_count, letter_count]


answer = word_count("123456 Hello there darkness my old friend 123456.")
print(f"The number of digits and letters is {answer}")
