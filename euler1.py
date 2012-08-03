from functools import reduce

def solve(max):
    nums = [num for num in range(1, max) if num % 3 == 0 or num % 5 == 0]
    sum = reduce(lambda x, y: x + y, nums)
    return sum

print(solve(10))
print(solve(1000))
