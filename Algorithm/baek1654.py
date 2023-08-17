import sys
'''
5 10
1
100
100
100
100
>>> 33
답 안나옴.. => 1을 버리고 다른 걸로 10개를 만들어야하는데...?
'''
k, n = map(int,sys.stdin.readline().split())


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


line_length = []
for _ in range(k):
    line_length.append(int(sys.stdin.readline()))

max_length = int(sum(line_length) / n)
for line_length_max in range(max_length, 1, -1):
    count_line = 0
    for ele in line_length:
        count_line += ele//line_length_max
    if count_line == n:
        print(line_length_max)
        break


        # while True:
        #     ele -= line_length_max
        #     if ele > 0:
        #         count_line+=1
        #     else:
        #         break