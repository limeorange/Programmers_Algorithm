# 250318 화 PM 10:28

def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if i >= citation:
            return i
    return len(citations)