
def Func(N):
    ret = 0
    for i in range(1, N + 1):
        ret += i
    return ret


def func(N):
    if N <= 0:
        return 0
    return N + func(N-1)


n = int(input())
print(Func(n))
print(func(n))
