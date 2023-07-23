import sys

resistance = dict(black=[0, 1], brown=[1, 10], red=[2, 100], orange=[3, 1000], yellow=[4, 10000], green=[5, 100000],
                  blue=[6, 1000000], violet=[7, 10000000], grey=[8, 100000000], white=[9, 10 ** 9])

first = sys.stdin.readline().replace("\n", '')
second = sys.stdin.readline().replace("\n", '')
last = sys.stdin.readline().replace("\n", '')

ans = int(str(resistance[first][0])+str(resistance[second][0]))*resistance[last][1]

print(ans)
