#!/usr/bin/python

import sys

# Check for correct input
if len(sys.argv) != 3:
    print("Please pass the scrambled words as the first argument and the dictionary file as the second argument")

# Read the hash and password file name
scramble  = sys.argv[1].split(";")
word_file = open(sys.argv[2])

# Extract all word from the word list
word_list = []
for word in word_file:
    word_list.append(word.replace("\n", ""))


# Search for scrambled words














# Function to check wether the passed words are anagrams
def isAnagram(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
