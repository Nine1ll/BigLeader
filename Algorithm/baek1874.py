import sys

N = int(sys.stdin.readline())

stack = []
sequence = [int(sys.stdin.readline()) for _ in range(N)]

for _, ele in enumerate(sequence):
    if ele in stack and ele == stack[-1]:
        stack.pop()
        print("+")
    else:
        for i in range(1, ele+1):
            stack.append(i)
            stack.pop()
            print("+")

print(sequence)

# 1부터 숫자를 쭉 집어 넣어서 입력 받은 수열을 만들 수 있나 보는 거임
# 근데 무조건 오름차순으로 그니까 작은 수부터 집어 넣어야함
# i-1, i, i+1 이 있을 때 연속된 숫자가 작은게 먼저 따닥 붙어 나오면 안됨.



