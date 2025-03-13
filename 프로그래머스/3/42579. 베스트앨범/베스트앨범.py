# 250313 목 PM 7:15

from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(list)
    gen_dic = defaultdict(int)
    answer = []
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        gen_dic[g] += p
        dic[g].append((i, p))
    top2_info = sorted(gen_dic.items(), key=lambda x:-x[1])
    
    for gen in top2_info:
        g1 = sorted(dic[gen[0]], key=lambda x:(-x[1], x[0]))
        for i in g1[:2]:
            answer.append(i[0])
    return answer