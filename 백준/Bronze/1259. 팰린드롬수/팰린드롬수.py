import sys

while True:
    number = sys.stdin.readline().replace("\n", "")
    if not int(number):
        break
        
    reverse = ""
    for i in range(len(number) - 1, 0 - 1, -1):
        reverse += number[i]

    if reverse == number:
        print("yes")
    else:
        print("no")
