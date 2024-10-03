# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

def iterate_numbers(endpoint):
    for num in range(0, endpoint):
        if num % 7 == 0:
            yield num


# numbers_divisible_by_seven_up_to_100 = iterate_numbers(100)
# for number in numbers_divisible_by_seven_up_to_100:
#     print(number)


# This is using a class

class DivisibleBySeven:
    def __init__(self, endpoint=100):
        self.endpoint = endpoint

    def iterate_numbers(self):
        for num in range(0, self.endpoint):
            if num % 7 == 0:
                yield num


class DivisibleBySevenStatic:
    @staticmethod
    def iterate_numbers(endpoint=100):
        for num in range(0, endpoint):
            if num % 7 == 0:
                yield num


for number in DivisibleBySevenStatic.iterate_numbers():
    print(number)
