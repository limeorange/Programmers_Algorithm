# 250319 수 PM 8:12

''' 
1. (idx, p) 형태로 queue 만들기 => deque 활용
2. 우선순위 정보를 따로 저장해서 더 높은 우선순위가 있는지 파악 => sorted_p
3. queue 순차적으로 확인하면서 조건에 따른 처리 => while문

'''

from collections import deque

def solution(priorities, location):
    
    # 1) (idx, p) 형태로 queue 만들기
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((i, p))
    
    # 2) 최우선순위 여부 확인 위한 리스트 만들기
    sorted_p = sorted(priorities, reverse = True)
    
    # 3) queue 순차적으로 확인하면서 조건에 따른 처리
    answer = 0
    while queue:
        i, p = queue.popleft()
        if p < sorted_p[0]:
            queue.append((i, p))
        # p가 최우선순위인 경우 실행시키고, sorted_p 갱신
        else:
            answer += 1
            sorted_p.pop(0)
        
            # 현재 실행된 프로세스가 구하고자 하는 location인 경우
            if location == i:
                return answer