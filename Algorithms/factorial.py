#!/usr/bin/env python3
from utils.timer import timer
import time

def factorial(n: int) -> int:
    memo = {}
    if n in memo:
        return memo[n]
    elif n == 0 or n == 1:
        memo[n] = 1
        return 1
    else:
        f = n * factorial(n-1)
        memo[n] = f
    return f

def countTrailingZeroes(n: int) -> int:
    if n < 0:
        return -1

    count = 0

    while(n >= 5):
        n //= 5
        count += n

    return count

if __name__ == '__main__':
    num = int(input("Enter a number to calculate the factorial: "))
    time_start = time.perf_counter()
    dynamic_result = factorial(num)
    time_end = time.perf_counter()
    etime = time_end - time_start
    print(f"Factorial of {num} using dynamic programming: {dynamic_result}................Elapsed time: {etime:0.4f}")
    print(f"Number of trailing zeroes of {num} is: {countTrailingZeroes(num)}")

