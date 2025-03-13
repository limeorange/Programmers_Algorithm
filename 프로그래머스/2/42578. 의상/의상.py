# 250313 목 PM 6:22

from collections import defaultdict

def solution(clothes):
    dic = defaultdict(int)
    for cloth in clothes:
        dic[cloth[1]] += 1
    answer = 1
    for i in dic.values():
        answer *= (i+1)
    return answer-1