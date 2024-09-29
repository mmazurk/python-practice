# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def simple_order1(str):
    word_list = str.split(" ")
    final_list = []
    for word in word_list:
        if word in final_list:
            continue
        final_list.append(word)
    final_list.sort()
    return final_list


# You can use a set to pull out duplicates in a list
def simple_order2(str):
    word_list = [word for word in str.split(" ")]
    final_list = list(set(word_list))
    final_list.sort()
    print(final_list)
    return final_list


my_string = "hello world and practice makes perfect and hello world again"
answer1 = " ".join(simple_order2(my_string))
print(answer1)
