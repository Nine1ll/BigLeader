string = input()

N = len(string) // 10 + 1

output = ""
for i in range(len(string)):
    output += string[i]
    if len(output) == 10 or i == len(string) -1:
        print(output)
        output = ""

