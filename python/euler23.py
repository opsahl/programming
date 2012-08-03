# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.  

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot
# be reduced any further by analysis even though it is known that the greatest
# number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.  

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math

LIMIT = 28123

def find_divisors(number):
    """ Returns a list of divisors for a number """
    result = [int(x) for x in range(1, int(math.ceil(number / 2))) if number % x == 0]
    temp = [int(number / x) for x in result if x != 1]
    result.extend(temp)
    result = list(set(result))

    return result

def sum_divisors(number):
    """ Returns the sum of the divisors of a number """
    divisors = find_divisors(number)
    return sum(divisors)

def is_abundant(number):
    """ Checks if a number is abundant (sum of divisors are greater than the number """
    if number < sum(find_divisors(number)):
        return True
    else:
        return False

def get_abundant_numbers_upto(number):
    """ Gets a list of all abundant numbers up to the number given """
    return [number for number in range(1, number) if is_abundant(number)]

def get_sums_under_from(in_list, limit):
    result = []

    for number1 in in_list:
        for number2 in in_list:
            temp = number1 + number2
            #print("%d + %d = %d" % (number1, number2, temp))
            # if the sum of the two numbers are over the limit, we don't need to go any further on this number1
            if number2 > number1:
                break
            elif temp <= limit:
                #print("adding %d" % temp)
                result.append(temp)
            else:
                break

    return set(result)

if __name__ == "__main__":
    abundant = get_abundant_numbers_upto(LIMIT)
    abundant_sums = get_sums_under_from(abundant, LIMIT)
    not_sum_of_abundant = sum([i for i in range(1, LIMIT + 1)]) - sum(abundant_sums)
    print(not_sum_of_abundant)
    #print(abundant_sums)
    print(find_divisors(100))
    
