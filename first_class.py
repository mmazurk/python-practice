
# This is just remembering how to create a class in python

class GetString(object):
    def __init__(self):
        self.s = "Dog"

    def setString(self, str):
        self.s = str

    def getString(self):
        return self.s


my_string = GetString()
print(my_string.getString())
my_string.setString("Poop")
print(my_string.getString())
