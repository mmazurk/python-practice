
from numpy import number


def list_and_tuple(nums):

    list_nums = [int(digit) for digit in str(nums)]
    tuple_nums = tuple(list_nums)

    return ({"list": list_nums, "tuple": tuple_nums})


solution = list_and_tuple(12345)
print(solution["list"])
print(solution["tuple"])
