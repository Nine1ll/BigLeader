import sys

word = sys.stdin.readline()

alpha_list = [chr(c) for c in range(65, 90+1)]
# print(alpha_list[0:2])
sum_ = 0
for c in word:
    if c in alpha_list[0:3]:
        sum_+=3
    elif c in alpha_list[3:6]:
        sum_+=4
    elif c in alpha_list[6:9]:
        sum_+=5
    elif c in alpha_list[9:12]:
        sum_+=6
    elif c in alpha_list[12:15]:
        sum_+=7
    elif c in alpha_list[15:19]:
        sum_+=8
    elif c in alpha_list[19:22]:
        sum_+=9
    elif c in alpha_list[22:]:
        sum_+=10
print(sum_)
