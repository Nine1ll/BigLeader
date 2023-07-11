import sys

str_in = list(sys.stdin.readlines())
str_in = str_in[:len(str_in)-1]
c_str = ['c=','c-','dz=','d-','lj','nj','s=','z=']
str_in_c = "c=-dzljnjsz"
cnt = 0
char = ''
print(str_in)

for c in str_in:
    if c in str_in_c:
        char+=c
        print(c, char)
        if char in c_str:
            cnt+=1
            char=''
    else:
        cnt+=1

