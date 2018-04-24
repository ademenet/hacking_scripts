"""
"""
import argparse
import string
import itertools

UPPER = list(string.ascii_uppercase)
LOWER = list(string.ascii_lowercase)
DIGIT = list(string.octdigits)
# Generate the string "Aa1Aa2Aa3..."
STRING = str()
for combination in map("".join, itertools.product(UPPER, LOWER, DIGIT)):
    STRING = STRING + combination

def _get_offset(offset_str):
    if '0x' in offset_str:
        offset = bytes.fromhex(offset_str[2:]).decode('utf-8')
    else:
        offset = bytes.fromhex(offset_str).decode('utf-8')
    return STRING.index(offset)

def _string_generator(size):
    return STRING[:size]

def _argparser():
    parser = argparse.ArgumentParser(description='This software gives you the EIP offset')
    parser.add_argument('size', type=int, help='size of the string')
    args = vars(parser.parse_args())
    return args

def main():
    args = _argparser()
    print('\033[95m#1 Copy/paste this string in order to get a segfault:\033[0m')
    print(_string_generator(args['size']))
    print('\033[95m#2 Paste the symbols where segfault occured:\033[0m')
    offset = input('0x????????: ')
    print('\033[95m#3 Your EIP offset is: \033[0m', _get_offset(offset))

if __name__ == '__main__':
    main()