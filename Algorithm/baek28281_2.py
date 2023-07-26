import sys

N, X = map(int, sys.stdin.readline().split())
price_lst = list(map(int, sys.stdin.readline().split()))

# X개를 연속된 2일에 걸쳐사는데 N일간 양말 가격이 주어짐
# 최소 가격을 원함 -> 그냥 2개 빼서 합이 최소인 것
price_sum = []
for i in range(N-1):
    price_sum.append(price_lst[i] + price_lst[i + 1])

min_=min(price_sum)

print(min_ * X)
