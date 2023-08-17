import sys


def stack_sequence(n, sequence):
    stack = []
    result = []
    current = 1

    for num in sequence:
        while current <= num:
            print(num, current)
            stack.append(current)
            result.append('+')
            current += 1

        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            return ['NO']

    return result


n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]

result = stack_sequence(n, sequence)

for r in result:
    print(r)
