# 250328 금 PM 6:00 / DFS+백트래킹

def solution(tickets):
    
    # 조건) 가능한 경로가 2개 이상일 경우, 알파벳 순서로 경로 return
    tickets.sort()
    visited = [False] * (len(tickets))
    
    def DFS(cur, route):
        # 정답 처리 (모든 티켓을 사용한 경우)
        if len(route) == len(tickets)+1:
            return route
        
        # 방문할 노드(공항) 탐색 => 방문X & 연결O(현뒤=미앞)
        for i in range(len(tickets)):
            start, end = tickets[i]
            if not visited[i] and start == cur:
                visited[i] = True
                result = DFS(end, route + [end])
                if result:
                    return result
                # result == None인 경우(티켓을 모두 쓰지 못하는 경우)
                # visited의 방문을 취소함으로써 이전 단계로 돌아가서 다른 노드 탐색
                visited[i] = False
        return None
    return DFS('ICN', ['ICN'])