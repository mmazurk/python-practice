# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

def digit_addition(value):
    """returns the value of a+aa+aaa+aaaa"""

    answer = 0
    string_value = str(value)

    for i in range(1, 5):
        temp = int(string_value * i)
        answer += temp

    return answer


digit = 5
print(digit_addition(digit))
