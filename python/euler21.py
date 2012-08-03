import math

def find_divisors(number):
    result = [x for x in range(1, int(math.sqrt(number))) if number % x == 0]
    temp = [number // x for x in result if x != 1]
    result.extend(temp)

    return result

def sum_divisors(number):
    divisors = find_divisors(number)
    return sum(divisors)

def is_amicable(number):
    possible_match = sum_divisors(number)
    tested = sum_divisors(possible_match)

    if number == tested and number != possible_match:
        return True
    else:
        return False
 
amicable = [number for number in range(1, 10000) if is_amicable(number)]

print(sum(amicable))
