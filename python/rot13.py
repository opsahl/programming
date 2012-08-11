#!/usr/bin/env python
#
# a program to rot13 a file or a string

import argparse
import sys

def rot13(cleartext):
    return cleartext


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f", "--file", help="Input from file")
    group.add_argument("-s", "--string", help="String to en/decode")
    args = parser.parse_args()

    if args.string:
        cleartext = args.string
    if args.file:
        try:
            f = open(args.string)
            cleartext = f.read()
        except IOError as e:
            print("I/O error {}: {}".format(e.errno, e.strerror))
        except:
            print("Unexpected error:", sys.exc_info()[0])
        else:
            f.close()

    if 'cleartext' in locals():
        print(rot13(cleartext))
    else:
        print("Could not open file, please look over your path and try again.")
