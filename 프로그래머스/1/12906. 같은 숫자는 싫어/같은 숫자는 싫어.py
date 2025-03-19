# 250319 수 PM 6:20

def solution(arr):
    answer = []
    temp = -1
    for i, a in enumerate(arr):
        if temp == a:
            continue
        else:
            temp = a
            answer.append(a)
    return answer