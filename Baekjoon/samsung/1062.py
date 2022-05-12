import sys
input = sys.stdin.readline
from itertools import combinations

n, k = map(int, input().split())
words = [set(input().replace('\n', '')).difference('a','n','t','i','c') for _ in range(n)]

if k < 5:
    print(0)
    sys.exit()
elif k == 26:
    print(n)
    sys.exit()
    
letters = {chr(i + 97): i for i in range(26)}
alpha = [i for i in range(26) if chr(i + 97) not in ['a', 'n', 't', 'i', 'c']]

result = 0
for combi in combinations(alpha, k-5):
    masking = 0
    for move in combi:
        masking |= 1 << move
    
    count = 0
    for word in words:
        word_bit = 0
        for char in word:
            word_bit |= 1 << letters[char]
        if masking | word_bit == masking:
            count += 1
    result = max(count, result)

print(result)