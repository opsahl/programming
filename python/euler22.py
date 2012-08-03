#solving project euler problem 22

def read_file(filename):
    """ Reads the file and returns a string of the contents """
    output = ""

    f = open(filename)
    output += f.read()
    f.close()

    return output

def parse_namestring(string):
    """ Parses the fileformat in the string from the file, and returns a sorted list of names """
    result = []
    doublequoted = string.split(',')

    # Remove double quotes
    for name in doublequoted:
        result.append(name[1:-1])

    result.sort()

    return result

def alphabetic_value(string):
    """ Calculates the alphabetic value of a string (the sum of values for letters in the string a=1 b=2 ...) """
    result = 0
    characters = list(string)

    for character in characters:
        result += ord(character) - 64  # -64 since the ordinal number of A = 65 B = 66 etc.

    return result

def total_namescore(string_list):
    result = 0

    for i in range(len(string_list)):
        result += alphabetic_value(string_list[i]) * (i + 1)

    return result

if __name__ == "__main__":
    string = read_file('names.txt')
    parsed = parse_namestring(string)
    print(total_namescore(parsed))

