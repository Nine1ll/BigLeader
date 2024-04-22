def solution(N, stages):
    answer = []
    stage_users = len(stages)
    failure_rate = [0] * (N + 2)
    
    for i in range(1, N+1):
        if stages.count(i) == 0:
            failure_rate[i] = 0
        else:
            failure_rate[i] = stages.count(i) / stage_users
        stage_users -= stages.count(i)
    sort_failure = sorted(failure_rate[1:N+1] ,reverse = True)
        
    for ele in sort_failure:
        for j in range(1,len(failure_rate)-1):
            if ele == failure_rate[j]:
                if j not in answer:
                    answer.append(j)

    return answer