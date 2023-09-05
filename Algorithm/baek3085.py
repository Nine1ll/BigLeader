import sys

n = int(sys.stdin.readline())
max_candy = 0
candy_list = [list(sys.stdin.readline().rstrip()) for _ in range(n)]


def candy_count(candy):
    max_candy = 0
    for row in range(n):
        temp_candy = 1
        for col in range(n-1):
            if candy[row][col] == candy[row][col+1]:
                temp_candy += 1
            else:
                temp_candy = 1
            if temp_candy > max_candy:
                max_candy = temp_candy

    for col in range(n):
        temp_candy = 1
        for row in range(n - 1):
            if candy[row][col] == candy[row + 1][col]:
                temp_candy += 1
            else:
                temp_candy = 1
            if temp_candy > max_candy:
                max_candy = temp_candy

    return max_candy


for row in range(n):
    for col in range(n - 1):
        if candy_list[row][col] != candy_list[row][col + 1]:
            temp = candy_list[row][col]
            candy_list[row][col] = candy_list[row][col + 1]
            candy_list[row][col + 1] = temp

            if max_candy < candy_count(candy_list):
                max_candy = candy_count(candy_list)

            temp = candy_list[row][col+1]
            candy_list[row][col+1] = candy_list[row][col]
            candy_list[row][col] = temp

for col in range(n):
    for row in range(n-1):
        if candy_list[row][col] != candy_list[row+1][col]:
            temp = candy_list[row][col]
            candy_list[row][col] = candy_list[row+1][col]
            candy_list[row+1][col] = temp

            if max_candy < candy_count(candy_list):
                max_candy = candy_count(candy_list)

            temp = candy_list[row+1][col]
            candy_list[row+1][col] = candy_list[row][col]
            candy_list[row][col] = temp

print(max_candy)