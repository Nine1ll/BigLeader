import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    elif a**2 + b**2 == c**2:
        print("right")
    elif a**2 + c**2 == b**2:
        print("right")
    elif c**2 + b**2 == a**2:
        print("right")
    else:
        print("wrong")
