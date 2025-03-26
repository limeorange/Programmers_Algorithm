# 250326 수 PM 9:01 ~ 9:37

'''
1. 아이디어
1) wires에서 요소를 하나씩 빼보면서, 두 파트의 송전탑 수를 DFS로 구한 후 차이 계산
2) len(wires)개의 차이값 중 최솟값 반환
'''

def solution(n, wires):
    
    # DFS 중첩함수로 작성
    def DFS(idx, graph, visited):
        nonlocal cnt
        
        # 재방문 방지
        visited[idx] = True
        
        # 송전탑 수 카운팅
        cnt += 1

        # 방문할 노드 탐색
        for i in graph[idx]:
            if not visited[i]:
                DFS(i, graph, visited)
        return cnt
    
    answer = []
    # wires에서 하나씩 연결 끊어보기
    for i in range(n-1):
        wires_ = wires.copy()
        wires_.pop(i)
        
        # 2차원 빈리스트 그래프 생성
        graph = [[] for _ in range(n+1)]
        for w in wires_:
            a, b = w[0], w[1] # 1, 3
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * (n+1)
        
        cnt_lst = []
        for i in range(1, n+1): # 1번 ~ n번 노드 방문 가능성 탐색
            if not visited[i]:
                cnt = 0
                DFS(i, graph, visited)
                cnt_lst.append(cnt)
        answer.append(abs(cnt_lst[0]-cnt_lst[1]))
    return min(answer)