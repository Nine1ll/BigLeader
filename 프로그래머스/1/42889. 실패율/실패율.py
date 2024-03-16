def solution(N, stages):
    stages.sort()
    failure_rate = [0]*(N+1)
    for i in list(set(stages)):
        if i > N: #이건 클리어임
            continue
        k = stages.index(i) #정렬했으니 이 인덱스 뒤로는 i와 같거나 큼 
        n = stages.count(i) # 도달 O & 클리어 X i의 개수
        bigger_n = len(stages[k:]) # 도달 O i보다 큰 숫자의 개수
        failure_rate[i] = n / bigger_n

    answer = []
    for i in range(len(failure_rate)):
        max_rate = max(failure_rate)
        arg_max = failure_rate.index(max_rate)
        if arg_max == 0:
            continue
        answer.append(arg_max)
        failure_rate[arg_max] = 0
    for j in range(1,N+1):
        if j not in answer:
            answer.append(j)

    return answer