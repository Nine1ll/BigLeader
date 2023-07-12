
def constructor(integer):
    length = len(str(integer))
    return_integer = integer
    for i in range(length):
        return_integer += int(str(integer)[i])
    return return_integer


N = input()

ans = int(N) - 9 * len(N)
# for i in range(int(N)+1):
#     result = constructor(i)

while True:
    if ans <= int(N):
        result = constructor(ans)
        if result != int(N):
            ans = ans + 1
        else:
            print(ans)
            break
    else:
        ans = 0
        print(ans)
        break

