# 250314 금 PM 11:34

'''
1. min_heap, max_heap 따로 만들어서 최솟값, 최댓값 구하기
2. heap_dic을 통해 유효한 값 판별하고, 두 개의 heap 동기화
'''

import heapq as hq
from collections import defaultdict

def solution(operations):
    min_heap = []
    max_heap = []
    heap_dic = defaultdict(int)
    
    for op in operations:
        if op[0] == 'I':
            num = int(op[2:])
            hq.heappush(min_heap, num)
            hq.heappush(max_heap, -num)
            heap_dic[num] += 1
            
        elif op == 'D 1':
            # 동기화 (실제 존재하지 않는 값 제거)
            while max_heap and heap_dic[-max_heap[0]] == 0:
                hq.heappop(max_heap)
            if max_heap:
                max_val = -hq.heappop(max_heap)
                heap_dic[max_val] -= 1
                
        elif op == 'D -1':
            while min_heap and heap_dic[min_heap[0]] == 0:
                hq.heappop(min_heap)
            if min_heap:
                min_val = hq.heappop(min_heap)
                heap_dic[min_val] -= 1
    
    while max_heap and heap_dic[-max_heap[0]] == 0:
        hq.heappop(max_heap)
        
    while min_heap and heap_dic[min_heap[0]] == 0:
        hq.heappop(min_heap)

    return [-max_heap[0], min_heap[0]] if min_heap else [0, 0]