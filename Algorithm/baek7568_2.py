import sys

n = int(sys.stdin.readline())

people_list = []
w_list = [0]*n

for _ in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    people_list.append([weight, height])

for i, person in enumerate(people_list):
    for people in people_list:
        if person[0] < people[0] and person[1] < people[1]:
            w_list[i] -= 1

sorted_list = sorted(w_list, reverse=True)

rank_dict = {}
for rank, num in enumerate(sorted_list, start=1):
    if num not in rank_dict:
        rank_dict[num] = rank

for num in w_list:
    print(rank_dict[num], end=" ")
