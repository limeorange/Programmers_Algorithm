# 250322 토 PM 11:58

def DFS(idx, visited, graph, answer):
    
    # 1) 재방문 방지
    visited[idx] = True
    
    # 2) 방문할 노드 탐색
    for i in graph[idx]:
        if not visited[i]:
            DFS(i, visited, graph, answer)

def solution(n, computers):
    y_len = len(computers)
    x_len = len(computers[0])
    
    graph = [[] for _ in range(y_len+1)]
    visited = [False] * (y_len+1)
    answer = 0
    
    # 1. map에 연결 정보 채우기
    
    for y in range(y_len):
        for x in range(x_len):
            if y != x and computers[y][x] == 1:
                graph[y+1].append(x+1)
    
    # 2. DFS 호출
    for i in range(1, y_len+1):
        if not visited[i]:
            DFS(i, visited, graph, answer)
            answer += 1            
    return answer