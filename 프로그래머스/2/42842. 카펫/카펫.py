# 250326 수 PM 6:58

'''
1. 아이디어
- yellow = (가로-2) * (세로-2)
- 세로가 가로보다 짧으므로 3부터 순차적으로 값을 더해나가면서
- 'total의 약수' & 'yellow 넓이 조건'에 부합하는 [w, h] 찾기
'''

def solution(brown, yellow):
    total = brown + yellow
    # 세로 길이는 최소 3부터 가능 (갈-노-갈)
    for h in range(3, total):
        if total % h == 0:
            w = total // h
            if (w-2) * (h-2) == yellow:
                return [w, h]