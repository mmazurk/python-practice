
# The question just asked me to calculate a square, but I played around with passing functions instead.
# I also used lambda functions here and leanred that it can't be over one line.

def doMath(function, value): return function(value)


def complexMath(val: int) -> int:
    for i in range(1, 5):
        val *= i
    return val


print(doMath(lambda x: x**2, 5))
print(doMath(lambda x: x/100, 3.234))
print(doMath(complexMath, 100))
