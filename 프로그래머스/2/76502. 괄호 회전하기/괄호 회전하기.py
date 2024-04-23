def check_pairs(string,stack):
    for s in string:
        if s == "(" or s == "{" or s == "[":
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == "(":
                stack.pop()
            elif not stack:
                return 0
        elif s == ']':
            if stack and stack[-1] == "[":
                stack.pop()
            elif not stack:
                return 0
        elif s == '}':
            if stack and stack[-1] == "{":
                stack.pop()
            elif not stack:
                return 0
    
    if stack:
        return 0
    else:
        return 1

def solution(s):
    # 회전 // 올바른 괄호 문자열?
    # 회전
    stack = []
    answer = 0
    for i in range(len(s)):
        rotation = s[i:] + s[:i]
        answer += check_pairs(rotation,stack)
    return answer