import sys

N, B = sys.stdin.readline().split()

lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(65, 65+26):
    lst.append(chr(i))

squares = len(N) - 1
ans = 0
for c in N:
    ans += lst.index(c)*int(B)**squares
    squares -= 1

print(ans)
