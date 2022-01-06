import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
N_number = list(map(int, input().split()))
M = int(input())
M_number = list(map(int, input().split()))

N_number = Counter(N_number)

for _ in M_number:
    print(N_number[_], end=" ")
