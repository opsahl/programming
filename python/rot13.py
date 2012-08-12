#!/usr/bin/env python
#
# a program to rot13 a file or a string

import argparse
import sys
import string

def code(letter):
    """ codes one letter in rot13

    >>> code('a')
    'n'
    """

    # we have to add 13 to the ascii value of the letter and wrap it around if it's over 122
    coded_ascii = ord(letter) + 13

    if coded_ascii > 122:
        coded_ascii -= 26

    return chr(coded_ascii)

def rot13(cleartext):
    """ en/decodes a string with rot13

    >>> rot13("abc")
    'nop'

    """
    
    coded = ""
    
    for letter in cleartext:
        if letter in string.ascii_letters:
            coded += (code(letter.lower()))
        else:
            coded += letter
    
    return coded


if __name__ == "__main__":
    # do doctests
    import doctest
    doctest.testmod()
    # Parse commandline and decide what to en/decode
    parser = argparse.ArgumentParser(description=""" This program will print the de/encoded version of the file in rot13, if you want to you can also redirect the output to a file. """)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--file", help="Input from file")
    group.add_argument("-s", "--string", help="String to en/decode")
    parser.add_argument("-o", "--output", help="Output to file, will erase file if one exists.")
    args = parser.parse_args()

    if args.string:
        cleartext = args.string
    if args.file:
        try:
            f = open(args.file, 'r')
        except IOError as e:
            print("I/O error {}: {}".format(e.errno, e.strerror))
        except TypeError as e:
            pass
        except:
            print("Unexpected error:", sys.exc_info()[0])
        else:
            cleartext = f.read()
            f.close()

    if args.output:

        try:
            f = open(args.output, 'w')
        except IOError as e:
            print("I/O error {}: {}".format(e.errno, e.strerror))
        else:
            f.write(rot13(cleartext))
            f.close()

    elif 'cleartext' in locals():
        print(rot13(cleartext))
    else:
        print("Could not open file, please look over your path and try again.")
