# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


def sort_tuples(input):
    name_sets = [item for item in input.split("\n")]
    name_sets = [tuple(item.split(",")) for item in name_sets]
    name_sets = [(name, int(age), int(score))
                 for name, age, score in name_sets]

    answer = sorted(name_sets, key=lambda x: (x[0], x[1], x[2]))
    print(answer)


lines = "Tom,19,80\nJohn,20,90\nJony,17,91\nJony,17,93\nJson,21,85"
sort_tuples(lines)

# This is just sorting practice in general

mylist = ["short", "loooooong", "loooooooonger"]
sorted_list = sorted(mylist, key=len)
print(sorted_list)

newlist = [-1, 1, 5, -66, 6, 27]
sorted_newlist = sorted(newlist, key=abs)
print(sorted_newlist)
