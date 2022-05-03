import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
d, s = [], []
for _ in range(m):
    input_d, input_b = map(int, input().split())
    d.append(input_d)
    s.append(input_b)

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[n-1,0], [n-1,1], [n-2,0], [n-2,1]]
visited = [[0]*n for _ in range(n)]

def move(d, s):
    global cloud
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + dx[d] * s) % n
        cloud[i][1] = (cloud[i][1] + dy[d] * s) % n
        graph[cloud[i][0]][cloud[i][1]] += 1
        visited[cloud[i][0]][cloud[i][1]] = 1
    cloud = []

def water():
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, 1, -1]
    for x in range(n):
        for y in range(n):
            if visited[x][y] != 0:
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 0:
                        graph[x][y] += 1

def make():
    global visited
    for i in range(n):
        for j in range(n):
            if visited[i][j] != 0:
                visited[i][j] = 0
            elif graph[i][j] >= 2:
                cloud.append([i, j])
                graph[i][j] -= 2

for i in range(m):
    move(d[i], s[i])
    water()
    make()

result = sum([sum(a) for a in graph])
print(result)