#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    raise ValueError("Please pass the word to decode as an argument.\nOnly one argument is allowed")

word = sys.argv[1]
solution = ""

for (idx, letter) in enumerate(word):
    solution += chr(ord(letter)-idx)

print(solution)
