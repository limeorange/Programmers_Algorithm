# 250329 토 PM 1:35 / 그래프+다익스트라
'''
1. 다익스트라: 출발지에서 모든 노드로의 최단거리 구하는 알고리즘 (가중치 있는 경우)
- 핵심 로직: 가까운 노드부터 차례로 방문하면서 더 빠른 경로가 있으면 갱신
- 핵심 자료구조: 우선순위 큐 => '최단 거리' 노드 탐색 보장 (가까운 마을 먼저 처리)
'''

import heapq

def solution(N, road, K):
    # 1. 그래프 생성 (2차원 빈 리스트)
    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append((b, c)) # (마을, 시간)
        graph[b].append((a, c)) # 양방향 도로이므로 b -> a도 추가
    
    # 2. 다익스트라를 위한 거리 배열 초기화
    distance = [float('inf')] * (N+1)
    distance[1] = 0
    
    # 3. 우선순위 큐(heapq) 사용
    heap = [(0, 1)] # (거리, 마을)
    
    while heap:
        dist, cur = heapq.heappop(heap) # (0, 1)
        
        # 이미 더 짧은 거리로 방문한 경우 패스
        if dist > distance[cur]:
            continue
        
        # 인접 노드 확인
        for neighbor, cost in graph[cur]: # (2, 1), (4, 2)
            new_dist = dist + cost # 0 + 1
            # 1번에서 이웃 노드까지의 최단 거리 갱신 
            if new_dist < distance[neighbor]: # 1 < inf
                distance[neighbor] = new_dist # dis[2] = 1
                heapq.heappush(heap, (new_dist, neighbor)) # (1, 2)
    
    # 4. K 이하의 거리인 마을 개수 세기
    answer = 0
    for d in distance:
        if d <= K:
            answer += 1
    return answer