# 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다고 한다.
# 다만 걷는 거리가 같을 때에는 아래층의 방을 더 선호한다.
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    num = N // H + 1
    floor = N % H
    if N % H == 0:
        num = N // H
        floor = H
    print(f'{floor*100+num}')
