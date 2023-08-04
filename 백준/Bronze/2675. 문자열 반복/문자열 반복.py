t = int(input())
for i in range(t):
    r,s = input().split()
    ans = ""
    for c in s:
        ans=ans+c*int(r)
    print(ans)