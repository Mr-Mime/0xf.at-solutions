#!/usr/bin/python

import base64
import sys

if len(sys.argv) != 2:
    raise ValueError("Please pass the word to decode as an argument.\nOnly one argument is allowed")

inp = sys.argv[1]
solution = base64.b64decode(inp)

print(str(solution, 'utf-8'))
