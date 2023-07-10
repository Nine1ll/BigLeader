import sys

n, m = sys.stdin.readline().split()

if int(n[-1]) > int(m[-1]):
    print(n[::-1])
elif int(n[-1]) < int(m[-1]):
    print(m[::-1])
else:
    if int(n[-2]) > int(m[-2]):
        print(n[::-1])
    elif int(n[-2]) < int(m[-2]):
        print(m[::-1])
    else:
        if int(n[-3]) > int(m[-3]):
            print(n[::-1])
        elif int(n[-3]) < int(m[-3]):
            print(m[::-1])
