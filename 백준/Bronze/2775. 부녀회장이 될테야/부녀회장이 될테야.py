import sys

t = int(sys.stdin.readline())

member_num = [[i for i in range(0, 14+1)]]

for j in range(1, 14+1):
    temp_lst = []
    num = 0
    for k in range(0, 14+1):
        num += member_num[j-1][k]
        temp_lst.append(num)
    member_num.append(temp_lst)

for _ in range(t):
    k = int(sys.stdin.readline())  # 층
    n = int(sys.stdin.readline())  # 호
    print(member_num[k][n])