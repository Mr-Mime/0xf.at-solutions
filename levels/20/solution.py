#!/usr/bin/python

import sys
import hashlib

# Check for correct input
if len(sys.argv) != 3:
    print("Please pass the hash to decode as the first argument and the password list file as the second argument")

# Read the hash and password file name
hash  = sys.argv[1]
pw_fn = sys.argv[2]

# Open the file
pw_file = open(pw_fn, 'r')

found_solution = False
solution = "nothing found :("

words = []

for word in pw_file:
    words.append(word.replace("\n", ""))

# Hash is generated form to words together
# Thus we will combine each word with each other
for (idx, word_1) in enumerate(words):
    if idx%100 == 0:
        print("\rRun " + str(idx) + "/" + str(len(words)), end="")
    
    for word_2 in words:
        word = word_1+word_2

        if hash == hashlib.md5(word.encode('utf-8')).hexdigest():
            found_solution = True
            solution = word
            break

    if found_solution: break

print(solution)

pw_file.close()