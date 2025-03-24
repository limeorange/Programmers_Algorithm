# 250324 월 PM 5:22

def solution(numbers, target):
    answer = 0
    
    # idx: 현재 numbers 리스트에서 몇 번째 숫자를 보고 있는지
    # total: 지금까지 선택한 숫자들의 합
    def dfs(idx, total):        
        nonlocal answer
        
        # 타겟 넘버를 찾은 경우 answer ++
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        
        dfs(idx + 1, total - numbers[idx])
        dfs(idx + 1, total + numbers[idx])
    
    dfs(0, 0)
    return answer