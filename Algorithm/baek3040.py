import sys

dwarf = []
found = False

for _ in range(9):
    dwarf.append(int(sys.stdin.readline()))

for i in range(9):
    for j in range(i+1, 9):
        sum_dwarf = sum(dwarf)
        sum_dwarf = sum_dwarf - dwarf[i] - dwarf[j]
        if sum_dwarf == 100:
            dwarf.remove(dwarf[j])
            dwarf.remove(dwarf[i])
            found = True
            break
    if found:
        break

for ele in dwarf:
    print(ele)