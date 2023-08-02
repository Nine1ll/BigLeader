import sys

n = int(sys.stdin.readline())

member = [list(sys.stdin.readline().split()) for _ in range(n)]
member.sort(key=lambda member: int(member[0]))

for mem in member:
    print(f"{mem[0]} {mem[1]}")
