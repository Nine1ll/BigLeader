lst = [0 for i in range(100)]


for i in range(1, 6+1):
    lst[i] += 1
print(lst)

for i in range(3, 5+1):
    lst[i]+=1
print(lst)

print(lst.count(1))
print(lst.count(2))
