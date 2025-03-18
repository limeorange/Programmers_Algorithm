# 250318 화 PM 9:30

def solution(array, commands):
    answer = []
    for c in commands:
        temp_arr = sorted(array[c[0]-1:c[1]])
        answer.append(temp_arr[c[2]-1])
    return answer