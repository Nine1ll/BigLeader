import sys
from itertools import permutations

n = int(sys.stdin.readline())
weight = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

min_weight = float('inf')
all_root = permutations(list(range(n)))

for p in all_root:
    sum_weight = 0
    is_visited = True
    
    for i in range(n - 1):
        visit = weight[p[i]][p[i + 1]]
        if visit == 0:
            is_visited = False
            break
        else:
            sum_weight += visit
    visit = weight[p[n - 1]][p[0]]
    
    if visit == 0:
        is_visited = False
    else:
        sum_weight += visit
    
    if is_visited and min_weight > sum_weight:
        min_weight = sum_weight

print(min_weight)