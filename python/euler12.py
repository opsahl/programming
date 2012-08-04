def triangle_nums():
    triangle_num = 1
    i = 2
    while True:
        yield triangle_num
        triangle_num += i
        i += 1

def find_num_divisors(num):
    num_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            num_divisors += 1

    return num_divisors

num_divisors = 1
triangle = triangle_nums()
while num_divisors < 500:
    current = next(triangle)
    num_divisors = find_num_divisors(current)
print(current)

