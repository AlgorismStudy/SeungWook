import sys
input = sys.stdin.readline
from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for i in range(n):
    nums = combinations(arr, i+1)
    for j in nums:
        if sum(j) == s:
            count += 1

print(count)