import sys

N = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
square_num = [i**2 for i in range(1, 31+1)]
minority = 0

for num in num_list:
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        minority += 1

print(minority)
