
def sum_numbers(num):
    string_num = str(abs(num))
    final_sum = 0

    for digit in string_num:
        final_sum += int(digit)

    return final_sum


print(sum_numbers(1234))
