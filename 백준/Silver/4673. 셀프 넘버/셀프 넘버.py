def d(n):
    self_num = n
    for c in str(n):
        self_num += int(c)
    return self_num

not_self = []
for i in range(1, 10000+1):
    not_self.append(d(i))

for i in range(1, 10000+1):
    if i not in not_self:
        print(i)