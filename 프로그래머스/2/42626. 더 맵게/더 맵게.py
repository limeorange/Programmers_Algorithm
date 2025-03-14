# 250314 금 PM 2:40 / heapq 활용

import heapq as hq

def solution(s, K):
    
    answer = 0
    hq.heapify(s)
    
    while len(s) >= 2:
        
        # 0번째 음식이 K 미만인 경우
        if s[0] < K:
            new_food = hq.heappop(s) + hq.heappop(s)*2
            hq.heappush(s, new_food)
            answer += 1
        
        # 모든 음식이 K 이상인 경우
        if s[0] >= K:
            break

    if s[0] < K:
        return -1
    else:
        return answer