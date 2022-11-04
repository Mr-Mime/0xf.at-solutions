#!/usr/bin/python

import sys

# Characters of the morse alphabet
codes = ['.−','−...','−.−.','−..','.','..−.','−−.','....','..','.−−−','−.−','.−..','−−','−.','−−−','.−−.','−−.−','.−.','...','−','..−','...−','.−−','−..−','−.−−','−−..','−−−−−','.−−−−','..−−−','...−−','....−','.....','−....','−−...','−−−..','−−−−.']

# Characters of the alphabet and number 0-9
chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

# Creating a dict
zipped = zip(codes, chars)
morse_dict = dict(zipped)


###########
# Main code begins here
###########


inp = sys.argv[1:]
sol = ""

for c in inp:
    sol += morse_dict[c]

print(sol)
