import sys

N = int(sys.stdin.readline())

result = -1
list_5 = [i for i in range(0, 5000+1, 5)]
list_3 = [j for j in range(0, 5000+1, 3)]

for m, ele_5 in enumerate(list_5):
    for n, ele_3 in enumerate(list_3):
        if N == ele_5 + ele_3:
            result = m + n
            break
print(result)
