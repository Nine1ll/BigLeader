import sys

k = int(sys.stdin.readline())

fib_minus_two = 0
fib_minus_one = 1
fib_current = 0

if k == 0:
    fib_current = fib_minus_two
elif k == 1:
    fib_current = fib_minus_one

for i in range(2, k + 1):
    fib_current = fib_minus_two + fib_minus_one
    fib_minus_two = fib_minus_one
    fib_minus_one = fib_current

print(fib_current)
