#!/usr/bin/env python3

import math
import os
import random
import re
import sys


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    difference = 6-n

    lowercase = re.compile("(?=.*[a-z]).*")
    uppercase = re.compile("(?=.*[A-Z]).*")
    digits = re.compile("(?=.*[0-9]).*")
    symbol = re.compile("(?=.*[!@#$%^&*()\-+ ]).*")

    matches = []
    matches.append(bool(lowercase.match(password)))
    matches.append(bool(uppercase.match(password)))
    matches.append(bool(digits.match(password)))
    matches.append(bool(symbol.match(password)))

    number_of_mismatch = matches.count(False)
    if difference > 0:
        if number_of_mismatch > difference:
            return number_of_mismatch
        elif number_of_mismatch == difference:
            return number_of_mismatch
        else:
            return difference
    else:
        return number_of_mismatch

if __name__ == '__main__':
    while(True):
        n = int(input().strip())

        password = input()

        answer = minimumNumber(n, password)

        print(f"{answer} changes required")
        print()
