import sys

start_channel = 100
buttons = [i for i in range(0, 9+1)]

N = int(sys.stdin.readline())
M = int(sys.stdin.readline()) # 고장난 버튼의 개수
broken_buttons =list(map(int,sys.stdin.readline().split()))
# 고장난 버튼을 빼고 가장 가까운 숫자로 가서 +, -를 누르면 되잖
# TODO 1: 가장 가까운 채널은?

print(N,M,broken_buttons)
broken_buttons.sort()
for button in reversed(broken_buttons):
    if button in buttons:
        buttons.remove(button)

print(buttons)

