"""
"""
import argparse
import string
import itertools

UPPER = list(string.ascii_uppercase)
LOWER = list(string.ascii_lowercase)
DIGIT = list(string.octdigits)

def _string_generator(size):
    string = str()
    for combination in map("".join, itertools.product(UPPER, LOWER, DIGIT)):
        string = string + combination
    return string[:size]

def _argparser():
    parser = argparse.ArgumentParser(description='This software gives you the EIP offset')
    parser.add_argument('size', type=int, help='size of the string')
    args = vars(parser.parse_args())
    return args

def main():
    # Parse arguments
    args = _argparser()
    # String generation
    print(_string_generator(args['size']))

if __name__ == '__main__':
    main()