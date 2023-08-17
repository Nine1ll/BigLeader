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

'''
최소 선택해서 내가 갔던 곳이면 그 다음으로 작은 곳을 선택하고 

모든 조합을 다해봐야해 근데 내가 간 곳은 제외하고 더해야 함

1에서 시작 시작한 곳으로 다시 돌아와야 해서 그 마지막 간 곳에서 시작한 곳의 번호로 돌아오는 건 고정 
2번 시작  5 1번 도착 15 3번 도착 12 4번 1번 고정 8 -> 40
3번 시작 6 1번 도착 10 2번 도착 4번 도착 10 , 9 -> 35  
'''