# 250314 금 PM 6:40 / 우선순위 큐 => heap 활용

import heapq as hq

def solution(jobs):
    jobs.sort() # 요청시간 순 정렬
    heap = []
    i, total, time, count = 0, 0, 0, 0
    
    
    # 모든 작업을 처리할 때까지 반복
    while count < len(jobs):
        
        # 현재 진행 가능한 모든 작업 힙에 추가 (time 기준 판별)
        while i < len(jobs) and jobs[i][0] <= time:
            # (실행시간, 요청시간) 형태로 heap에 추가
            # 현재 진행 가능한 작업 중에서는 '실행시간'이 최우선순위가 되기 때문
            hq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
        
        # 현재 실행 가능한 작업이 힙에 있으면
        if heap:
            run_time, request_time = hq.heappop(heap)
            time += run_time
            total += (time - request_time)
            count += 1
            
        # 현재 실행 가능한 작업이 없으면 time을 다음 작업 요청시간으로 이동시킴
        else:
            time = jobs[i][0]
            
    return total // len(jobs)