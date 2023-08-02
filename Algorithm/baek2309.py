import sys
# 9개 중에 7개를 뽑거나
# 9개 중에 2개를 빼거나 => 이게 더 좋은 방식 이긴 함.
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
