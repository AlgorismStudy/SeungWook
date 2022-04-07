import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[[0,0] for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

queue = deque([(0, 0, 0)])
visited[0][0][0] = 1
result = -1
while queue:
    cur_x, cur_y, wall = queue.popleft()
    if cur_x == n - 1 and cur_y == m - 1:
        result = visited[cur_x][cur_y][wall]
        break
    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        
        if next_x <= -1 or next_x >= n or next_y <= -1 or next_y >= m:
            continue
        if graph[next_x][next_y] == 0 and visited[next_x][next_y][wall] == 0:
            queue.append((next_x, next_y, wall))
            visited[next_x][next_y][wall] = visited[cur_x][cur_y][wall] + 1
        if graph[next_x][next_y] == 1 and wall == 0:
            queue.append((next_x, next_y, wall + 1))
            visited[next_x][next_y][wall + 1] = visited[cur_x][cur_y][wall] + 1

print(result)