# 250324 월 PM 3:21

from collections import deque

def BFS(y, x, maps, answer, visited):
    
    N, M = len(maps), len(maps[0])
    
    # 1) 큐 생성 & 재방문 방지
    q = deque([(y, x)])
    visited[y][x] = True
    
    # 2) 방문할 노드 탐색 (상하좌우, 방문X, 연결O)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    
    while q:
        cur = q.popleft()
        cY, cX = cur[0], cur[1]
        
        # 정답 처리 (N-1, M-1) 도달한 경우
        if (cY, cX) == (N-1, M-1):
            answer = maps[cY][cX]
            return answer
            
        for i in range(4):
            nY = cY + dy[i]
            nX = cX + dx[i]
            if 0 <= nY < len(maps) and 0 <= nX < len(maps[0]):
                if maps[nY][nX] != 0 and not visited[nY][nX]:
                    visited[nY][nX] = True
                    maps[nY][nX] = maps[cY][cX] + 1
                    q.append((nY, nX))

def solution(maps):
    
    N, M = len(maps), len(maps[0])
    answer1 = -1
    visited = [[False] * M for _ in range(N)]
    
    # BFS 호출
    answer2 = BFS(0, 0, maps, answer1, visited)
    answer = answer2 if answer2 else answer1
    
    return answer