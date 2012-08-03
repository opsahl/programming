from itertools import takewhile
from functools import reduce

# Solving project euler part two
#
#
def fibonacci():
    """ A generator that generates fibonacci numbers """
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

def solve(upto):
    """ Generates fibonacci numbers up to the limit, and then takes the sum of the even ones """
    fibgen = fibonacci()
    fibsuptogen = takewhile(lambda x: x < upto, fibgen)
    even_fibs = [ fib for fib in fibsuptogen if fib % 2 == 0]
    return reduce(lambda x, y: x + y, even_fibs)

print(solve(4000000))
