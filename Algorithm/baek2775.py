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
'''
0층 1호 1 => 1층 1호 1 => 2층 1호 1
0층 2호 2 => 1층 2호 (1) + 2 => 2층 2호 1 + 1+ 2
0층 3호 3 => 1층 3호 (1 + 2) + 3
0층 4호 4 => 1층 4호 (1 + 2 + 3) + 4
...
0층 i호 i
'''

# def member_count(floor, room_number):
#     if floor == 0:
#         return room_number
#     else:
#         member_num = 0
#         for j in range(1, room_number+1):
#             member_num += member_count(floor - 1, j)
#             print(f"member_count({floor - 1}, {j}) : {member_count(floor - 1, j)}")
#             print(member_num)
#             return member_num
