#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = ''
    for c in s:
        if c.isupper():
            result += chr((ord(c) + k - 65) % 26 + 65)
        elif c.islower():
            result += chr((ord(c) + k - 97) % 26 + 97)
        else:
            result += c
    return result

if __name__ == '__main__':

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

