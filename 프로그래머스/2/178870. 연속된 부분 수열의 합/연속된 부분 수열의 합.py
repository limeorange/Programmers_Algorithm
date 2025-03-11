# 250312 수 AM 12:36

def solution(s, k):
    left, right = 0, 0
    current_sum = s[0]
    min_length = float('inf')
    answer = [-1, -1]
    
    while right < len(s):
        # 부분합이 k보다 작은 경우 => 부분합의 우측 요소 추가(right++)
        if current_sum < k:
            right += 1
            if right < len(s):
                current_sum += s[right]
                
        # 부분합이 k보다 큰 경우 => 부분합의 좌측 요소 제거(left++)
        elif current_sum > k:
            current_sum -= s[left]
            left += 1
        
        # 부분합이 k인 경우 => 최소 길이 갱신 가능하면 answer 변경
        else:
            if (right-left) < min_length:
                min_length = right-left
                answer = [left, right]
        
            # answer를 찾았어도 뒤에서 길이가 더 짧은 부분합이 나올 수도 있음
            current_sum -= s[left]
            left += 1
    return answer