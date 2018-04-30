"""
This script generates a string with several differents characters like "Aa1Aa2Aa3Aa4..." and calculate the offset for 
buffer overflows.

Use python 3.+ to execute it.

Usage:
    $> python3 string_generator.py 200
    #1 Copy/paste this string in order to get a segfault:
    Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad
    8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag
    #2 Paste the symbols where segfault occured:
    0x????????: 0x41336141
    #3 Your EIP offset is:  9
"""
import argparse
import string
import itertools

UPPER = list(string.ascii_uppercase)
LOWER = list(string.ascii_lowercase)
DIGIT = list(string.digits)
# Generate the string "Aa1Aa2Aa3..."
STRING = str()
for combination in map("".join, itertools.product(UPPER, LOWER, DIGIT)):
    STRING = STRING + combination

def _get_offset(offset_str):
    # Remove '0x' prefix
    if '0x' in offset_str:
        offset = bytes.fromhex(offset_str[2:]).decode('utf-8')
    else:
        offset = bytes.fromhex(offset_str).decode('utf-8')
    # Handle big and little endian
    try:
        offset_index = STRING.index(offset)
    except:
        offset_index = -1
    try:
        offset_index = STRING.index(offset[::-1])
    except:
        offset_index = -1
    if offset_index == -1:
        print("\033[31mAn error occured.\033[0m")
        exit()
    return offset_index

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