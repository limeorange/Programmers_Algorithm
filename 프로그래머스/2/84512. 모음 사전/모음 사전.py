# 250326 수 PM 8:03

from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    for i in range(1, 6):
        for p in product(vowels, repeat=i):
            words.append(''.join(p))
    
    words.sort()
    return words.index(word)+1