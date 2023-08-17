import sys

distance = []
dna = []

n, m = map(int, sys.stdin.readline().split())


def find_all_indexes(input_str, search_str):
    start = 0
    indexes = []

    while start < len(input_str):
        start = input_str.find(search_str, start)
        if start == -1:
            break
        indexes.append(start)
        start += 1

    return indexes


for _ in range(n):
    dna.append(sys.stdin.readline().rstrip())



'''
함수를 하나 만들어서 그냥 A, T, G, C의 모든 인덱스를 반환하고 그걸 비교하는 게 좋은 듯.
'''
