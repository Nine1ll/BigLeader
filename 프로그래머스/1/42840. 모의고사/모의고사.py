def solution(answers):
    patterns = [[1,2,3,4,5],
               [2,1,2,3,2,4,2,5],
               [3,3,1,1,2,2,4,4,5,5]]
    scores = [0]*3
    for i, pattern in enumerate(patterns):
        for j, answer in enumerate(answers):
            if answer == pattern[j % len(pattern)]:
                scores[i] += 1

    max_score = max(scores)
    answer = []
    
    for k, socre in enumerate(scores):
        if socre == max_score:
            answer.append(k+1)
    answer.sort()

    return answer