def solution(answers):
    answer = []
    count = [0]*3
    patterns = [[1,2,3,4,5],
              [2,1,2,3,2,4,2,5],
              [3,3,1,1,2,2,4,4,5,5]]
    for num, pattern in enumerate(patterns):
        for i in range(len(answers)):
            pattern_index = i % len(pattern)
            if answers[i] == pattern[pattern_index]:
                count[num] += 1
    
    max_score = max(count)
    for i in range(len(count)):
        if max_score == count[i]:
            answer.append(i+1)
    
    return answer