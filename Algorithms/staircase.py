#!/usr/bin/env python3

import math
import os
import random
import re
import sys


def staircase(n):
    upper_bound = n + 1
    for i in range(1, upper_bound):
        spaces = n - i
        line = ' ' * spaces
        line += '#' * i
        print(line)

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
