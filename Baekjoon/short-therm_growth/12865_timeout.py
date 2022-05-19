import sys
input = sys.stdin.readline
from itertools import combinations

n, k = map(int, input().split())

answer = -1
dic = {}
for _ in range(n):
    w, v = map(int, input().split())
    dic[w] = v
    if v > answer:
        answer = v

for num in range(2, n+1):
    for i in combinations(dic.keys(), num):
        if sum(i) <= k:
            result = 0
            for j in i:
                result += dic[j]
            if result > answer:
                answer = result

print(answer)