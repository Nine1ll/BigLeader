import sys

N, B = map(int, sys.stdin.readline().split())

lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(65, 65+26):
    lst.append(chr(i))

ans = ""
while N != 0:
    ans += lst[N % B]
    N = N//B

print(ans[::-1])
