def make_factorial(upto):
    result = 1
    for i in range(2, upto):
        result *= i

    return result

def listify(number):
    result = []
    strnum = str(number)
    for digit in strnum:
        result.append(int(digit))

    return result

print(sum(listify(make_factorial(100))))
