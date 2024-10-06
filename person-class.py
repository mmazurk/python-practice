# Define a class, which have a class parameter and have a same instance parameter.

class Person:

    def __init__(self, age=1.5):
        self.data = {"age": age}

    def assign_name(self, name):
        self.data["name"] = name


bloopis = Person()
bloopis.assign_name("Bloopis")
print(bloopis.data["name"], "is", bloopis.data["age"])


class Utility:
    my_constant = 2287

    @staticmethod
    def add_things(a, b):
        return a + b

    @staticmethod
    def subtract_things(a, b):
        return a - b


print("The answer is", Utility.add_things(1, 2))
