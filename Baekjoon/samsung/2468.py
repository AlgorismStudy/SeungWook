import sys
input = sys.stdin.readline
import copy
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(num):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and copy_g[nx][ny] > num:
                queue.append([nx, ny])
                copy_g[nx][ny] = -1

height = 1
for i in range(min(min(graph)), max(max(graph))):
    copy_g = copy.deepcopy(graph)
    count = 0
    for j in range(n):
        for k in range(n):
            if copy_g[j][k] > i:
                queue.append([j,k])
                copy_g[j][k] = -1
                count += 1
                bfs(i)
    height = max(height, count)

print(height)