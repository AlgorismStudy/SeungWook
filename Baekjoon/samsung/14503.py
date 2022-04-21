import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph[r][c] = 2
count = 1

while True:
    for _ in range(4):
        d = (d-1) % 4
        nr = r + dx[d]
        nc = c + dy[d]
        
        if 0<=nr<n and 0<=nc<m and graph[nr][nc] == 0:
            graph[nr][nc] = 2
            r, c = nr, nc
            count += 1
            break
    else:
        nr = r + dx[(d+2) % 4]
        nc = c + dy[(d+2) % 4]
        if 0<=nr<n and 0<=nc<m and graph[nr][nc] != 1:
            r, c = nr, nc
        else:
            break
        
print(count)