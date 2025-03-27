# 250327 목 PM 10:40

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0  # target이 words에 없으면 변환 불가
    
    visited = set()
    q = deque([(begin, 0)])  # (현재 단어, 변환 횟수)

    while q:
        word, cnt = q.popleft()

        if word == target:
            return cnt

        for w in words:
            if w not in visited and is_one_diff(word, w):
                visited.add(w)
                q.append((w, cnt + 1))

    return 0  # 도달 못함

# 현재 단어와 비교 단어가 1글자만 다르면 True
def is_one_diff(a, b):
    return sum([x != y for x, y in zip(a, b)]) == 1