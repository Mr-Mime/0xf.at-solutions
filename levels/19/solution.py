#!/usr/bin/python

import sys

# Dictionary with the value for each character
char_dict = {
    "a" : 4,
    "b" : 6,
    "c" : 8,
    "d" : 6,
    "e" : 9,
    "f" : 12,
    "g" : 8,
    "h" : 12,
    "i" : 16,
    "j" : 10,
    "k" : 15,
    "l" : 20,
    "m" : 12,
    "n" : 18,
    "o" : 24,
    "p" : 14,
    "q" : 21,
    "r" : 28,
    "s" : 35,
    "t" : 16,
    "u" : 24,
    "v" : 32,
    "w" : 18,
    "x" : 27,
    "y" : 36,
    "z" : 45
}

# Read input argument
inp = sys.argv[1]
inp.lower()

sum = 0

for char in inp:
    if char.isalpha():
        sum += char_dict[char]
    else:
        sum += int(char)

print(sum)
