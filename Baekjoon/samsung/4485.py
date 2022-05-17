import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

num = 0
while 1:
    n = int(input())
    if n == 0:
        sys.exit()
        
    graph = [list(map(int, input().split())) for _ in range(n)]
    money = [[9*n*n]*n for _ in range(n)]
    
    q = deque([[0,0]])
    money[0][0] = graph[0][0]
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if money[x][y] + graph[nx][ny] < money[nx][ny]:
                    money[nx][ny] = money[x][y] + graph[nx][ny]
                    q.append([nx, ny])
    num += 1
    print('Problem',str(num)+':',money[n-1][n-1])