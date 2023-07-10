import sys

lst = []
index_list = []
result = 0

for i in range(9):
    lst.append(int(sys.stdin.readline()))
    for j in range(i, 9):
        if i != j:
            index_list.append([i,j])

for k in range(len(index_list)):
    klist = index_list[k]
    result = sum(lst) - lst[klist[0]] - lst[klist[1]]
    a = lst[klist[0]]
    b = lst[klist[1]]
    if result == 100:
        lst.remove(a)
        lst.remove(b)
        lst.sort()
        print(*lst)
        break
