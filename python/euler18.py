def read_file(filename):
    """reads the file and makes it into a string"""
    pyramid = ""
    f = open(filename)
    for line in f.readlines():
        pyramid += line
    f.close()

    return pyramid

def format_pyramid(in_string):
    list_of_strings = in_string.split('\n')
    #we get an extra list as a cause of the split, so we pop it
    list_of_strings.pop()
    
    result = []

    for string in list_of_strings:
        temp = string.split()
        result.append([int(string) for string in temp])

    return result

def make_pairs(in_list):
    result = []
    for i in range(len(in_list) - 1):
        result.append([in_list[i], in_list[i + 1]])

    return result

def reduce_line(in_pairs):
    return [max(pair[0], pair[1]) for pair in in_pairs]
        

def add_lists(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    return result

def reduce_pyramid(pyramid):
    while len(pyramid) > 1:
        last_line = pyramid.pop()
        pairs = make_pairs(last_line)
        reduced = reduce_line(pairs)
        pyramid[-1] = add_lists(pyramid[-1], reduced)

    return pyramid[0][0]

if __name__=="__main__":
    string_in = read_file("euler18.txt")
    list_list_numbers = format_pyramid(string_in)
    print(reduce_pyramid(list_list_numbers))

