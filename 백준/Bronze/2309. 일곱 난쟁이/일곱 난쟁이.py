import sys
dwarf = [int(sys.stdin.readline()) for _ in range(9)]
index_lst = []


for i in range(9):
    for j in range(i+1, 9):
        index_lst.append([i, j])

for idx in index_lst:
    sum_h = sum(dwarf)
    sum_h = sum_h - dwarf[idx[0]] - dwarf[idx[1]]
    if sum_h == 100:
        dwarf.remove(dwarf[idx[1]])
        dwarf.remove(dwarf[idx[0]])
        dwarf.sort()
        print(*dwarf)
        break
        