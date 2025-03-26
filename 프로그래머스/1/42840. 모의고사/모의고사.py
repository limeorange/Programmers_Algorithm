# 250326 수 PM 1:30

'''
아이디어
1. 1번, 2번, 3번 수포자의 최소 반복 길이의 최소공배수 기준으로 맞은 개수 구하기
=> 5, 8, 10 => 40
=> answer의 길이가 어떻게 들어올지 모르기 때문에 변수화 해줘야 함
'''

def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    s1_cnt, s2_cnt, s3_cnt = 0, 0, 0
    for i in range(len(answers)):
        if s1[i % len(s1)] == answers[i]:
            s1_cnt += 1
        if s2[i % len(s2)] == answers[i]:
            s2_cnt += 1
        if s3[i % len(s3)] == answers[i]:
            s3_cnt += 1
    
    max_val = max(s1_cnt, s2_cnt, s3_cnt)
    answer = []
    if s1_cnt == max_val:
        answer.append(1)
    if s2_cnt == max_val:
        answer.append(2)
    if s3_cnt == max_val:
        answer.append(3)
    return answer