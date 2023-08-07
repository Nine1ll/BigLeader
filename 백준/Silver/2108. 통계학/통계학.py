import math
import sys

n = int(sys.stdin.readline())


def second_smallest_mode(nums):
    # 각 항목의 빈도를 계산
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # 최대 빈도를 찾기
    max_freq = max(freq.values())

    # 최대 빈도를 가진 항목들 찾기
    modes = [num for num, count in freq.items() if count == max_freq]

    # 최빈값들 중 두번째로 작은 값 찾기
    modes.sort()
    if len(modes) > 1:
        return modes[1]
    else:
        return modes[0]


num_K = []
for _ in range(n):
    num_K.append(int(sys.stdin.readline()))

num_K.sort()
print(round(sum(num_K) / n))
print(num_K[math.ceil(n / 2) - 1])
print(second_smallest_mode(num_K))
print(max(num_K) - min(num_K))