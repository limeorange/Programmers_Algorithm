# 250313 목 PM 4:31

from collections import Counter

def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    return list((p_counter-c_counter).keys())[0]