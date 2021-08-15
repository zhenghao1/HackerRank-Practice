import math

def reverse(num):
    rev_num = 0
    while (num > 0):
        last_number = num % 10
        rev_num = rev_num * 10 + last_number
        num = num // 10

    return rev_num

if __name__ == '__main__':
    times = int(input("Enter number of tests: ").strip())
    for _ in range(times):
        number = int(input("Enter the integer to reverse: ").strip())
        reversed_integer = reverse(number)
        print(reversed_integer)
