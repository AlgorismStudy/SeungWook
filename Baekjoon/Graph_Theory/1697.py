import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visit = [0] * 123456

dx = [-1, 1, 2]
queue = deque([n])

while queue:
    x = queue.popleft()
    if x == k:
        print(visit[x])
        break
    for i in dx:
        if i == 2: nx = x * i
        else: nx = x + i
        if 0<=nx<=100000 and visit[nx] == 0:
            visit[nx] = visit[x] + 1
            queue.append(nx)