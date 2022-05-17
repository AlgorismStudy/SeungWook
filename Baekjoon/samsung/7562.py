import sys
input = sys.stdin.readline
from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(int(input())):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    
    q = deque([start])
    graph = [[0]*l for _ in range(l)]
    while q:
        x, y = q.popleft()
        
        if graph[x][y] == 0:
            graph[x][y] = 1
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

    print(graph[end[0]][end[1]]-1)