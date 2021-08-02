#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def roundUp(grade):
    return int(math.ceil(grade/5.0)) * 5

def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            rounded = roundUp(grade)
            if(rounded - grade < 3):
                result.append(rounded)
            else:
                result.append(grade)
    return result


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print()
    print('\n'.join(map(str, result)))
