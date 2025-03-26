# 250326 수 PM 1:56

from itertools import permutations

def is_sosu(N): 
    if N <= 1:
        return False
    else:
        for i in range(2, N):
            if N % i == 0:
                return False
    return True

def solution(numbers):
    
    # 가능한 중복조합 (1~7개) 구해서 후보 숫자 구하기
    numbers = list(map(int, numbers))
    lst = []
    for i in range(1, 8):
        lst.extend(list(permutations(numbers, i)))
    lst = set(lst)
    print(lst)
    
        
    # 소수 목록 => 총 개수 구하기
    answer = 0
    uni_lst = []
    for n in lst:
        cur_num = ''
        for i in n:
            cur_num += str(i)
        uni_lst.append(int(cur_num))
    uni_lst = set(uni_lst)
    
    for un in uni_lst:
        if is_sosu(un):
            answer += 1
    return answer