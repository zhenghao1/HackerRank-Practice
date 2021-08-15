#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def isAlternating(s):
 
    # Check if ith character matches
    # with the character at index (i + 2)
    for i in range ( len(s) - 2) :
        if (s[i] != s[i + 2]) :
            return False
         
     
 
    #If string consists of a single
    #character repeating itself
    if (s[0] == s[1]):
        return False
 
    return True

def getCombinations(s):
    distinct_characters = list(set(s))
    total_distincts = len(distinct_characters)
    if total_distincts < 2:
        return None
    size = total_distincts - 2
    tupled_combinations = list(combinations(list(set(distinct_characters)), size))
    return tupled_combinations

def alternate(s):
    temp = []
    combos = getCombinations(s)
    if combos is None:
        return 0
    for pair in combos:
        check_string = s.translate({ord(i): None for i in pair})
        if(isAlternating(check_string)):
            temp.append(len(check_string))
            
    if len(temp) == 0:
        return 0
    return max(temp)

if __name__ == '__main__':
    l = int(input().strip())

    s = input()

    result = alternate(s)

    print(f'Answer: {result}')

