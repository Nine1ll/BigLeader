## https://www.acmicpc.net/problem/12605

import sys

N = int(sys.stdin.readline())
sentences = []
for i in range(N):
    sentence = list(sys.stdin.readline().split())
    sentences.append(sentence)

for i, sentence in enumerate(sentences):
    length = len(sentence)
    print(f"Case #{i + 1}:", end=" ")
    for j in range(length):
        if j == 0 and j != length-1:
            print(f"{sentence.pop()}", end=" ")
        elif j == length-1:
            print(sentence.pop())
        else:
            print(sentence.pop(), end=" ")
