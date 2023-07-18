import sys


def sort_by_len(e):
    return len(e)


N = int(sys.stdin.readline())

str_list = []
for _ in range(N):
    word = sys.stdin.readline().replace("\n", "")
    if word not in str_list:
        str_list.append(word)
str_list.sort()
str_list.sort(key=sort_by_len)

for i in range(len(str_list)):
    print(str_list[i])
