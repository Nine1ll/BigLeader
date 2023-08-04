import sys

n = int(sys.stdin.readline())
han_su = 0

for num in range(1, n + 1):
    lst = []
    string_n = str(num)
    if len(string_n) <= 2 :
        han_su+=1
    else:
        for i in range(len(string_n)-1):
            lst.append([int(string_n[i]), int(string_n[i+1])])

        for idx, ele in enumerate(lst):
            lst[idx] = ele[0] - ele[1]

        a = 0
        for el in lst:
            if lst[0] == el:
                a += 1
        if a == len(lst):
            han_su += 1

print(han_su)