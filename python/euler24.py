# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
# listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
# 
# 012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
# 6, 7, 8 and 9?

def permutations(digit_list):
    """ Takes a list of digits, and returns a list of permutations, sorted in lexicographic order """

    if len(digit_list) == 1:
        return digit_list
    elif len(digit_list) == 2:
        return [[digit_list[0], digit_list[1]], [digit_list[1], digit_list[0]]]
    else:
        result = []
        for number in digit_list:
            rest_permutations = []
            for lst in permutations(list(filter(lambda x: x != number, digit_list))):
                rest_permutations.append(lst)            
            for item in rest_permutations:
                item.insert(0, number)

            result.extend(rest_permutations)

        return result

def prettify(digit_list):
    """ collapses a list into a string of the digits """
    result = ""
    
    for digit in digit_list:
        result += str(digit)
    
    return result

if __name__ == "__main__":
    perms = permutations(list(range(10)))
    print(prettify(perms[1000000-1]))
