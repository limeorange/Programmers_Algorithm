# 250324 월 PM 3:21
# 전역변수 없이 인자로 변수 관리
# 정수는 immutable 타입이므로 함수 내부에서 값이 바뀌어도 외부에 반영되지 않음
# => return으로 정수값 반환하기!

from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    answer = -1
    visited = [[False] * M for _ in range(N)]
    
    # 1) 큐 생성 & 재방문 방지
    q = deque([(0, 0)])
    visited[0][0] = True
    
    # 2) 방문할 노드 탐색 (상하좌우, 방문X, 연결O)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    
    while q:
        cur = q.popleft()
        cY, cX = cur[0], cur[1]
        
        # 정답 처리 (N-1, M-1) 도달한 경우
        if (cY, cX) == (N-1, M-1):
            return maps[cY][cX]
            
        for i in range(4):
            nY = cY + dy[i]
            nX = cX + dx[i]
            if 0 <= nY < len(maps) and 0 <= nX < len(maps[0]):
                if maps[nY][nX] != 0 and not visited[nY][nX]:
                    visited[nY][nX] = True
                    maps[nY][nX] = maps[cY][cX] + 1
                    q.append((nY, nX))
    return answer