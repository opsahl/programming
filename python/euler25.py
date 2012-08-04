# What is the first term in the Fibonacci sequence to contain 1000 digits?

def fibonacci():
    """ A generator that generates fibonacci numbers """
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    fibgen = fibonacci()
    current = next(fibgen)

    term = 1

    while len(str(current)) < 1000:
        current = next(fibgen)
        term += 1

    result = next(fibgen)
    term += 1
    print(term)
