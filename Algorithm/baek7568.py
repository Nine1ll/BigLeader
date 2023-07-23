import sys

n = int(sys.stdin.readline())

people_list = []

for _ in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    people_list.append([weight,height])

for person in people_list:
    rank = 1
    for people in people_list:
        if person[0] < people[0] and person[1] < people[1]:
            rank+=1
    print(rank, end=' ')
