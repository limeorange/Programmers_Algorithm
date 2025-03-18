# 250318 화 PM 10:01

def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=lambda x:str(x)*3, reverse=True)
    answer = str(int(''.join(nums)))
    return answer