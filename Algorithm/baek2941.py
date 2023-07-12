croatia = list(input())
cnt = 0

for idx, c in enumerate(croatia):
    cnt+=1
    if c == '=':
        if croatia[idx-1] == 'z':
            try:
                if croatia[idx-2] == 'd':
                    cnt-=2
                else:
                    cnt-=1
            except:
                pass
        else:
            cnt-=1
    elif c == '-':
        cnt-=1
    elif c == 'j':
        if croatia[idx - 1] in 'nl':
            cnt-=1
    else:
        pass

print(cnt)
