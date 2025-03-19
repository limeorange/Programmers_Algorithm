# 250319 수 PM 10:00

def solution(prices):
    answer = [0] * len(prices)  # 결과 배열 (모든 시간을 0으로 초기화)
    stack = []  # 스택 초기화 (인덱스를 저장)

    for i, price in enumerate(prices):  # 주식 가격을 하나씩 확인
        while stack and prices[stack[-1]] > price:  # 가격이 하락하면 스택에서 꺼냄
            j = stack.pop()
            answer[j] = i - j  # 현재 시간(i)에서 스택에서 꺼낸 시간(j) 빼기
        
        stack.append(i)  # 현재 인덱스를 스택에 저장

    while stack:  # 끝까지 가격이 안 떨어진 경우
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer