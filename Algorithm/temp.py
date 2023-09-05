import sys

ujeans = sys.stdin.readline().rstrip()

if ujeans == "1":
    print("NO")


def mul(string_num1, string_num2):
    str1 = 1
    str2 = 1
    for i in range(len(string_num1)):
        str1 *= int(string_num1[i])
    for j in range(len(string_num2)):
        str2 *= int(string_num2[j])
    return str1 == str2


for i in range(1, len(ujeans)):
    if mul(ujeans[:i + 1], ujeans[i + 1:]):
        print('YES')
        break

    elif i == len(ujeans) - 1:
        print('NO')




