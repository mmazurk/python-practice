# Define a function that can convert a integer into a string and print it in console.
def inttostring(x): return print(str(x))


inttostring(50)

# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.


def sumstring(x, y): return print(int(x) + int(y))


sumstring("100", "100")


# Define a function that can accept two strings as input and concatenate them and then print it in console.
def concatstring(x, y): return print(str(x) + str(y))


concatstring("a", "b")

# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.


def lengthstring(x, y): return print(len(str(x) + str(y)))


lengthstring("abc", "def")


# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
def isevenorodd(x):
    if x % 2 == 0:
        return print("even")
    else:
        return print("odd")


isevenorodd(1)
