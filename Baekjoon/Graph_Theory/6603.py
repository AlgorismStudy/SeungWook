import sys
input = sys.stdin.readline
from itertools import combinations

while 1:
    k_list = list(map(int, input().split()))
    if k_list[0] == 0:
        break
    for i in combinations(k_list[1:], 6):
        print(*i)
    print()