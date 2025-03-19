# 250319 수 PM 7:01

def solution(s):
    stack = []
    for i in s:
        if stack and stack[0] == ')':
            return False
        if stack and stack[-1] == '(' and i == ')':
            stack.pop()
        else:
            stack.append(i)
    return True if len(stack) == 0 else False