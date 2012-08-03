def parse(string):
    """ Parses a string with two number separated by a space and returns a tuple of the two numbers """
    str_nums = string.split()
    nums = [int(num) for num in str_nums]
    return tuple(nums)

def devideable(num, factor):
    """ Returns true or false depending on if num can be devided by factor """
    if num % factor == 0:
        return True
    else:
        return False


def sieve(high):
    """ Uses a sieve to find primes up to high, returns a tuple of the primes """

    nums = [num for num in range(2, high + 1)] # The + 1 is so that high is also in the set
    primes = []
    
    while nums:
        primes.append(nums.pop(0))
        nums = [num for num in nums if not devideable(num, primes[len(primes) - 1])] 

    return tuple(primes)

def find_primes(low, high):
    """ Find all the primes between the numbers """
    primes_upto_high = sieve(high)
    return [num for num in primes_upto_high if num >= low]

if __name__ == "__main__":
    times = int(input("Input number of cases: "))

    for i in range(times):
        string_to_parse = input("Input range for primes (num num): ")
        low, high = parse(string_to_parse)
        primes = find_primes(low, high)
        [print(prime) for prime in primes]
        print() # separate sets with an empty line
