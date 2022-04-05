import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
ck = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        if graph[i][j] == 2:
            ck.append((i,j))

ckcom = list(combinations(ck, m))

result = 12345
for i in ckcom:
    ck_distance = 0
    for j in range(len(house)):
        distance = 12345
        for x, y in i:
            distance = min(distance, abs(x-house[j][0])+abs(y-house[j][1]))
        ck_distance += distance
    result = min(result, ck_distance)

print(result)