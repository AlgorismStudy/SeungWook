import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for _ in range(N)]

print(Counter(sorted(numbers)).most_common(1)[0][0])