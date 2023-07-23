# import sys
#
#
# def fibonacci(k):
#     if k == 0:
#         return 0
#     elif k == 1:
#         return 1
#     else:
#         return fibonacci(k - 2) + fibonacci(k - 1)
#
#
# k = int(sys.stdin.readline())
#
# print(fibonacci(k))

import sys

def fibonacci(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1

    fib_minus_two = 0
    fib_minus_one = 1
    fib_current = 0

    for i in range(2, k + 1):
        fib_current = fib_minus_two + fib_minus_one
        fib_minus_two = fib_minus_one
        fib_minus_one = fib_current

    return fib_current

k = int(sys.stdin.readline())

print(fibonacci(k))
