# 250319 수 PM 6:46

import numpy as np

def solution(progresses, speeds):
    days = []
    for i, p in enumerate(progresses):
        days.append(int(np.ceil((100-p)/speeds[i])))
        
    answer = []
    temp = days[0]
    cnt = 1
    for d in days[1:]:
        if d <= temp:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            temp = d
    answer.append(cnt)
    return answer