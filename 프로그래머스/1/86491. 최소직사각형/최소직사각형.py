# 250326 수 PM 1:06 (6m)

def solution(sizes):
    w, h = [], []
    for s1, s2 in sizes:
        if s1 > s2:
            w.append(s1)
            h.append(s2)
        else:
            w.append(s2)
            h.append(s1)
    answer = max(w)*max(h)
    return answer