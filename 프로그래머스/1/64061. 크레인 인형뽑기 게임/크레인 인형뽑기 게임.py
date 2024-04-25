def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        # print(f'move : {move}')
        for i in range(len(board)):
            doll = board[i][move-1]
            # print(f"is_doll : {doll}")
            if doll:
                # print(f"doll : {doll}, stack : {stack}")
                if not stack: 
                    stack.append(doll)
                else:
                    if stack[-1] == doll:
                        stack.pop()
                        answer+=2
                        # print(f"answer : {answer}")
                    else:
                        stack.append(doll)
                board[i][move-1] = 0 
                # print(f"stack : {stack}\n")            
                break
                
    return answer