# Trying to solve project euler problem 11
# -- textfile for problem is saved as euler11.txt

from functools import reduce

def readfile():
    f = open('euler11.txt', 'r')
    filecontent = [line for line in f] 
    return filecontent

def prepare_table(str_table):
    strnum_table = [string.split() for string in str_table]
    numtable = []
    for row in strnum_table:
        numtable.append([int(strnum) for strnum in row])
    return numtable

def get_table():
    return prepare_table(readfile())

def check_horiz(table):
    max_product = 0
    for line in table:
        last = len(line) - 3
        for i in range(last):
            temp = line[i] * line[i + 1] * line[i + 2] * line[i + 3]
            if temp > max_product:
                max_product = temp
    return max_product

def check_vert(table):
    max_product = 0
    for i in range(len(table) - 3):
        for j in range(len(table[i])):
            temp = table[i][j] * table[i+1][j] * table[i+2][j] * table[i+3][j]
            if temp > max_product:
                max_product = temp
    return max_product

def check_diag1(table):
    max_product = 0
    for i in range(len(table) - 3):
        for j in range(len(table[i]) - 3):
            temp = table[i][j] * table[i+1][j+1] * table[i+2][j+2] * table[i+3][j+3]
            if temp > max_product:
                max_product = temp
    return max_product

def check_diag2(table):
    max_product = 0
    for i in range(len(table) -3):
        for j in range(3, len(table)):
            temp = table[i][j] * table[i+1][j-1] * table[i+2][j-2] * table[i+3][j-3]
            if temp > max_product:
                max_product = temp
    return max_product

if __name__ == "__main__":
    table = get_table()
    max_product = 0
    results = []
    results.append(check_horiz(table))
    results.append(check_vert(table))
    results.append(check_diag1(table))
    results.append(check_diag2(table))
    for result in results:
        if result > max_product:
            max_product = result
    print(max_product)
