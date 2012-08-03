def get_nums_from_file(name):
    f = open(name)
    lines = [int(line) for line in f]
    return lines

def solve(nums):
    result = sum(nums)
    result = str(result)[:10]
    return result

if __name__=="__main__":
    nums = get_nums_from_file('euler13.txt')
    print(solve(nums))
