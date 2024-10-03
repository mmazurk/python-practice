# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

def word_frequency(sentence):
    frequencies = {}
    words = sentence.split(" ")

    for word in words:
        if not word in frequencies.keys():
            frequencies[word] = 1
        else:
            frequencies[word] += 1

    sorted_keys = sorted(frequencies.keys())
    final_sorted_frequencies = {key: frequencies[key] for key in sorted_keys}
    print(final_sorted_frequencies)

    return None


sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
print(word_frequency(sentence))
