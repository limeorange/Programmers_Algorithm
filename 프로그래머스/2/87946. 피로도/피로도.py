# 250326 수 PM 8:43 (17m)

from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    # 던전 순서 셔플 (중복없는 순열): len(dungeons)!
    for p in permutations(dungeons):
        cur_k = k
        cnt = 0
        for d in p:
            if cur_k >= d[0]:
                cur_k -= d[1]
                cnt += 1
            else:
                break
        answer.append(cnt)
    return max(answer)