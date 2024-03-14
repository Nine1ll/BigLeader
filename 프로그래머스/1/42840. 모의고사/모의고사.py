import sys

def solution(answers):
    answer = []
    scores = [0] * 3
    patterns = [[1,2,3,4,5],
            [2,1,2,3,2,4,2,5],
            [3,3,1,1,2,2,4,4,5,5]]
    
    for i, pattern in enumerate(patterns):
        for j, number in enumerate(answers):
            if number == pattern[j % len(pattern)]:
                scores[i] += 1
    
    max_score = max(scores)

    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i+1)

    return answer

answer = list(map(int, sys.stdin.readline().split()))
print(solution(answer))