#!/usr/bin/env python3

import math
import os
import random
import re
import sys


def christmas_tree(n):
    upper_bound = n + 1
    for pair in enumerate(range(1, upper_bound)):
        spaces = n - pair[1]
        hashes = sum(pair)
        line = ' ' * spaces
        line += '#' * hashes
        line += ' ' * spaces
        print(line)

if __name__ == '__main__':
    n = int(input().strip())
    christmas_tree(n)
