def solution(numbers):
    numbers.sort()
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            add = numbers[i] + numbers[j]
            answer.append(add)
    answer = list(set(answer))
    answer.sort()
    return answer